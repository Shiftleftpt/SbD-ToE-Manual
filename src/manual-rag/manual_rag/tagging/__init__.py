"""Auto-tagging module - RAG-based tag suggestions and integration"""

import re
import yaml
from pathlib import Path
from typing import List, Dict, Set, Tuple
from dataclasses import dataclass
from sentence_transformers import util
import json

from ..query import SemanticSearch
from ..config import MANUAL_ROOT, TAGS_FILE


@dataclass
class TagSuggestion:
    """A single tag suggestion with confidence"""
    tag: str
    confidence: float  # 0.0-1.0
    source: str  # 'rag', 'pattern', 'existing'
    reasoning: str  # Why this tag was suggested


class CanonicalTags:
    """Load and manage canonical tags"""
    
    def __init__(self, tags_file: Path = TAGS_FILE):
        self.tags_file = tags_file
        self.tags = self._load_tags()
        self.tag_names = set(self.tags.keys())
        # Build reverse index for aliases -> canonical
        self.alias_map = {}
        for tag, data in self.tags.items():
            if isinstance(data, dict) and 'aliases' in data:
                for alias in data.get('aliases', []):
                    self.alias_map[alias.lower()] = tag
    
    def _load_tags(self) -> Dict:
        """Load tags from YAML"""
        if not self.tags_file.exists():
            print(f"Warning: Tags file not found at {self.tags_file}")
            return {}
        
        try:
            with open(self.tags_file, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {}
        except Exception as e:
            print(f"Error loading tags: {e}")
            return {}
    
    def is_valid(self, tag: str) -> bool:
        """Check if tag is canonical or valid alias"""
        return tag.lower() in self.tag_names or tag.lower() in self.alias_map
    
    def normalize(self, tag: str) -> str:
        """Convert alias to canonical tag name"""
        tag_lower = tag.lower()
        if tag_lower in self.alias_map:
            return self.alias_map[tag_lower]
        if tag_lower in self.tag_names:
            return tag_lower
        return None
    
    def get_description(self, tag: str) -> str:
        """Get tag description"""
        normalized = self.normalize(tag)
        if normalized and isinstance(self.tags.get(normalized), dict):
            return self.tags[normalized].get('description', '')
        return ''


class AutoTagger:
    """Auto-tagger using RAG + pattern matching"""
    
    def __init__(self):
        self.searcher = SemanticSearch()
        self.canonical = CanonicalTags()
        # Compile patterns for common tag indicators
        self._compile_patterns()
    
    def _compile_patterns(self):
        """Compile regex patterns for tag detection"""
        self.patterns = {
            'cicd': re.compile(r'\b(ci[-/]?cd|pipeline|github\s+action|gitlab|jenkins|automation|deploy)', re.I),
            'arquitetura': re.compile(r'\b(architecture|design|pattern|system\s+design|componente|estrutura)', re.I),
            'threat-modeling': re.compile(r'\b(threat|attack|ameaça|stride|dfd|data\s+flow)', re.I),
            'testes': re.compile(r'\b(test|unit\s+test|integration|sast|dast|security\s+test)', re.I),
            'containers': re.compile(r'\b(container|docker|kubernetes|k8s|image|registry)', re.I),
            'dependencias': re.compile(r'\b(dependency|dependencies|sbom|supply\s+chain|vendor)', re.I),
            'criptografia': re.compile(r'\b(encrypt|crypto|cipher|certificate|tls|ssl|hash)', re.I),
            'autenticacao': re.compile(r'\b(auth|login|oauth|mfa|2fa|credential|password)', re.I),
        }
    
    def extract_patterns(self, content: str, title: str = '') -> Dict[str, float]:
        """Extract tag patterns from content
        
        Returns:
            Dict mapping tag names to confidence scores (0.0-1.0)
        """
        text = (title + ' ' + content).lower()
        
        matched_tags = {}
        for tag, pattern in self.patterns.items():
            # Count matches (more = higher confidence)
            matches = len(pattern.findall(text))
            if matches > 0:
                # Confidence based on match frequency, capped at 0.6
                confidence = min(0.6, matches * 0.15)
                matched_tags[tag] = confidence
        
        return matched_tags
    
    def suggest_from_rag(self, content: str, top_k: int = 5, context_file: str = None) -> Dict[str, float]:
        """Get tag suggestions from semantic search on content
        
        Args:
            content: Document content
            top_k: Number of similar documents to consider
            context_file: Optional file path to prioritize same-chapter results
        
        Returns:
            Dict mapping tag names to confidence scores
        """
        try:
            # Pass context_file to search for chapter-aware ranking
            results = self.searcher.search(content[:500], top_k=top_k, context_file=context_file)
            
            # Aggregate tags from similar documents
            tag_scores = {}
            for result in results:
                if 'tags' not in result or not result['tags']:
                    continue
                
                similarity = result.get('similarity', 0.0)
                # Confidence = similarity * tag frequency boost
                base_confidence = similarity * 0.8  # Scale similarity to 0.0-0.8
                
                for tag in result['tags']:
                    # Normalize tag
                    normalized = self.canonical.normalize(tag)
                    if not normalized:
                        continue
                    
                    # Update score (take max or accumulate?)
                    if normalized not in tag_scores:
                        tag_scores[normalized] = base_confidence
                    else:
                        # Average with slight boost for consensus
                        tag_scores[normalized] = (tag_scores[normalized] + base_confidence) / 2
                        tag_scores[normalized] *= 1.05  # +5% for consensus
        
        except Exception as e:
            print(f"Error getting RAG suggestions: {e}")
            tag_scores = {}
        
        return tag_scores
    
    def suggest_tags(self, file_path: str, content: str, title: str = '', 
                    existing_tags: List[str] = None,
                    min_confidence: float = 0.3) -> List[TagSuggestion]:
        """Generate tag suggestions combining RAG + patterns
        
        Args:
            file_path: Relative path in manual (for logging/reference only)
            content: File content
            title: Document title
            existing_tags: Tags already in file (for reference)
            min_confidence: Minimum confidence threshold for suggestions
        
        Returns:
            List of TagSuggestion objects, sorted by confidence
        """
        if existing_tags is None:
            existing_tags = []
        
        # Normalize existing tags
        existing_normalized = set()
        for tag in existing_tags:
            normalized = self.canonical.normalize(tag)
            if normalized:
                existing_normalized.add(normalized)
        
        suggestions = {}
        
        # 1. Get RAG suggestions (from similar documents in index)
        # Pass file_path so search can prioritize same-chapter results
        rag_suggestions = self.suggest_from_rag(content, context_file=file_path)
        for tag, confidence in rag_suggestions.items():
            if confidence >= min_confidence:
                suggestions[tag] = TagSuggestion(
                    tag=tag,
                    confidence=confidence,
                    source='rag',
                    reasoning=f'Found in {int(confidence*100)}% of similar documents'
                )
        
        # 2. Extract pattern-based suggestions
        pattern_suggestions = self.extract_patterns(content, title)
        for tag, confidence in pattern_suggestions.items():
            if confidence >= min_confidence:
                normalized = self.canonical.normalize(tag)
                if normalized:
                    if normalized not in suggestions:
                        suggestions[normalized] = TagSuggestion(
                            tag=normalized,
                            confidence=confidence,
                            source='pattern',
                            reasoning=f'Content keywords match pattern'
                        )
                    else:
                        # Boost confidence if both RAG and pattern agree
                        suggestions[normalized].confidence = min(1.0, suggestions[normalized].confidence + 0.15)
                        suggestions[normalized].source = 'rag+pattern'
                        suggestions[normalized].reasoning = 'RAG + keyword pattern agreement'
        
        # 3. Identify gaps - tags in similar docs but not existing
        for tag in rag_suggestions:
            if tag not in existing_normalized and tag not in suggestions:
                confidence = rag_suggestions[tag]
                if confidence >= min_confidence * 0.7:  # Lower threshold for potential gaps
                    suggestions[tag] = TagSuggestion(
                        tag=tag,
                        confidence=confidence * 0.9,  # Slightly lower confidence
                        source='rag',
                        reasoning=f'Present in similar documents (gap candidate)'
                    )
        
        # Sort by confidence descending
        result = sorted(suggestions.values(), key=lambda s: s.confidence, reverse=True)
        
        return result
    
    def merge_tags(self, existing_tags: List[str], 
                   suggested_tags: List[TagSuggestion],
                   strategy: str = 'conservative') -> Tuple[List[str], List[str]]:
        """Merge existing and suggested tags
        
        Args:
            existing_tags: Current tags in file
            suggested_tags: RAG suggestions (sorted by confidence)
            strategy: 'conservative' (>0.8 conf), 'balanced' (>0.6), 'aggressive' (>0.4)
        
        Returns:
            Tuple of (final_tags, new_tags_added)
        """
        thresholds = {
            'conservative': 0.8,
            'balanced': 0.6,
            'aggressive': 0.4
        }
        threshold = thresholds.get(strategy, 0.6)
        
        # Normalize existing tags
        final_tags_set = set()
        for tag in existing_tags:
            normalized = self.canonical.normalize(tag)
            if normalized:
                final_tags_set.add(normalized)
        
        # Add high-confidence suggestions
        new_tags = []
        for suggestion in suggested_tags:
            if suggestion.confidence >= threshold and suggestion.tag not in final_tags_set:
                final_tags_set.add(suggestion.tag)
                new_tags.append(suggestion.tag)
        
        final_tags = sorted(list(final_tags_set))
        return final_tags, new_tags


class FileTagUpdater:
    """Update markdown file frontmatter with tags"""
    
    @staticmethod
    def read_frontmatter(file_path: Path) -> Tuple[Dict, str]:
        """Extract frontmatter and content
        
        Returns:
            Tuple of (frontmatter_dict, content_without_frontmatter)
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        frontmatter = {}
        remaining_content = content
        
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    frontmatter = yaml.safe_load(parts[1]) or {}
                    remaining_content = parts[2]
                except yaml.YAMLError:
                    pass
        
        return frontmatter, remaining_content
    
    @staticmethod
    def write_frontmatter(file_path: Path, frontmatter: Dict, content: str):
        """Write updated frontmatter and content"""
        # Ensure tags is a list
        if 'tags' in frontmatter:
            if not isinstance(frontmatter['tags'], list):
                frontmatter['tags'] = list(frontmatter['tags'])
            # Remove duplicates, keep order
            seen = set()
            unique_tags = []
            for tag in frontmatter['tags']:
                if tag not in seen:
                    unique_tags.append(tag)
                    seen.add(tag)
            frontmatter['tags'] = unique_tags
        
        # Write back
        yaml_content = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)
        full_content = f"---\n{yaml_content}---\n{content}"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(full_content)
    
    @staticmethod
    def update_tags(file_path: Path, new_tags: List[str], dry_run: bool = False) -> Dict:
        """Update file tags
        
        Args:
            file_path: Path to markdown file
            new_tags: New tags to set
            dry_run: If True, return changes without writing
        
        Returns:
            Dict with old_tags, new_tags, changes
        """
        frontmatter, content = FileTagUpdater.read_frontmatter(file_path)
        old_tags = frontmatter.get('tags', [])
        
        changes = {
            'file': str(file_path),
            'old_tags': old_tags,
            'new_tags': new_tags,
            'added': [t for t in new_tags if t not in old_tags],
            'removed': [t for t in old_tags if t not in new_tags],
            'updated': old_tags != new_tags
        }
        
        if not dry_run and changes['updated']:
            frontmatter['tags'] = new_tags
            FileTagUpdater.write_frontmatter(file_path, frontmatter, content)
        
        return changes


# Export key classes for use by tools and scripts
__all__ = [
    'AutoTagger',
    'CanonicalTags',
    'FileTagUpdater',
    'TagSuggestion',
]

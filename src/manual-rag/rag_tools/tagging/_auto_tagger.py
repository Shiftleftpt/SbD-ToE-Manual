"""Auto-tagging - RAG-based tag suggestions"""

import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple
from dataclasses import dataclass

from ._tags import CanonicalTags

# Setup path for imports
_current_dir = Path(__file__).parent
_rag_tools_dir = _current_dir.parent
_root_dir = _rag_tools_dir.parent.parent

sys.path.insert(0, str(_root_dir))

from manual_rag.config import MANUAL_ROOT
from rag_core import SemanticSearch


@dataclass
class TagSuggestion:
    """A single tag suggestion with confidence
    
    Attributes:
        tag: Tag name (canonical)
        confidence: Confidence score (0.0-1.0)
        source: Source of suggestion ('rag', 'pattern', 'rag+pattern')
        reasoning: Explanation for the suggestion
    """
    tag: str
    confidence: float  # 0.0-1.0
    source: str  # 'rag', 'pattern', 'rag+pattern'
    reasoning: str  # Why this tag was suggested


class AutoTagger:
    """Auto-tagger using RAG + pattern matching
    
    Responsible for:
    - Pattern-based tag extraction (regex matching)
    - RAG-based suggestions (semantic search on similar docs)
    - Merging and ranking suggestions with confidence scores
    - Combining multiple sources (RAG + patterns)
    """
    
    def __init__(self):
        """Initialize auto-tagger with RAG searcher and canonical tags"""
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
        """Extract tag patterns from content using regex
        
        Args:
            content: Document content
            title: Document title (weighted higher)
        
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
        """Get tag suggestions from semantic search on similar documents
        
        Uses chapter-aware ranking: documents from same chapter as context_file
        are ranked higher.
        
        Args:
            content: Document content to find similar docs for
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
                    
                    # Update score: average with slight boost for consensus
                    if normalized not in tag_scores:
                        tag_scores[normalized] = base_confidence
                    else:
                        # Average existing score with new score
                        tag_scores[normalized] = (tag_scores[normalized] + base_confidence) / 2
                        tag_scores[normalized] *= 1.05  # +5% boost for consensus
        
        except Exception as e:
            print(f"Error getting RAG suggestions: {e}")
            tag_scores = {}
        
        return tag_scores
    
    def suggest_tags(self, file_path: str, content: str, title: str = '', 
                    existing_tags: List[str] = None,
                    min_confidence: float = 0.3) -> List[TagSuggestion]:
        """Generate tag suggestions combining RAG + patterns
        
        Merges suggestions from:
        1. RAG (semantic search on similar documents)
        2. Pattern matching (regex keywords)
        3. Gap analysis (tags in similar docs but not in current)
        
        Args:
            file_path: Relative path in manual (for chapter-aware search)
            content: File content
            title: Document title
            existing_tags: Tags already in file (for reference)
            min_confidence: Minimum confidence threshold for inclusion
        
        Returns:
            List of TagSuggestion objects, sorted by confidence (descending)
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
        """Merge existing and suggested tags with confidence threshold
        
        Applies strategy-based confidence thresholds:
        - conservative: > 0.8 (high confidence only)
        - balanced: > 0.6 (recommended)
        - aggressive: > 0.4 (include more suggestions)
        
        Args:
            existing_tags: Current tags in file
            suggested_tags: RAG suggestions (sorted by confidence)
            strategy: Confidence threshold strategy
        
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


__all__ = ["AutoTagger", "TagSuggestion"]

"""Recommendation engine - suggests tags based on content and context."""

from pathlib import Path
from typing import List, Set
from dataclasses import dataclass
from collections import defaultdict
import re

from ..core import CanonicalTagsManager


@dataclass
class Recommendation:
    """A tag recommendation."""
    tag: str
    confidence: float
    reason: str
    category: str = ""


class RecommendationEngine:
    """Suggests tags for markdown files based on analysis."""
    
    # Semantic relations between tags
    SEMANTIC_RELATIONS = {
        'sbom': ['supply-chain', 'sca', 'dependencias', 'oss'],
        'sca': ['sbom', 'supply-chain', 'dependencias', 'vulnerability'],
        'cicd': ['pipeline', 'deployment', 'iac', 'testing'],
        'testing': ['sast', 'dast', 'fuzzing', 'cicd'],
        'threat-modeling': ['architecture', 'design', 'compliance'],
        'governance': ['compliance', 'policy', 'audit'],
    }
    
    def __init__(self, canonical: CanonicalTagsManager):
        self.canonical = canonical
    
    def extract_frontmatter(self, filepath: str) -> dict:
        """Extract frontmatter from markdown file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
            if not match:
                return {}
            
            frontmatter_text = match.group(1)
            frontmatter = {}
            
            for line in frontmatter_text.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    frontmatter[key.strip()] = value.strip().strip('"\'')
            
            return frontmatter
        except Exception:
            return {}
    
    def extract_content_text(self, filepath: str) -> str:
        """Extract clean text from markdown (no code blocks)."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove frontmatter
            content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
            
            # Remove code blocks
            content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
            content = re.sub(r'`[^`]*`', '', content)
            
            # Remove HTML comments
            content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
            
            return content
        except Exception:
            return ""
    
    def get_parent_context_tags(self, filepath: str) -> List[str]:
        """Extract tags from parent chapter intro.md."""
        contextual_tags = []
        path_obj = Path(filepath)
        
        for parent in path_obj.parents:
            intro_path = parent / "intro.md"
            if intro_path.exists():
                frontmatter = self.extract_frontmatter(str(intro_path))
                if 'tags' in frontmatter:
                    tags_str = frontmatter['tags'].strip('[]')
                    if tags_str:
                        contextual_tags = [t.strip() for t in tags_str.split(',')]
                break
        
        return contextual_tags
    
    def recommend_tags(self, filepath: str, existing_tags: List[str] = None, 
                      max_recommendations: int = 5, min_confidence: float = 0.60) -> List[Recommendation]:
        """Generate tag recommendations for a file."""
        if existing_tags is None:
            frontmatter = self.extract_frontmatter(filepath)
            existing_tags_str = frontmatter.get('tags', '').strip('[]')
            existing_tags = [t.strip() for t in existing_tags_str.split(',')] if existing_tags_str else []
        
        recommendations = []
        existing_set = set(t.lower() for t in existing_tags)
        
        # Get context from parent chapter
        parent_tags = self.get_parent_context_tags(filepath)
        parent_set = set(t.lower() for t in parent_tags)
        
        # Extract content
        frontmatter = self.extract_frontmatter(filepath)
        title = frontmatter.get('title', Path(filepath).stem)
        description = frontmatter.get('description', '')
        content = self.extract_content_text(filepath)
        
        combined_text = f"{title} {description} {content}".lower()
        
        # Score each canonical tag
        scores = {}
        
        # Rule 1: Direct keyword match in content (HIGH confidence if found)
        for tag_name, tag_info in self.canonical.tags.items():
            if tag_name.lower() in existing_set:
                continue  # Already has tag
            
            score = 0.0
            reason_parts = []
            
            # Check tag name appears (STRONG signal - the tag name itself is in the document)
            if f" {tag_name} " in f" {combined_text} " or f"-{tag_name} " in f" -{combined_text}":
                score += 0.70  # INCREASED from 0.4 to 0.70 - direct keyword is strong evidence
                reason_parts.append("tag keyword")
            
            # Check keywords in description (moderate signal)
            elif tag_info.description and tag_info.description.lower() in combined_text:
                score += 0.50  # INCREASED from 0.3 to 0.50
                reason_parts.append("description match")
            
            # Rule 2: Semantic relation to parent tags
            for parent_tag in parent_set:
                if parent_tag in self.SEMANTIC_RELATIONS:
                    if tag_name.lower() in [t.lower() for t in self.SEMANTIC_RELATIONS[parent_tag]]:
                        score += 0.25
                        reason_parts.append(f"related to {parent_tag}")
                        break
            
            # Rule 3: Context boost from parent chapter (strong contextual signal)
            if tag_name.lower() in parent_set:
                score += 0.30  # INCREASED from 0.2 to 0.30
                reason_parts.append("context: parent chapter")
            
            # Rule 4: Related tags already present
            if tag_info.related:
                for related_tag in tag_info.related:
                    if related_tag.lower() in existing_set:
                        score += 0.20  # INCREASED from 0.15 to 0.20
                        reason_parts.append(f"related to existing tag")
                        break
            
            if score > 0 and score >= min_confidence:
                reason = "; ".join(reason_parts)
                scores[tag_name] = (min(score, 0.99), reason, tag_info.category)
        
        # Sort by score
        for tag_name, (score, reason, category) in sorted(scores.items(), key=lambda x: x[1][0], reverse=True):
            if len(recommendations) >= max_recommendations:
                break
            
            recommendations.append(Recommendation(
                tag=tag_name,
                confidence=score,
                reason=reason,
                category=category
            ))
        
        return recommendations

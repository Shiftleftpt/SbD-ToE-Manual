"""Canonical tags manager - single source of truth for all tags."""

import yaml
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass
import difflib


@dataclass
class TagInfo:
    """Information about a canonical tag."""
    name: str
    category: str
    description: str
    aliases: List[str]
    related: List[str]
    
    def to_dict(self) -> dict:
        return {
            'category': self.category,
            'description': self.description,
            'aliases': self.aliases,
            'related': self.related,
        }


class CanonicalTagsManager:
    """Manages canonical tags and their relationships."""
    
    def __init__(self, canonical_path: str):
        self.canonical_path = Path(canonical_path)
        self.tags: Dict[str, TagInfo] = {}
        self.load()
    
    def load(self):
        """Load canonical tags from YAML."""
        if not self.canonical_path.exists():
            raise FileNotFoundError(f"Canonical tags file not found: {self.canonical_path}")
        
        with open(self.canonical_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        # The YAML file is a flat dict of tags (no wrapper)
        tags_data = data or {}
        
        for tag_name, tag_config in tags_data.items():
            if isinstance(tag_config, dict):
                # Support both 'category' and 'label' fields
                category = tag_config.get('category') or tag_config.get('label', 'uncategorized')
                self.tags[tag_name] = TagInfo(
                    name=tag_name,
                    category=category,
                    description=tag_config.get('description', ''),
                    aliases=tag_config.get('aliases', []),
                    related=tag_config.get('related', [])
                )
    
    def get_tag(self, tag_name: str) -> Optional[TagInfo]:
        """Get tag by name."""
        return self.tags.get(tag_name)
    
    def find_similar_tag(self, query: str, threshold: float = 0.8) -> Optional[str]:
        """Find similar tag using fuzzy matching."""
        matches = difflib.get_close_matches(query, self.tags.keys(), n=1, cutoff=threshold)
        return matches[0] if matches else None
    
    def find_by_alias(self, alias: str) -> Optional[str]:
        """Find canonical tag by alias."""
        for tag_name, tag_info in self.tags.items():
            if alias.lower() in [a.lower() for a in tag_info.aliases]:
                return tag_name
        return None
    
    def get_all_tags(self) -> List[str]:
        """Get all canonical tag names."""
        return list(self.tags.keys())
    
    def get_tags_by_category(self, category: str) -> List[str]:
        """Get all tags in a category."""
        return [name for name, info in self.tags.items() if info.category == category]
    
    def get_related_tags(self, tag_name: str) -> List[str]:
        """Get tags related to a given tag."""
        tag = self.get_tag(tag_name)
        return tag.related if tag else []

"""Tag normalization and canonical tag management"""

import sys
import yaml
from pathlib import Path
from typing import Dict

# Setup path for imports
_current_dir = Path(__file__).parent
_rag_tools_dir = _current_dir.parent
_root_dir = _rag_tools_dir.parent.parent

sys.path.insert(0, str(_root_dir))

from rag_tools.config import TAGS_FILE


class CanonicalTags:
    """Load and manage canonical tags from YAML
    
    Responsible for:
    - Loading the canonical tag vocabulary
    - Validating tags against the canonical list
    - Normalizing aliases to canonical names
    - Providing tag metadata (descriptions, etc)
    """
    
    def __init__(self, tags_file: Path = TAGS_FILE):
        """Initialize with tags file
        
        Args:
            tags_file: Path to canonical-tags.yml
        """
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
        """Load tags from YAML file"""
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
        """Check if tag is canonical or valid alias
        
        Args:
            tag: Tag name to validate
            
        Returns:
            True if tag is valid (canonical or known alias)
        """
        return tag.lower() in self.tag_names or tag.lower() in self.alias_map
    
    def normalize(self, tag: str) -> str:
        """Convert alias to canonical tag name
        
        Args:
            tag: Tag name (canonical or alias)
            
        Returns:
            Canonical tag name, or None if not found
        """
        tag_lower = tag.lower()
        if tag_lower in self.alias_map:
            return self.alias_map[tag_lower]
        if tag_lower in self.tag_names:
            return tag_lower
        return None
    
    def get_description(self, tag: str) -> str:
        """Get tag description from metadata
        
        Args:
            tag: Tag name (will be normalized)
            
        Returns:
            Description string, or empty string if not found
        """
        normalized = self.normalize(tag)
        if normalized and isinstance(self.tags.get(normalized), dict):
            return self.tags[normalized].get('description', '')
        return ''


__all__ = ["CanonicalTags"]

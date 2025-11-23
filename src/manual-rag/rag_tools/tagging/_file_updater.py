"""File frontmatter operations - read/write YAML metadata"""

import yaml
from pathlib import Path
from typing import Dict, List, Tuple


class FileTagUpdater:
    """Update markdown file frontmatter with tags
    
    Responsible for:
    - Reading YAML frontmatter from markdown files
    - Writing updated frontmatter back to files
    - Managing tag lists in frontmatter (deduplication, sorting)
    """
    
    @staticmethod
    def read_frontmatter(file_path: Path) -> Tuple[Dict, str]:
        """Extract YAML frontmatter and content from markdown file
        
        Args:
            file_path: Path to markdown file
            
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
        """Write YAML frontmatter and content back to markdown file
        
        Args:
            file_path: Path to markdown file
            frontmatter: Dictionary to write as YAML
            content: Content after frontmatter
        """
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
        """Update file tags in frontmatter
        
        Args:
            file_path: Path to markdown file
            new_tags: New tags to set
            dry_run: If True, return changes without writing to file
        
        Returns:
            Dict with:
            - file: File path
            - old_tags: Previous tags
            - new_tags: New tags
            - added: Tags added
            - removed: Tags removed
            - updated: Whether file was changed
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


__all__ = ["FileTagUpdater"]

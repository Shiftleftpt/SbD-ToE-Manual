#!/usr/bin/env python3
"""
Extract cat_* and grp_* tags to dedicated frontmatter fields.

This is a one-off script to:
1. Extract cat_nnn tags → categoria: nnn field
2. Extract grp_nnn tags → group: nnn field
3. Remove cat_nnn and grp_nnn from tags list
"""

import sys
from pathlib import Path
import re
import yaml
from typing import Tuple, Optional, Dict, Any, List

def parse_markdown(content: str) -> Tuple[Dict[str, Any], str]:
    """Parse markdown with YAML frontmatter."""
    # Match frontmatter between --- markers
    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not match:
        return {}, content
    
    fm_text = match.group(1)
    body = match.group(2)
    
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError as e:
        print(f"ERROR: YAML parse error: {e}")
        return {}, content
    
    return fm, body


def build_markdown(fm: Dict[str, Any], body: str) -> str:
    """Build markdown with YAML frontmatter."""
    fm_text = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
    return f"---\n{fm_text}---\n{body}"


def extract_and_move_tags(fm: Dict[str, Any]) -> Tuple[bool, Optional[str], Optional[str]]:
    """
    Extract cat_* and grp_* from tags and move to separate fields.
    Returns: (modified, categoria_value, group_value)
    """
    tags = fm.get('tags', [])
    if not isinstance(tags, list):
        tags = []
    
    new_tags = []
    categoria = None
    group = None
    
    for tag in tags:
        if isinstance(tag, str):
            if tag.startswith('cat_'):
                categoria = tag[4:]  # Remove 'cat_' prefix
            elif tag.startswith('grp_'):
                group = tag[4:]  # Remove 'grp_' prefix
            else:
                new_tags.append(tag)
        else:
            new_tags.append(tag)
    
    modified = (categoria is not None or group is not None)
    
    if modified:
        fm['tags'] = new_tags
        if categoria:
            fm['categoria'] = categoria
        if group:
            fm['group'] = group
    
    return modified, categoria, group


def process_file(filepath: Path) -> bool:
    """Process a single markdown file."""
    try:
        content = filepath.read_text(encoding='utf-8')
        fm, body = parse_markdown(content)
        
        if not fm:
            print(f"⚠️  No frontmatter: {filepath.name}")
            return False
        
        # Extract and move tags
        modified, categoria, group = extract_and_move_tags(fm)
        
        if not modified:
            print(f"ℹ️  No cat_* or grp_* tags: {filepath.name}")
            return False
        
        # Build new content
        new_content = build_markdown(fm, body)
        filepath.write_text(new_content, encoding='utf-8')
        
        print(f"✅ {filepath.name}")
        if categoria:
            print(f"   → categoria: {categoria}")
        if group:
            print(f"   → group: {group}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error in {filepath.name}: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Find and process all intro.md files with cat_* or grp_* tags."""
    repo_root = Path(__file__).parent
    docs_root = repo_root / "manuals_src" / "docs"
    
    print(f"🔍 Searching for intro.md files in {docs_root}...\n")
    
    # Find all intro.md files
    intro_files = sorted(docs_root.glob("**/intro.md"))
    print(f"Found {len(intro_files)} intro.md files\n")
    
    updated = 0
    skipped = 0
    
    for filepath in intro_files:
        if process_file(filepath):
            updated += 1
        else:
            skipped += 1
    
    print(f"\n{'='*60}")
    print(f"📊 Results:")
    print(f"  Updated: {updated}")
    print(f"  Skipped: {skipped}")
    print(f"  Total: {len(intro_files)}")
    print(f"{'='*60}\n")
    
    return 0 if updated > 0 else 1


if __name__ == "__main__":
    sys.exit(main())

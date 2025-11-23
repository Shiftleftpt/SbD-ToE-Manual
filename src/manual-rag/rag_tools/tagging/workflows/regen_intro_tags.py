#!/usr/bin/env python3
"""
Regenerate tags for intro.md files after categoria/group extraction.

After removing cat_* and grp_* from tags, the intro.md files now have ~5 tags.
This script runs auto-tagging to bring them back to ~7 tags using HIGH-QUALITY
suggestions only (confidence >= 0.60, validated by recall test: 93% accuracy).

Strategy:
1. Only accept high-confidence suggestions (≥60%)
2. Preserve existing tags (user intent)
3. Add top suggestions up to 7 tags max
4. Always remove cat_* and grp_* (now in categoria/group fields)

Only targets intro.md files in sbd-toe/010-sbd-manual/* directories.
"""

import sys
from pathlib import Path
from typing import List

# Setup path for imports
_current_dir = Path(__file__).parent
sys.path.insert(0, str(_current_dir))

from rag_tools.tagging import AutoTagger, FileTagUpdater
from rag_core.config import MANUAL_ROOT


def find_intro_files() -> List[Path]:
    """Find all intro.md files in 010-sbd-manual chapters"""
    # MANUAL_ROOT points to sbd-toe, so we need to go up one level to docs
    docs_root = Path(MANUAL_ROOT).parent
    sbd_manual = docs_root / "sbd-toe" / "010-sbd-manual"
    
    intro_files = []
    for chapter_dir in sorted(sbd_manual.glob("[0-9][0-9]-*")):
        intro = chapter_dir / "intro.md"
        if intro.exists():
            intro_files.append(intro)
    
    return intro_files


def regen_tags(file_path: Path, strategy: str = 'balanced', max_tags: int = 7) -> bool:
    """Regenerate tags for a single intro.md file
    
    Args:
        file_path: Path to intro.md file
        strategy: Confidence threshold strategy ('conservative', 'balanced', 'aggressive')
        max_tags: Maximum number of tags to keep (besides preserved ones)
    
    Returns:
        True if updated, False otherwise
    """
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract frontmatter and body
        if not content.startswith('---'):
            print(f"⚠️  No frontmatter: {file_path.name}")
            return False
        
        parts = content.split('---', 2)
        if len(parts) < 3:
            print(f"⚠️  Invalid frontmatter: {file_path.name}")
            return False
        
        import yaml
        try:
            frontmatter = yaml.safe_load(parts[1]) or {}
            body = parts[2]
        except yaml.YAMLError as e:
            print(f"❌ YAML error in {file_path.name}: {e}")
            return False
        
        # Skip if categoria/group missing (not an intro.md we care about)
        if 'categoria' not in frontmatter or 'group' not in frontmatter:
            print(f"⚠️  Missing categoria/group: {file_path.name}")
            return False
        
        # Get existing tags
        existing_tags = frontmatter.get('tags', [])
        title = frontmatter.get('title', '')
        
        # Get auto-tagger suggestions
        tagger = AutoTagger()
        rel_path = str(file_path.relative_to(MANUAL_ROOT))
        
        # Get suggestions from RAG + patterns
        # Use higher min_confidence to ensure quality (recall test showed 93% with good quality)
        suggestions = tagger.suggest_tags(
            file_path=rel_path,
            content=body,
            title=title,
            existing_tags=existing_tags,
            min_confidence=0.60  # Only high-confidence suggestions (recall test baseline)
        )
        
        # Merge tags using strategy
        final_tags, new_tags = tagger.merge_tags(existing_tags, suggestions, strategy=strategy)
        
        # IMPORTANT: Remove cat_* and grp_* tags (we keep them only in categoria/group fields)
        final_tags_filtered = [t for t in final_tags if not (t.startswith('cat_') or t.startswith('grp_'))]
        
        # Filter to only HIGH-CONFIDENCE tags (>=0.60) to ensure quality
        # Keep existing tags (user intent) + high-confidence suggestions
        high_confidence_suggestions = {s.tag: s.confidence for s in suggestions if s.confidence >= 0.60}
        final_tags_filtered = [
            t for t in final_tags_filtered 
            if t in existing_tags or t in high_confidence_suggestions
        ]
        
        # Limit to max_tags if needed (preserve existing tags first, then top suggestions)
        if len(final_tags_filtered) > max_tags:
            # Priority: existing tags first, then by confidence
            existing_in_final = [t for t in final_tags_filtered if t in existing_tags]
            suggested_only = [t for t in final_tags_filtered if t not in existing_tags]
            suggested_only.sort(key=lambda t: high_confidence_suggestions.get(t, 0), reverse=True)
            
            final_tags_filtered = existing_in_final + suggested_only[:max_tags - len(existing_in_final)]
        
        new_tags_count = len(final_tags_filtered) - len([t for t in existing_tags if not (t.startswith('cat_') or t.startswith('grp_'))])
        
        if new_tags_count == 0:
            print(f"ℹ️  No new tags needed: {file_path.name}")
            return False
        
        # Update frontmatter
        frontmatter['tags'] = final_tags_filtered
        
        # Write back
        new_fm = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)
        new_content = f"---\n{new_fm}---\n{body}"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ {file_path.name}")
        print(f"   Previous: {len(existing_tags)} tags (w/ cat_*/grp_*)")
        print(f"   New: {len(final_tags_filtered)} tags (filtered)")
        if new_tags_count > 0:
            print(f"   Added: +{new_tags_count} new tag(s)")
        
        return True
        
    except Exception as e:
        print(f"❌ Error processing {file_path.name}: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main: regenerate tags for all intro.md files"""
    intro_files = find_intro_files()
    
    print(f"🔍 Found {len(intro_files)} intro.md files in 010-sbd-manual\n")
    print("=" * 80)
    print("Regenerating tags using auto-tagger (balanced strategy)")
    print("=" * 80 + "\n")
    
    if not intro_files:
        print("❌ No intro.md files found!")
        return 1
    
    updated = 0
    skipped = 0
    
    for file_path in intro_files:
        if regen_tags(file_path, strategy='balanced'):
            updated += 1
        else:
            skipped += 1
        print()
    
    print("=" * 80)
    print(f"📊 Results:")
    print(f"  Updated: {updated}")
    print(f"  Skipped: {skipped}")
    print(f"  Total: {len(intro_files)}")
    print("=" * 80 + "\n")
    
    return 0 if updated > 0 else 1


if __name__ == "__main__":
    sys.exit(main())

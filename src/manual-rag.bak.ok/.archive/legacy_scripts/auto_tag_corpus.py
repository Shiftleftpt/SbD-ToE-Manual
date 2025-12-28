#!/usr/bin/env python3
"""
Phase B-4: Apply BALANCED strategy to entire corpus (291 files)
Track changes and generate detailed delta report
"""

import json
from pathlib import Path
from typing import Dict, List
import sys
from datetime import datetime
import shutil

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "tag-normalization"))

from manual_rag.tagging import AutoTagger, FileTagUpdater
from rag_core.config import MANUAL_ROOT


def auto_tag_file(file_path: Path, strategy: str = 'balanced', dry_run: bool = False) -> Dict:
    """Auto-tag a single file and return delta information"""
    
    tagger = AutoTagger()
    frontmatter, content = FileTagUpdater.read_frontmatter(file_path)
    
    title = frontmatter.get('title', file_path.stem)
    existing_tags = frontmatter.get('tags', [])
    existing_set = set(existing_tags)
    
    # Get suggestions using BALANCED strategy
    suggestions = tagger.suggest_tags(
        str(file_path.relative_to(MANUAL_ROOT.parent)),
        content,
        title,
        existing_tags,
        min_confidence=0.60
    )
    
    # Merge using BALANCED strategy
    final_tags, new_tags = tagger.merge_tags(existing_tags, suggestions, strategy='balanced')
    final_set = set(final_tags)
    
    # Calculate changes
    added = final_set - existing_set
    removed = existing_set - final_set
    retained = existing_set & final_set
    
    delta = {
        'file': str(file_path.relative_to(MANUAL_ROOT.parent)),
        'chapter': file_path.parent.name,
        'existing_count': len(existing_set),
        'final_count': len(final_set),
        'added': sorted(list(added)),
        'removed': sorted(list(removed)),
        'retained': sorted(list(retained)),
        'added_count': len(added),
        'removed_count': len(removed),
        'changed': len(added) + len(removed) > 0,
        'change_magnitude': abs(len(added) - len(removed))
    }
    
    # Apply changes if not dry run
    if not dry_run and delta['changed']:
        try:
            frontmatter['tags'] = sorted(final_tags)
            FileTagUpdater.write_frontmatter(file_path, frontmatter, content)
            delta['status'] = 'updated'
        except Exception as e:
            delta['status'] = f'error: {str(e)}'
    elif dry_run:
        delta['status'] = 'dry_run'
    else:
        delta['status'] = 'no_change'
    
    return delta


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true', help='Dry run without writing changes')
    parser.add_argument('--sample', type=int, default=0, help='Limit to N files (0 = all)')
    args = parser.parse_args()
    
    dry_run = args.dry_run
    sample_size = args.sample
    
    print("\n" + "=" * 160)
    print("🚀 PHASE B-4: FULL CORPUS AUTO-TAGGING (BALANCED STRATEGY)")
    print("=" * 160)
    print(f"Mode: {'DRY RUN' if dry_run else 'WRITE MODE'}")
    print(f"Strategy: BALANCED (0.6 confidence threshold)")
    print("=" * 160)
    
    # Find all markdown files
    base_path = MANUAL_ROOT.parent
    all_files = sorted(list(base_path.rglob("*.md")))
    all_files = [f for f in all_files if not str(f).endswith('.2review')]
    
    # Filter to files with tags
    tagged_files = []
    for md_file in all_files:
        try:
            with open(md_file, 'r') as f:
                content = f.read()
                if 'tags: [' in content or "tags: '" in content:
                    tagged_files.append(md_file)
        except:
            pass
    
    if sample_size > 0:
        tagged_files = tagged_files[:sample_size]
    
    print(f"\nProcessing: {len(tagged_files)} files with existing tags")
    print(f"Out of: {len(all_files)} total markdown files\n")
    
    results = []
    chapters = {}
    
    for i, file_path in enumerate(tagged_files, 1):
        print(f"\r[{i:3}/{len(tagged_files)}] {file_path.name:50}", end="", flush=True)
        
        try:
            delta = auto_tag_file(file_path, dry_run=dry_run)
            results.append(delta)
            
            chapter = delta['chapter']
            if chapter not in chapters:
                chapters[chapter] = {'files': 0, 'changed': 0, 'total_added': 0, 'total_removed': 0}
            
            chapters[chapter]['files'] += 1
            if delta['changed']:
                chapters[chapter]['changed'] += 1
                chapters[chapter]['total_added'] += delta['added_count']
                chapters[chapter]['total_removed'] += delta['removed_count']
        
        except Exception as e:
            print(f"\n✗ ERROR: {file_path.name}: {str(e)}")
    
    print("\n")
    
    # Generate report
    print("\n" + "=" * 160)
    print("SUMMARY REPORT")
    print("=" * 160)
    
    total_files = len(results)
    changed_files = sum(1 for r in results if r['changed'])
    unchanged_files = total_files - changed_files
    
    total_added = sum(r['added_count'] for r in results)
    total_removed = sum(r['removed_count'] for r in results)
    
    print(f"\n📊 OVERALL STATISTICS")
    print(f"   Files processed: {total_files}")
    print(f"   Files changed: {changed_files} ({changed_files/total_files*100:.1f}%)")
    print(f"   Files unchanged: {unchanged_files} ({unchanged_files/total_files*100:.1f}%)")
    print(f"   Tags added: {total_added}")
    print(f"   Tags removed: {total_removed}")
    print(f"   Net change: {total_added - total_removed:+d}")
    
    # By chapter
    print(f"\n📂 BY CHAPTER")
    print("-" * 160)
    print(f"{'Chapter':<40} {'Files':<8} {'Changed':<10} {'Added':<8} {'Removed':<8} {'Net':<8}")
    print("-" * 160)
    
    for chapter in sorted(chapters.keys()):
        stats = chapters[chapter]
        net = stats['total_added'] - stats['total_removed']
        print(f"{chapter:<40} {stats['files']:<8} {stats['changed']:<10} "
              f"{stats['total_added']:<8} {stats['total_removed']:<8} {net:+d}")
    
    # Files with most changes
    print(f"\n🔝 TOP 10 FILES WITH MOST CHANGES")
    print("-" * 160)
    
    top_changes = sorted([r for r in results if r['changed']], 
                        key=lambda x: x['change_magnitude'], reverse=True)[:10]
    
    for i, r in enumerate(top_changes, 1):
        print(f"{i:2}. {r['file']:<60}")
        print(f"    Added: {', '.join(r['added'][:3])}{'...' if len(r['added']) > 3 else ''}")
        if r['removed']:
            print(f"    Removed: {', '.join(r['removed'][:3])}{'...' if len(r['removed']) > 3 else ''}")
        print()
    
    # Save detailed report
    timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    report_file = Path(__file__).parent / f"auto_tag_report_{timestamp}.json"
    
    report = {
        'timestamp': timestamp,
        'mode': 'dry_run' if dry_run else 'write',
        'strategy': 'balanced',
        'files_processed': total_files,
        'files_changed': changed_files,
        'files_unchanged': unchanged_files,
        'total_tags_added': total_added,
        'total_tags_removed': total_removed,
        'net_change': total_added - total_removed,
        'by_chapter': chapters,
        'file_deltas': results
    }
    
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n💾 Report saved: {report_file}")
    
    if dry_run:
        print(f"\n✅ DRY RUN COMPLETE - No files were modified")
        print(f"To apply changes, run with: python3 auto_tag_corpus.py")
    else:
        print(f"\n✅ AUTO-TAGGING COMPLETE - {changed_files} files updated")


if __name__ == "__main__":
    main()

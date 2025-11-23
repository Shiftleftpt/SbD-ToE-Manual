#!/usr/bin/env python3
"""Quick recall test after removing cat_*/grp_* from canonical tags"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from rag_tools.tagging import AutoTagger, FileTagUpdater
from rag_core.config import MANUAL_ROOT

def test_recall():
    """Test recall/precision metrics on a sample of files"""
    
    tagger = AutoTagger()
    base_path = MANUAL_ROOT.parent
    
    # Find some test files
    test_files = list(base_path.rglob("*.md"))[:10]
    test_files = [f for f in test_files if not str(f).endswith('.2review')]
    
    print("🧪 RECALL TEST - After Removing cat_*/grp_* from Canonical Tags")
    print("=" * 80)
    print()
    
    total_stats = {
        'files': 0,
        'avg_existing': 0,
        'avg_suggested': 0,
        'avg_recall': 0,
        'avg_precision': 0,
        'avg_f1': 0
    }
    
    for file_path in test_files[:5]:  # Test 5 files
        try:
            frontmatter, content = FileTagUpdater.read_frontmatter(file_path)
            if not frontmatter.get('tags'):
                continue
            
            existing_tags = frontmatter.get('tags', [])
            title = frontmatter.get('title', '')
            
            rel_path = str(file_path.relative_to(MANUAL_ROOT.parent))
            suggestions = tagger.suggest_tags(
                file_path=rel_path,
                content=content,
                title=title,
                existing_tags=existing_tags,
                min_confidence=0.3
            )
            
            suggested_tags = set(s.tag for s in suggestions)
            existing_set = set(existing_tags)
            
            # Check if any cat_* or grp_* were suggested
            cat_grp_suggested = [t for t in suggested_tags if t.startswith('cat_') or t.startswith('grp_')]
            
            re_detected = suggested_tags & existing_set
            recall = len(re_detected) / len(existing_set) if existing_set else 0
            precision = len(re_detected) / len(suggested_tags) if suggested_tags else 0
            f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
            
            print(f"📄 {file_path.name}")
            print(f"   Existing tags: {len(existing_set)}")
            print(f"   Suggested tags: {len(suggested_tags)}")
            print(f"   Re-detected: {len(re_detected)} (Recall: {recall:.0%}, Precision: {precision:.0%}, F1: {f1:.2f})")
            if cat_grp_suggested:
                print(f"   ⚠️  cat_*/grp_* STILL SUGGESTED: {cat_grp_suggested}")
            else:
                print(f"   ✅ No cat_*/grp_* suggested")
            print()
            
            total_stats['files'] += 1
            total_stats['avg_existing'] += len(existing_set)
            total_stats['avg_suggested'] += len(suggested_tags)
            total_stats['avg_recall'] += recall
            total_stats['avg_precision'] += precision
            total_stats['avg_f1'] += f1
            
        except Exception as e:
            print(f"❌ Error processing {file_path.name}: {e}")
            print()
    
    if total_stats['files'] > 0:
        print("=" * 80)
        print("📊 SUMMARY")
        print("=" * 80)
        print(f"Files tested: {total_stats['files']}")
        print(f"Avg existing tags: {total_stats['avg_existing'] / total_stats['files']:.1f}")
        print(f"Avg suggested tags: {total_stats['avg_suggested'] / total_stats['files']:.1f}")
        print(f"Avg Recall: {total_stats['avg_recall'] / total_stats['files']:.0%}")
        print(f"Avg Precision: {total_stats['avg_precision'] / total_stats['files']:.0%}")
        print(f"Avg F1: {total_stats['avg_f1'] / total_stats['files']:.2f}")
        print()
        print("✅ If no cat_*/grp_* are suggested above, the cleanup was successful!")


if __name__ == "__main__":
    test_recall()

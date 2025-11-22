#!/usr/bin/env python3
"""
Extended 4-Way Comparison - 20+ files for robust statistics
"""

import json
from pathlib import Path
from typing import Dict, List
from datetime import datetime
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "tag-normalization"))

from manual_rag.tagging import AutoTagger, FileTagUpdater
from manual_rag.config import MANUAL_ROOT


def run_comparison(file_path: Path, existing_tags: List[str]) -> Dict:
    """Run comparison on a single file"""
    
    tagger = AutoTagger()
    frontmatter, content = FileTagUpdater.read_frontmatter(file_path)
    title = frontmatter.get('title', file_path.stem)
    
    # Get RAG suggestions
    try:
        suggestions = tagger.suggest_tags(
            str(file_path.relative_to(MANUAL_ROOT.parent)),
            content,
            title,
            existing_tags,
            min_confidence=0.35
        )
        
        human_high = [s for s in suggestions if s.confidence >= 0.70]
        human_med = [s for s in suggestions if 0.50 <= s.confidence < 0.70]
        
        human_result = {
            'high': len(human_high),
            'medium': len(human_med),
            'error': None
        }
    except Exception as e:
        human_result = {
            'high': 0,
            'medium': 0,
            'error': str(e)
        }
    
    # Calculate metrics
    existing_set = set(existing_tags)
    human_high_set = set(s.tag for s in suggestions if s.confidence >= 0.70)
    
    human_recall = len(human_high_set & existing_set) / len(existing_set) if existing_set else 0
    human_precision = len(human_high_set & existing_set) / len(human_high_set) if human_high_set else 0
    
    return {
        'file': file_path.name,
        'chapter': file_path.parent.name,
        'existing_count': len(existing_tags),
        'human_high': len(human_high_set),
        'human_recall': round(human_recall, 3),
        'human_precision': round(human_precision, 3),
        'human_f1': round(2 * (human_precision * human_recall) / max(human_precision + human_recall, 0.001), 3),
        'error': human_result['error']
    }


def main():
    print("\n🔍 EXTENDED 4-WAY COMPARISON (20+ files)")
    print("=" * 130)
    
    # Find files with tags
    base_path = MANUAL_ROOT.parent
    all_files = sorted(list(base_path.rglob("*.md")))
    all_files = [f for f in all_files if not str(f).endswith('.2review')]
    
    test_files = []
    for md_file in all_files:
        try:
            with open(md_file, 'r') as f:
                content = f.read()
                if 'tags: [' in content or "tags: '" in content:
                    test_files.append(md_file)
                    if len(test_files) >= 20:
                        break
        except:
            pass
    
    print(f"Found {len(test_files)} files with tags\n")
    
    results = []
    for i, file_path in enumerate(test_files, 1):
        print(f"[{i:2}/{len(test_files)}] {file_path.name:40}", end=" ", flush=True)
        try:
            frontmatter, _ = FileTagUpdater.read_frontmatter(file_path)
            existing = frontmatter.get('tags', [])
            
            if not existing:
                print("(no tags)")
                continue
            
            result = run_comparison(file_path, existing)
            results.append(result)
            print(f"✓ recall={result['human_recall']*100:5.1f}% prec={result['human_precision']*100:5.1f}%")
        except Exception as e:
            print(f"✗ ({str(e)[:40]})")
    
    # Analysis
    print("\n" + "=" * 130)
    print("STATISTICS")
    print("=" * 130)
    
    if results:
        recalls = [r['human_recall'] for r in results]
        precisions = [r['human_precision'] for r in results]
        f1s = [r['human_f1'] for r in results]
        
        print(f"\nFiles analyzed:        {len(results)}")
        print(f"\nRecall (re-detecting existing tags):")
        print(f"  Min:                 {min(recalls)*100:6.1f}%")
        print(f"  Max:                 {max(recalls)*100:6.1f}%")
        print(f"  Avg:                 {sum(recalls)/len(recalls)*100:6.1f}%")
        print(f"  Median:              {sorted(recalls)[len(recalls)//2]*100:6.1f}%")
        
        print(f"\nPrecision (correctness of high-conf suggestions):")
        print(f"  Min:                 {min(precisions)*100:6.1f}%")
        print(f"  Max:                 {max(precisions)*100:6.1f}%")
        print(f"  Avg:                 {sum(precisions)/len(precisions)*100:6.1f}%")
        
        print(f"\nF1 Score (harmonic mean):")
        print(f"  Min:                 {min(f1s)*100:6.1f}%")
        print(f"  Max:                 {max(f1s)*100:6.1f}%")
        print(f"  Avg:                 {sum(f1s)/len(f1s)*100:6.1f}%")
        
        # Distribution
        print(f"\nRecall Distribution:")
        for threshold in [0.0, 0.25, 0.50, 0.75, 1.0]:
            count = sum(1 for r in recalls if threshold <= r < threshold + 0.25)
            pct = count * 100 / len(recalls)
            bar = "█" * int(pct / 5)
            print(f"  {threshold:.0%}-{threshold+0.25:.0%}: {count:2} files ({pct:5.1f}%) {bar}")
        
        # By chapter
        print(f"\nBy Chapter:")
        chapters = {}
        for r in results:
            ch = r['chapter']
            if ch not in chapters:
                chapters[ch] = []
            chapters[ch].append(r['human_recall'])
        
        for ch in sorted(chapters.keys()):
            vals = chapters[ch]
            avg = sum(vals) / len(vals) * 100
            print(f"  {ch:40} {len(vals):2} files  avg recall={avg:5.1f}%")
    
    # Save
    output_file = Path(__file__).parent / f"results/extended_comparison_{datetime.now().isoformat().replace(':', '-')}.json"
    output_file.parent.mkdir(exist_ok=True)
    
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Results saved: {output_file}")


if __name__ == "__main__":
    main()

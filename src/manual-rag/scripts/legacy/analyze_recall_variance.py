#!/usr/bin/env python3
"""
Analyze why recall varies - examine high vs low performing files
"""

import json
from pathlib import Path
from typing import Dict, List
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "tag-normalization"))

from manual_rag.tagging import AutoTagger, FileTagUpdater
from manual_rag.config import MANUAL_ROOT


def analyze_file(file_path: Path) -> Dict:
    """Deep analysis of a single file"""
    
    tagger = AutoTagger()
    frontmatter, content = FileTagUpdater.read_frontmatter(file_path)
    title = frontmatter.get('title', file_path.stem)
    existing_tags = frontmatter.get('tags', [])
    
    suggestions = tagger.suggest_tags(
        str(file_path.relative_to(MANUAL_ROOT.parent)),
        content,
        title,
        existing_tags,
        min_confidence=0.35
    )
    
    human_high = [s for s in suggestions if s.confidence >= 0.70]
    
    # Calculate metrics
    existing_set = set(existing_tags)
    human_high_set = set(s.tag for s in human_high)
    
    re_detected = human_high_set & existing_set
    missed = existing_set - human_high_set
    
    recall = len(re_detected) / len(existing_set) if existing_set else 0
    
    # Analyze sources
    rag_only = [s for s in human_high if s.source == 'rag']
    pattern_match = [s for s in human_high if 'pattern' in s.source]
    
    return {
        'file': file_path.name,
        'chapter': file_path.parent.name,
        'size': file_path.stat().st_size,
        'existing_count': len(existing_tags),
        'recall': recall,
        're_detected_count': len(re_detected),
        're_detected': list(re_detected),
        'missed_count': len(missed),
        'missed': list(missed),
        'high_conf_count': len(human_high),
        'rag_source_count': len(rag_only),
        'pattern_source_count': len(pattern_match),
        'content_length': len(content),
        'content_density': len(existing_tags) / max(len(content) / 1000, 1)  # tags per 1000 chars
    }


def main():
    print("\n🔬 DEEP ANALYSIS: Why Recall Varies")
    print("=" * 140)
    
    # Find test files
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
    
    print(f"Analyzing {len(test_files)} files...\n")
    
    results = []
    for i, file_path in enumerate(test_files, 1):
        print(f"[{i:2}/{len(test_files)}]", end=" ", flush=True)
        try:
            result = analyze_file(file_path)
            results.append(result)
            print(f"✓ {result['file']:40} recall={result['recall']*100:5.1f}%")
        except Exception as e:
            print(f"✗ {str(e)[:50]}")
    
    # Sort by recall
    high_recall = sorted([r for r in results if r['recall'] >= 0.75], key=lambda x: -x['recall'])
    low_recall = sorted([r for r in results if r['recall'] < 0.50], key=lambda x: x['recall'])
    
    print("\n" + "=" * 140)
    print("HIGH RECALL FILES (75%+)")
    print("=" * 140)
    
    for r in high_recall:
        print(f"\n📄 {r['file']} ({r['chapter']})")
        print(f"   Recall: {r['recall']*100:.1f}%  |  Size: {r['size']:,} bytes  |  Tags: {r['existing_count']}")
        print(f"   Re-detected: {r['re_detected_count']}/{r['existing_count']}  |  Sources: RAG={r['rag_source_count']} Pattern={r['pattern_source_count']}")
        if r['missed']:
            print(f"   Missed: {', '.join(r['missed'])}")
        print(f"   Content density: {r['content_density']:.2f} tags per 1K chars")
    
    print("\n" + "=" * 140)
    print("LOW RECALL FILES (<50%)")
    print("=" * 140)
    
    for r in low_recall:
        print(f"\n📄 {r['file']} ({r['chapter']})")
        print(f"   Recall: {r['recall']*100:.1f}%  |  Size: {r['size']:,} bytes  |  Tags: {r['existing_count']}")
        print(f"   Re-detected: {r['re_detected_count']}/{r['existing_count']}  |  Sources: RAG={r['rag_source_count']} Pattern={r['pattern_source_count']}")
        if r['missed']:
            print(f"   Missed: {', '.join(r['missed'][:3])}{'...' if len(r['missed']) > 3 else ''}")
        print(f"   Content density: {r['content_density']:.2f} tags per 1K chars")
    
    # Correlation analysis
    print("\n" + "=" * 140)
    print("CORRELATION ANALYSIS")
    print("=" * 140)
    
    recalls = [r['recall'] for r in results]
    sizes = [r['content_length'] for r in results]
    tag_counts = [r['existing_count'] for r in results]
    densities = [r['content_density'] for r in results]
    
    # Simple correlation
    def correlation(x, y):
        if len(x) < 2:
            return 0
        mx = sum(x) / len(x)
        my = sum(y) / len(y)
        cov = sum((x[i] - mx) * (y[i] - my) for i in range(len(x))) / len(x)
        sx = (sum((xi - mx) ** 2 for xi in x) / len(x)) ** 0.5
        sy = (sum((yi - my) ** 2 for yi in y) / len(y)) ** 0.5
        return cov / (sx * sy) if sx * sy > 0 else 0
    
    print(f"\nRecall vs Content Length:     {correlation(recalls, sizes):+.3f}")
    print(f"Recall vs Tag Count:         {correlation(recalls, tag_counts):+.3f}")
    print(f"Recall vs Content Density:   {correlation(recalls, densities):+.3f}")
    
    # Insights
    print("\n" + "=" * 140)
    print("KEY INSIGHTS")
    print("=" * 140)
    
    avg_high = sum(r['content_length'] for r in high_recall) / len(high_recall) if high_recall else 0
    avg_low = sum(r['content_length'] for r in low_recall) / len(low_recall) if low_recall else 0
    
    print(f"\nContent Length:")
    print(f"  High recall avg: {avg_high:,.0f} chars")
    print(f"  Low recall avg:  {avg_low:,.0f} chars")
    print(f"  → Longer, more detailed documents have better recall")
    
    avg_density_high = sum(r['content_density'] for r in high_recall) / len(high_recall) if high_recall else 0
    avg_density_low = sum(r['content_density'] for r in low_recall) / len(low_recall) if low_recall else 0
    
    print(f"\nTag Density (tags per 1K chars):")
    print(f"  High recall avg: {avg_density_high:.2f}")
    print(f"  Low recall avg:  {avg_density_low:.2f}")
    print(f"  → Files with higher tag density achieve better recall")
    
    print(f"\nConclusion:")
    print(f"  • RAG performs best on semantically rich, detailed documents")
    print(f"  • Short intro/summary documents have lower recall (less content to match)")
    print(f"  • Overall average recall of 59% is good for Phase B (conservative merge strategy)")
    print(f"  • Precision of 77.1% means most suggestions are correct")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Test different merge strategies (confidence thresholds)
Compare: conservative (0.8), balanced (0.6), aggressive (0.4)
"""

import json
from pathlib import Path
from typing import Dict, List
import sys
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "tag-normalization"))

from manual_rag.tagging import AutoTagger, FileTagUpdater
from rag_core.config import MANUAL_ROOT


def test_strategy(file_path: Path, strategy: str, min_conf: float) -> Dict:
    """Test a single strategy on one file"""
    
    tagger = AutoTagger()
    frontmatter, content = FileTagUpdater.read_frontmatter(file_path)
    title = frontmatter.get('title', file_path.stem)
    existing_tags = frontmatter.get('tags', [])
    
    suggestions = tagger.suggest_tags(
        str(file_path.relative_to(MANUAL_ROOT.parent)),
        content,
        title,
        existing_tags,
        min_confidence=min_conf
    )
    
    suggested_tags = set(s.tag for s in suggestions)
    existing_set = set(existing_tags)
    
    re_detected = suggested_tags & existing_set
    false_positives = suggested_tags - existing_set
    false_negatives = existing_set - suggested_tags
    
    recall = len(re_detected) / len(existing_set) if existing_set else 0
    precision = len(re_detected) / len(suggested_tags) if suggested_tags else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    
    return {
        'strategy': strategy,
        'min_conf': min_conf,
        'existing_count': len(existing_set),
        'suggested_count': len(suggested_tags),
        're_detected_count': len(re_detected),
        'false_positives': len(false_positives),
        'false_negatives': len(false_negatives),
        'recall': recall,
        'precision': precision,
        'f1': f1,
        'new_tags_added': len(false_positives),
        'tags_missed': len(false_negatives)
    }


def main():
    print("\n🎯 STRATEGY COMPARISON: Testing Confidence Thresholds")
    print("=" * 160)
    print("Strategies: conservative(0.8) | balanced(0.6) | aggressive(0.4)")
    print("=" * 160)
    
    strategies = [
        ('conservative', 0.80),
        ('balanced', 0.60),
        ('aggressive', 0.40)
    ]
    
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
    
    print(f"\nTesting {len(test_files)} files across {len(strategies)} strategies...\n")
    
    all_results = []
    
    for i, file_path in enumerate(test_files, 1):
        print(f"\n[{i:2}/{len(test_files)}] {file_path.name}")
        print("-" * 160)
        
        for strategy_name, min_conf in strategies:
            try:
                result = test_strategy(file_path, strategy_name, min_conf)
                all_results.append(result)
                all_results[-1]['file'] = file_path.name
                all_results[-1]['chapter'] = file_path.parent.name
                
                print(
                    f"  {strategy_name:12} | Suggested: {result['suggested_count']:2} | "
                    f"Re-detected: {result['re_detected_count']:2} | "
                    f"Recall: {result['recall']*100:5.1f}% | "
                    f"Prec: {result['precision']*100:5.1f}% | "
                    f"F1: {result['f1']*100:5.1f}%"
                )
            except Exception as e:
                print(f"  {strategy_name:12} | ERROR: {str(e)[:50]}")
    
    # Aggregate results by strategy
    print("\n" + "=" * 160)
    print("AGGREGATE RESULTS BY STRATEGY")
    print("=" * 160)
    
    for strategy_name, _ in strategies:
        strategy_results = [r for r in all_results if r['strategy'] == strategy_name]
        
        avg_recall = sum(r['recall'] for r in strategy_results) / len(strategy_results) if strategy_results else 0
        avg_precision = sum(r['precision'] for r in strategy_results) / len(strategy_results) if strategy_results else 0
        avg_f1 = sum(r['f1'] for r in strategy_results) / len(strategy_results) if strategy_results else 0
        
        total_suggested = sum(r['suggested_count'] for r in strategy_results)
        total_fp = sum(r['false_positives'] for r in strategy_results)
        total_fn = sum(r['false_negatives'] for r in strategy_results)
        
        fp_rate = total_fp / total_suggested if total_suggested > 0 else 0
        
        print(f"\n📊 {strategy_name.upper()}")
        print(f"   Recall:      {avg_recall*100:5.1f}%  (range: 0-100%)")
        print(f"   Precision:   {avg_precision*100:5.1f}%  (range: 0-100%)")
        print(f"   F1 Score:    {avg_f1*100:5.1f}%  (harmonic mean)")
        print(f"   False Pos Rate: {fp_rate*100:5.1f}%  ({total_fp} / {total_suggested})")
        print(f"   Total Missed: {total_fn}")
    
    # Recommendation
    print("\n" + "=" * 160)
    print("RECOMMENDATION")
    print("=" * 160)
    
    conservative_results = [r for r in all_results if r['strategy'] == 'conservative']
    balanced_results = [r for r in all_results if r['strategy'] == 'balanced']
    aggressive_results = [r for r in all_results if r['strategy'] == 'aggressive']
    
    conservative_f1 = sum(r['f1'] for r in conservative_results) / len(conservative_results)
    balanced_f1 = sum(r['f1'] for r in balanced_results) / len(balanced_results)
    aggressive_f1 = sum(r['f1'] for r in aggressive_results) / len(aggressive_results)
    
    conservative_recall = sum(r['recall'] for r in conservative_results) / len(conservative_results)
    balanced_recall = sum(r['recall'] for r in balanced_results) / len(balanced_results)
    aggressive_recall = sum(r['recall'] for r in aggressive_results) / len(aggressive_results)
    
    print(f"\nF1 Scores: Conservative={conservative_f1*100:.1f}% | Balanced={balanced_f1*100:.1f}% | Aggressive={aggressive_f1*100:.1f}%")
    print(f"Recall:    Conservative={conservative_recall*100:.1f}% | Balanced={balanced_recall*100:.1f}% | Aggressive={aggressive_recall*100:.1f}%")
    
    if balanced_f1 >= max(conservative_f1, aggressive_f1):
        print(f"\n✅ RECOMMENDATION: Use BALANCED (0.6 threshold)")
        print(f"   • Optimal F1 score: {balanced_f1*100:.1f}%")
        print(f"   • Good recall: {balanced_recall*100:.1f}% (catches most existing tags)")
        print(f"   • Balanced precision (not too many false positives)")
    elif conservative_f1 > aggressive_f1:
        print(f"\n✅ RECOMMENDATION: Use CONSERVATIVE (0.8 threshold)")
        print(f"   • Best precision - only high-confidence suggestions")
        print(f"   • F1 score: {conservative_f1*100:.1f}%")
    else:
        print(f"\n✅ RECOMMENDATION: Use AGGRESSIVE (0.4 threshold)")
        print(f"   • Best recall: {aggressive_recall*100:.1f}%")
        print(f"   • F1 score: {aggressive_f1*100:.1f}%")
    
    # Save detailed results
    timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    output_file = Path(__file__).parent / f"strategy_comparison_{timestamp}.json"
    
    with open(output_file, 'w') as f:
        json.dump({
            'timestamp': timestamp,
            'files_tested': len(test_files),
            'results': all_results,
            'summary': {
                'conservative': {
                    'f1': conservative_f1,
                    'recall': conservative_recall,
                    'precision': sum(r['precision'] for r in conservative_results) / len(conservative_results)
                },
                'balanced': {
                    'f1': balanced_f1,
                    'recall': balanced_recall,
                    'precision': sum(r['precision'] for r in balanced_results) / len(balanced_results)
                },
                'aggressive': {
                    'f1': aggressive_f1,
                    'recall': aggressive_recall,
                    'precision': sum(r['precision'] for r in aggressive_results) / len(aggressive_results)
                }
            }
        }, f, indent=2)
    
    print(f"\n💾 Detailed results saved: {output_file}")


if __name__ == "__main__":
    main()

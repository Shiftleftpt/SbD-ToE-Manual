#!/usr/bin/env python3
"""
4-Way Comparison Test - Existing vs Human(RAG) vs Robot(Standard)
Runs in RAG environment to leverage all dependencies
"""

import json
from pathlib import Path
from typing import Dict, List
from datetime import datetime
import sys

# Ensure we're in right directory for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "tag-normalization"))

from manual_rag.tagging import AutoTagger, FileTagUpdater
from rag_core.config import MANUAL_ROOT

# Import standard engine
try:
    from tag_system.core.canonical_tags import CanonicalTagsManager
    from tag_system.recommenders.recommendation_engine import RecommendationEngine
    HAS_STANDARD = True
except ImportError:
    print("⚠️  Standard engine not available, RAG-only comparison")
    HAS_STANDARD = False


def run_comparison(file_path: Path, existing_tags: List[str]) -> Dict:
    """Run 4-way comparison on a single file"""
    
    # Initialize
    tagger = AutoTagger()
    
    # Read file
    frontmatter, content = FileTagUpdater.read_frontmatter(file_path)
    title = frontmatter.get('title', file_path.stem)
    
    # Get RAG/Human suggestions
    try:
        relative_path_str = str(file_path.relative_to(MANUAL_ROOT.parent))
        human_suggestions = tagger.suggest_tags(
            relative_path_str,
            content,
            title,
            existing_tags,
            min_confidence=0.35
        )
        
        human_high = [s for s in human_suggestions if s.confidence >= 0.70]
        human_med = [s for s in human_suggestions if 0.50 <= s.confidence < 0.70]
        
        human_result = {
            'high_confidence': [
                {'tag': s.tag, 'confidence': s.confidence, 'source': s.source}
                for s in human_high
            ],
            'medium_confidence': [
                {'tag': s.tag, 'confidence': s.confidence, 'source': s.source}
                for s in human_med
            ],
            'count': len(human_high),
            'error': None
        }
    except Exception as e:
        human_result = {
            'high_confidence': [],
            'medium_confidence': [],
            'count': 0,
            'error': str(e)
        }
    
    # Get Robot/Standard suggestions (if available)
    if HAS_STANDARD:
        try:
            canonical = CanonicalTagsManager("canonical-tags.yml")
            rec_engine = RecommendationEngine(canonical)
            recommendations = rec_engine.recommend_tags(
                str(file_path),
                existing_tags=existing_tags,
                min_confidence=0.60
            )
            
            robot_high = [r for r in recommendations if r.confidence >= 0.70]
            robot_med = [r for r in recommendations if 0.50 <= r.confidence < 0.70]
            
            robot_result = {
                'high_confidence': [
                    {'tag': r.tag, 'confidence': r.confidence}
                    for r in robot_high
                ],
                'medium_confidence': [
                    {'tag': r.tag, 'confidence': r.confidence}
                    for r in robot_med
                ],
                'count': len(robot_high),
                'error': None
            }
        except Exception as e:
            robot_result = {
                'high_confidence': [],
                'medium_confidence': [],
                'count': 0,
                'error': str(e)
            }
    else:
        robot_result = {
            'high_confidence': [],
            'medium_confidence': [],
            'count': 0,
            'error': 'Standard engine not available'
        }
    
    # Calculate metrics
    existing_set = set(existing_tags)
    human_set = set(s['tag'] for s in human_result['high_confidence'])
    robot_set = set(s['tag'] for s in robot_result['high_confidence'])
    
    human_recall = len(human_set & existing_set) / len(existing_set) if existing_set else 0
    robot_recall = len(robot_set & existing_set) / len(existing_set) if existing_set else 0
    
    agreement = len(human_set & robot_set) / max(len(human_set | robot_set), 1)
    
    return {
        'file': str(file_path.relative_to(MANUAL_ROOT.parent.parent)),
        'filename': file_path.name,
        'size': file_path.stat().st_size,
        
        'existing_tags': existing_tags,
        'existing_count': len(existing_tags),
        
        'human': human_result,
        'robot': robot_result,
        
        'metrics': {
            'human_recall': round(human_recall, 3),
            'robot_recall': round(robot_recall, 3),
            'human_robot_agreement': round(agreement, 3),
            'human_edge': round(human_recall - robot_recall, 3),
            'human_new': list(human_set - existing_set),
            'robot_new': list(robot_set - existing_set),
            'both_new': list((human_set & robot_set) - existing_set)
        }
    }


def format_comparison(result: Dict) -> str:
    """Format comparison result"""
    lines = []
    
    lines.append("=" * 130)
    lines.append(f"📄 {result['filename']}")
    lines.append(f"   Path: .../{result['file'].split('/')[-2]}/{result['file'].split('/')[-1]}")
    lines.append("=" * 130)
    lines.append("")
    
    # Existing
    lines.append("📋 EXISTING TAGS:")
    for i, tag in enumerate(result['existing_tags'][:10], 1):
        lines.append(f"   {i:2}. {tag}")
    if len(result['existing_tags']) > 10:
        lines.append(f"   ... +{len(result['existing_tags'])-10} more")
    lines.append("")
    
    # Human/RAG
    h = result['human']
    lines.append("👤 HUMAN/RAG SUGGESTIONS:")
    if h['error']:
        lines.append(f"   ❌ {h['error']}")
    else:
        lines.append(f"   High confidence: {h['count']}")
        for item in h['high_confidence'][:5]:
            lines.append(f"      {item['tag']:<25} {item['confidence']*100:5.1f}% [{item['source']}]")
    lines.append("")
    
    # Robot/Standard
    r = result['robot']
    lines.append("🤖 ROBOT/STANDARD RECOMMENDATIONS:")
    if r['error']:
        lines.append(f"   ❌ {r['error']}")
    else:
        lines.append(f"   High confidence: {r['count']}")
        for item in r['high_confidence'][:5]:
            lines.append(f"      {item['tag']:<25} {item['confidence']*100:5.1f}%")
    lines.append("")
    
    # Metrics
    m = result['metrics']
    lines.append("📊 METRICS:")
    lines.append(f"   Recall (vs existing):")
    lines.append(f"      Human:  {m['human_recall']*100:5.1f}%")
    lines.append(f"      Robot:  {m['robot_recall']*100:5.1f}%")
    lines.append(f"      Edge:   {m['human_edge']*100:+6.1f}%")
    lines.append(f"")
    lines.append(f"   Agreement: {m['human_robot_agreement']*100:5.1f}%")
    
    if m['both_new']:
        lines.append(f"   Both suggest: {', '.join(m['both_new'])}")
    
    lines.append("")
    
    return "\n".join(lines)


def main():
    print("\n🔍 4-WAY TAG COMPARISON TEST")
    print("=" * 130)
    print("Comparing: Existing Tags vs Human(RAG) vs Robot(Standard Engine)")
    print("=" * 130)
    print("")
    
    # Find diverse test files
    base_path = MANUAL_ROOT.parent
    all_files = list(base_path.rglob("*.md"))
    all_files = [f for f in all_files if not str(f).endswith('.2review')]
    
    # Select files with existing tags
    test_files = []
    categories = set()
    
    for md_file in all_files:
        try:
            with open(md_file, 'r') as f:
                content = f.read()
                if 'tags: [' in content or "tags: '" in content:
                    # Get category
                    parts = md_file.parts
                    chapter = next((p for p in reversed(parts) if p != md_file.name), 'other')
                    
                    if chapter not in categories and len(test_files) < 5:
                        test_files.append(md_file)
                        categories.add(chapter)
        except:
            pass
    
    if not test_files:
        print("❌ No test files found!")
        sys.exit(1)
    
    print(f"Found {len(test_files)} diverse test files\n")
    
    # Run comparisons
    results = []
    for i, file_path in enumerate(test_files, 1):
        print(f"[{i}/{len(test_files)}] {file_path.name}...", end=" ", flush=True)
        try:
            frontmatter, _ = FileTagUpdater.read_frontmatter(file_path)
            existing = frontmatter.get('tags', [])
            
            if not existing:
                print("(no tags, skip)")
                continue
            
            result = run_comparison(file_path, existing)
            results.append(result)
            print(f"✓")
        except Exception as e:
            print(f"✗ ({e})")
    
    # Print all comparisons
    print("\n" + "=" * 130)
    print("DETAILED COMPARISONS")
    print("=" * 130 + "\n")
    
    for result in results:
        print(format_comparison(result))
    
    # Summary
    if results:
        avg_human_recall = sum(r['metrics']['human_recall'] for r in results) / len(results)
        avg_robot_recall = sum(r['metrics']['robot_recall'] for r in results) / len(results)
        avg_agreement = sum(r['metrics']['human_robot_agreement'] for r in results) / len(results)
        
        print("=" * 130)
        print("SUMMARY")
        print("=" * 130)
        print(f"Files compared:         {len(results)}")
        print(f"Avg Human recall:       {avg_human_recall*100:.1f}%")
        print(f"Avg Robot recall:       {avg_robot_recall*100:.1f}%")
        print(f"Human advantage:        {(avg_human_recall-avg_robot_recall)*100:+.1f}%")
        print(f"Avg H↔R agreement:      {avg_agreement*100:.1f}%")
    
    # Save results
    output_file = Path(__file__).parent / f"results/comparison_{datetime.now().isoformat().replace(':', '-')}.json"
    output_file.parent.mkdir(exist_ok=True)
    
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Results saved: {output_file}")


if __name__ == "__main__":
    main()

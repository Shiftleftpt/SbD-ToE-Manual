#!/usr/bin/env python3
"""
Enhanced recall quality test - Four-way comparison:
1. Existing tags (baseline)
2. Human/RAG suggestions (our new AutoTagger)
3. Robot/Standard engine recommendations
4. Comparison metrics (agreement, delta, quality)
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set

# Add paths
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))
sys.path.insert(0, str(parent_dir.parent))  # Add tag-normalization itself

# Old system (recommendation engine)
from tag_system.core.canonical_tags import CanonicalTagsManager
from tag_system.validators.validation_engine import ValidationEngine
from tag_system.recommenders.recommendation_engine import RecommendationEngine

# New system (RAG-based AutoTagger)
manual_rag_dir = Path(__file__).parent.parent.parent.parent / "manual-rag"
sys.path.insert(0, str(manual_rag_dir))

try:
    from manual_rag.tagging import AutoTagger, FileTagUpdater
    from manual_rag.config import MANUAL_ROOT
    HAS_RAG = True
except ImportError as e:
    print(f"⚠️  Warning: Could not import RAG system: {e}")
    print("   Continuing with standard engine only...")
    HAS_RAG = False
    AutoTagger = None
    FileTagUpdater = None
    MANUAL_ROOT = None


def get_human_suggestions(file_path: Path, existing_tags: List[str]) -> Dict:
    """Get RAG-based suggestions from AutoTagger (Human perspective)"""
    if not HAS_RAG or AutoTagger is None:
        return {
            'high_confidence': [],
            'medium_confidence': [],
            'total_suggestions': 0,
            'error': 'RAG system not available'
        }
    
    try:
        tagger = AutoTagger()
        frontmatter, content = FileTagUpdater.read_frontmatter(file_path)
        title = frontmatter.get('title', file_path.stem)
        
        # Get suggestions with details
        suggestions = tagger.suggest_tags(
            file_path.relative_to(MANUAL_ROOT).as_posix() if file_path.parent.name != 'sbd-toe' else str(file_path.relative_to(MANUAL_ROOT)),
            content,
            title,
            existing_tags,
            min_confidence=0.35
        )
        
        # High confidence (70%+)
        high_conf = [s for s in suggestions if s.confidence >= 0.70]
        # Medium confidence (50-70%)
        med_conf = [s for s in suggestions if 0.50 <= s.confidence < 0.70]
        
        return {
            'high_confidence': [
                {'tag': s.tag, 'confidence': s.confidence, 'source': s.source}
                for s in high_conf
            ],
            'medium_confidence': [
                {'tag': s.tag, 'confidence': s.confidence, 'source': s.source}
                for s in med_conf
            ],
            'total_suggestions': len(suggestions),
            'error': None
        }
    except Exception as e:
        return {
            'high_confidence': [],
            'medium_confidence': [],
            'total_suggestions': 0,
            'error': str(e)
        }


def get_robot_suggestions(file_path: Path, validator, rec_engine, existing_tags: List[str]) -> Dict:
    """Get suggestions from standard recommendation engine (Robot perspective)"""
    try:
        recommendations = rec_engine.recommend_tags(str(file_path), existing_tags=existing_tags, min_confidence=0.60)
        
        # High confidence (70%+)
        high_conf = [r for r in recommendations if r.confidence >= 0.70]
        # Medium confidence (50-70%)
        med_conf = [r for r in recommendations if 0.50 <= r.confidence < 0.70]
        
        return {
            'high_confidence': [
                {'tag': r.tag, 'confidence': r.confidence, 'reason': r.reason}
                for r in high_conf
            ],
            'medium_confidence': [
                {'tag': r.tag, 'confidence': r.confidence, 'reason': r.reason}
                for r in med_conf
            ],
            'total_suggestions': len(recommendations),
            'error': None
        }
    except Exception as e:
        return {
            'high_confidence': [],
            'medium_confidence': [],
            'total_suggestions': 0,
            'error': str(e)
        }


def analyze_file_comprehensive(file_path: Path, validator, rec_engine, canonical_mgr) -> Dict:
    """Comprehensive four-way analysis"""
    
    # 1. Get existing tags
    validation_result = validator.validate_file(str(file_path))
    existing_tags = validation_result.existing_tags if validation_result.existing_tags else []
    
    # 2. Get Human suggestions (RAG)
    human_sug = get_human_suggestions(file_path, existing_tags)
    
    # 3. Get Robot suggestions (Standard engine)
    robot_sug = get_robot_suggestions(file_path, validator, rec_engine, existing_tags)
    
    # Convert to sets for comparison
    existing_set = set(existing_tags)
    human_high_set = set(s['tag'] for s in human_sug['high_confidence'])
    robot_high_set = set(s['tag'] for s in robot_sug['high_confidence'])
    
    # 4. Calculate metrics
    human_recall = len(human_high_set & existing_set) / len(existing_set) if existing_set else 0
    robot_recall = len(robot_high_set & existing_set) / len(existing_set) if existing_set else 0
    
    # Agreement metrics
    human_robot_agreement = len(human_high_set & robot_high_set) / max(len(human_high_set | robot_high_set), 1)
    human_existing_agreement = len(human_high_set & existing_set) / max(len(human_high_set | existing_set), 1)
    robot_existing_agreement = len(robot_high_set & existing_set) / max(len(robot_high_set | existing_set), 1)
    
    # New suggestions (not in existing, high confidence)
    human_new = human_high_set - existing_set
    robot_new = robot_high_set - existing_set
    both_suggest = human_new & robot_new  # Both agree on new tags
    
    return {
        'file': str(file_path.relative_to(file_path.parents[3]) if file_path.parents[3].name == 'sbd-toe' else file_path),
        'filename': file_path.name,
        'size': file_path.stat().st_size,
        
        # Perspective 1: Existing
        'existing': {
            'tags': existing_tags,
            'count': len(existing_tags)
        },
        
        # Perspective 2: Human (RAG)
        'human': {
            'high_confidence': human_sug['high_confidence'],
            'high_count': len(human_sug['high_confidence']),
            'medium_confidence': human_sug['medium_confidence'],
            'medium_count': len(human_sug['medium_confidence']),
            'new_suggestions': list(human_new),
            'error': human_sug['error']
        },
        
        # Perspective 3: Robot (Standard)
        'robot': {
            'high_confidence': robot_sug['high_confidence'],
            'high_count': len(robot_sug['high_confidence']),
            'medium_confidence': robot_sug['medium_confidence'],
            'medium_count': len(robot_sug['medium_confidence']),
            'new_suggestions': list(robot_new),
            'error': robot_sug['error']
        },
        
        # Metrics
        'metrics': {
            'human_recall': round(human_recall, 3),
            'robot_recall': round(robot_recall, 3),
            'human_robot_agreement': round(human_robot_agreement, 3),
            'human_existing_agreement': round(human_existing_agreement, 3),
            'robot_existing_agreement': round(robot_existing_agreement, 3),
            'both_suggest_new': list(both_suggest),
            'delta_human_vs_robot': len(human_high_set ^ robot_high_set)
        }
    }


def format_report(analysis: Dict) -> str:
    """Format analysis into readable report"""
    report = []
    
    report.append("="*140)
    report.append(f"📄 {analysis['filename']}")
    report.append(f"   Path: {analysis['file']}")
    report.append(f"   Size: {analysis['size']:,} bytes")
    report.append("="*140)
    report.append("")
    
    # Perspective 1: Existing tags
    report.append("┌─ PERSPECTIVE 1: 📋 EXISTING TAGS (Baseline)")
    report.append("├──────────────────────────────────────────────────────────────────────────────────────")
    existing = analysis['existing']
    if existing['tags']:
        for i, tag in enumerate(existing['tags'], 1):
            report.append(f"│  {i:2d}. {tag}")
    else:
        report.append("│  [No tags]")
    report.append(f"│  Total: {existing['count']}")
    report.append("│")
    
    # Perspective 2: Human (RAG)
    report.append("├─ PERSPECTIVE 2: 👤 HUMAN/RAG SUGGESTIONS")
    report.append("├──────────────────────────────────────────────────────────────────────────────────────")
    human = analysis['human']
    
    if human['error']:
        report.append(f"│  ❌ Error: {human['error']}")
    else:
        if human['high_confidence']:
            report.append(f"│  ✓ High confidence (70%+): {human['high_count']}")
            for item in human['high_confidence'][:5]:
                report.append(f"│    • {item['tag']:<25} {item['confidence']*100:5.1f}%  [{item['source']}]")
            if human['high_count'] > 5:
                report.append(f"│    ... and {human['high_count']-5} more")
        
        if human['medium_confidence']:
            report.append(f"│  ◐ Medium confidence (50-70%): {human['medium_count']}")
            for item in human['medium_confidence'][:3]:
                report.append(f"│    • {item['tag']:<25} {item['confidence']*100:5.1f}%  [{item['source']}]")
        
        if human['new_suggestions']:
            report.append(f"│  💡 New suggestions: {len(human['new_suggestions'])}")
            for tag in human['new_suggestions'][:5]:
                report.append(f"│    + {tag}")
    report.append("│")
    
    # Perspective 3: Robot (Standard)
    report.append("├─ PERSPECTIVE 3: 🤖 ROBOT/STANDARD RECOMMENDATIONS")
    report.append("├──────────────────────────────────────────────────────────────────────────────────────")
    robot = analysis['robot']
    
    if robot['error']:
        report.append(f"│  ❌ Error: {robot['error']}")
    else:
        if robot['high_confidence']:
            report.append(f"│  ✓ High confidence (70%+): {robot['high_count']}")
            for item in robot['high_confidence'][:5]:
                report.append(f"│    • {item['tag']:<25} {item['confidence']*100:5.1f}%")
            if robot['high_count'] > 5:
                report.append(f"│    ... and {robot['high_count']-5} more")
        
        if robot['medium_confidence']:
            report.append(f"│  ◐ Medium confidence (50-70%): {robot['medium_count']}")
            for item in robot['medium_confidence'][:3]:
                report.append(f"│    • {item['tag']:<25} {item['confidence']*100:5.1f}%")
        
        if robot['new_suggestions']:
            report.append(f"│  💡 New suggestions: {len(robot['new_suggestions'])}")
            for tag in robot['new_suggestions'][:5]:
                report.append(f"│    + {tag}")
    report.append("│")
    
    # Metrics & Comparison
    report.append("├─ PERSPECTIVE 4: 📊 COMPARISON METRICS")
    report.append("├──────────────────────────────────────────────────────────────────────────────────────")
    metrics = analysis['metrics']
    
    report.append(f"│  Recall (vs existing):")
    report.append(f"│    • Human:  {metrics['human_recall']*100:5.1f}%")
    report.append(f"│    • Robot:  {metrics['robot_recall']*100:5.1f}%")
    report.append(f"│    • Delta:  {(metrics['human_recall']-metrics['robot_recall'])*100:+6.1f}%")
    
    report.append(f"│")
    report.append(f"│  Agreement with existing:")
    report.append(f"│    • Human:  {metrics['human_existing_agreement']*100:5.1f}%")
    report.append(f"│    • Robot:  {metrics['robot_existing_agreement']*100:5.1f}%")
    
    report.append(f"│")
    report.append(f"│  Human ↔ Robot agreement: {metrics['human_robot_agreement']*100:5.1f}%")
    
    if metrics['both_suggest_new']:
        report.append(f"│  Both suggest new tags: {metrics['both_suggest_new']}")
    
    report.append("└──────────────────────────────────────────────────────────────────────────────────────")
    report.append("")
    
    return "\n".join(report)


def main():
    print("\n🔍 Enhanced Recall Quality Test (4-Way Comparison)")
    print("="*140)
    
    # Initialize systems
    canonical_mgr = CanonicalTagsManager("canonical-tags.yml")
    validator = ValidationEngine(canonical_mgr)
    rec_engine = RecommendationEngine(canonical_mgr)
    
    # Find test files with tags
    base_path = Path("../../manuals_src/docs/sbd-toe")
    all_md_files = list(base_path.rglob("*.md"))
    all_md_files = [f for f in all_md_files if not str(f).endswith('.2review')]
    
    # Select diverse files
    test_files = []
    categories_covered = set()
    
    for md_file in all_md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'tags: [' in content or "tags: '" in content:
                    # Get chapter (folder name)
                    parts = md_file.parts
                    chapter = parts[-2] if len(parts) >= 2 else 'other'
                    
                    if chapter not in categories_covered and len(test_files) < 6:
                        test_files.append(md_file)
                        categories_covered.add(chapter)
        except:
            pass
    
    if not test_files:
        print("❌ No test files found!")
        sys.exit(1)
    
    print(f"📁 Found {len(test_files)} diverse test files\n")
    
    # Analyze all
    results = []
    for i, file_path in enumerate(test_files, 1):
        print(f"[{i}/{len(test_files)}] Analyzing {file_path.name}...", end=" ", flush=True)
        try:
            result = analyze_file_comprehensive(file_path, validator, rec_engine, canonical_mgr)
            results.append(result)
            print(f"✓")
        except Exception as e:
            print(f"✗ ({e})")
    
    # Print all reports
    print("\n\n" + "="*140)
    print("📊 DETAILED ANALYSIS RESULTS")
    print("="*140 + "\n")
    
    for result in results:
        print(format_report(result))
    
    # Summary statistics
    print("="*140)
    print("📈 AGGREGATE STATISTICS")
    print("="*140)
    
    if results:
        avg_human_recall = sum(r['metrics']['human_recall'] for r in results) / len(results)
        avg_robot_recall = sum(r['metrics']['robot_recall'] for r in results) / len(results)
        avg_agreement = sum(r['metrics']['human_robot_agreement'] for r in results) / len(results)
        
        print(f"\nFiles analyzed:           {len(results)}")
        print(f"Average recall (Human):   {avg_human_recall*100:.1f}%")
        print(f"Average recall (Robot):   {avg_robot_recall*100:.1f}%")
        print(f"Average H↔R agreement:    {avg_agreement*100:.1f}%")
        print(f"Human advantage:          {(avg_human_recall-avg_robot_recall)*100:+.1f}%")
    
    # Save results
    output_dir = Path(__file__).parent / "results"
    output_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().isoformat().replace(':', '-')
    json_file = output_dir / f"four_way_comparison_{timestamp}.json"
    
    with open(json_file, 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Results saved to: {json_file}")


if __name__ == "__main__":
    main()

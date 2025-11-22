#!/usr/bin/env python3
"""
Multi-file recall quality test with three-way analysis (Human vs Existing vs Robot)
Runs analysis on 4 diverse documents and saves results to disk for reproducibility
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime

# Add tag_system to path
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))
os.chdir(parent_dir)

from tag_system.core.canonical_tags import CanonicalTagsManager
from tag_system.validators.validation_engine import ValidationEngine
from tag_system.recommenders.recommendation_engine import RecommendationEngine


def get_file_content(filepath):
    """Load markdown file content"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"[ERROR: Could not read file - {e}]"


def analyze_file(filepath, validator, rec_engine, canonical_mgr):
    """Analyze single file with all three perspectives"""
    
    content = get_file_content(filepath)
    if not content or "[ERROR" in content:
        return None
    
    # Extract existing tags
    validation_result = validator.validate_file(str(filepath))
    existing_tags = validation_result.existing_tags if validation_result.existing_tags else []
    
    # Get robot recommendations - pass filepath (not content)
    recommendations = rec_engine.recommend_tags(str(filepath), existing_tags=existing_tags, min_confidence=0.60)
    
    # Find re-detected tags (high confidence)
    re_detected = []
    missed_tags = []
    for tag in existing_tags:
        tag_found = False
        for rec in recommendations:
            if rec.tag == tag and rec.confidence >= 0.70:
                re_detected.append({
                    'tag': tag,
                    'confidence': rec.confidence,
                    'reason': rec.reason
                })
                tag_found = True
                break
        if not tag_found:
            missed_tags.append(tag)
    
    # New suggestions (not already in file)
    new_suggestions = []
    for rec in recommendations:
        if rec.tag not in existing_tags and rec.confidence >= 0.70:
            new_suggestions.append({
                'tag': rec.tag,
                'confidence': rec.confidence,
                'reason': rec.reason
            })
    
    # Calculate recall
    recall = len(re_detected) / len(existing_tags) if existing_tags else 0
    
    return {
        'filepath': str(filepath),
        'filename': filepath.name,
        'content_length': len(content),
        'existing_tags': existing_tags,
        'existing_count': len(existing_tags),
        're_detected': re_detected,
        're_detected_count': len(re_detected),
        'missed_tags': missed_tags,
        'missed_count': len(missed_tags),
        'recall_percentage': round(recall * 100, 1),
        'new_suggestions': new_suggestions,
        'new_suggestions_count': len(new_suggestions),
        'recommendation_action': {
            'keep': existing_tags[:len(existing_tags) - len(missed_tags)],
            'review': missed_tags,
            'add': [s['tag'] for s in new_suggestions],
            'total_optimized': len(existing_tags) - len(missed_tags) + len(new_suggestions)
        }
    }


def format_analysis_report(analysis_data):
    """Format analysis into readable report"""
    
    report = []
    report.append("="*120)
    report.append(f"📄 FILE: {analysis_data['filename']}")
    report.append(f"   Path: {analysis_data['filepath']}")
    report.append(f"   Size: {analysis_data['content_length']:,} chars")
    report.append("="*120)
    report.append("")
    
    # Perspective 1: Existing tags
    report.append("PERSPECTIVE 1: 📋 EXISTING TAGS (Currently in file)")
    report.append("-" * 120)
    if analysis_data['existing_tags']:
        for i, tag in enumerate(analysis_data['existing_tags'], 1):
            report.append(f"  {i}. {tag}")
    else:
        report.append("  [No tags]")
    report.append("")
    
    # Perspective 2: Robot re-detection
    report.append("PERSPECTIVE 2: 🤖 ROBOT RE-DETECTION (Can AI find existing tags?)")
    report.append("-" * 120)
    report.append(f"Re-detected (70%+ confidence): {analysis_data['re_detected_count']}/{analysis_data['existing_count']}")
    
    if analysis_data['re_detected']:
        for item in analysis_data['re_detected']:
            report.append(f"  ✓ {item['tag']:<20} {item['confidence']*100:.0f}%  [{item['reason']}]")
    
    if analysis_data['missed_tags']:
        report.append("")
        report.append(f"Missed (couldn't re-detect): {analysis_data['missed_count']}")
        for tag in analysis_data['missed_tags']:
            report.append(f"  ✗ {tag}")
    
    report.append(f"\n  RECALL: {analysis_data['recall_percentage']:.1f}%")
    report.append("")
    
    # Perspective 3: New suggestions
    report.append("PERSPECTIVE 3: 💡 NEW SUGGESTIONS (What robot recommends)")
    report.append("-" * 120)
    report.append(f"High-confidence suggestions (70%+): {analysis_data['new_suggestions_count']}")
    
    if analysis_data['new_suggestions']:
        for i, sugg in enumerate(analysis_data['new_suggestions'][:10], 1):  # Top 10
            report.append(f"  {i:2d}. {sugg['tag']:<20} {sugg['confidence']*100:.0f}%")
        if len(analysis_data['new_suggestions']) > 10:
            report.append(f"  ... and {len(analysis_data['new_suggestions']) - 10} more")
    report.append("")
    
    # Action recommendation
    report.append("RECOMMENDED ACTION:")
    report.append("-" * 120)
    action = analysis_data['recommendation_action']
    report.append(f"  KEEP:        {len(action['keep'])} tags (re-detected)")
    report.append(f"  REVIEW:      {len(action['review'])} tags (missed by robot)")
    report.append(f"  ADD:         {len(action['add'])} tags (high confidence)")
    report.append(f"  TOTAL:       {action['total_optimized']} tags (optimized)")
    report.append("")
    
    return "\n".join(report)


def main():
    # Initialize engines
    canonical_mgr = CanonicalTagsManager("canonical-tags.yml")
    validator = ValidationEngine(canonical_mgr)
    rec_engine = RecommendationEngine(canonical_mgr)
    
    # Select 4 diverse test files with existing tags
    base_path = Path("../../manuals_src/docs/sbd-toe")
    
    # Collect all md files and find ones with tags
    all_md_files = list(base_path.rglob("*.md"))
    all_md_files = [f for f in all_md_files if not str(f).endswith('.2review')]
    
    # Find files with tags
    files_with_tags = []
    for md_file in all_md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'tags: [' in content or "tags: '" in content:
                    files_with_tags.append(md_file)
                    if len(files_with_tags) >= 4:
                        break
        except:
            pass
    
    test_files = files_with_tags[:4]
    
    # Verify files exist
    valid_files = [f for f in test_files if f.exists()]
    if not valid_files:
        print("❌ No test files found! Checking available paths...")
        print(f"Base path: {base_path}")
        print(f"Exists: {base_path.exists()}")
        sys.exit(1)
    
    print(f"\n🔍 Running multi-file recall quality test...")
    print(f"📁 Found {len(valid_files)} test files\n")
    
    # Analyze all files
    all_results = []
    all_reports = []
    
    for filepath in valid_files:
        print(f"  Analyzing: {filepath.name}...", end=" ")
        result = analyze_file(filepath, validator, rec_engine, canonical_mgr)
        
        if result:
            all_results.append(result)
            report = format_analysis_report(result)
            all_reports.append(report)
            print(f"✓ ({result['recall_percentage']:.1f}% recall)")
        else:
            print(f"✗ (skipped)")
    
    # Print all reports to console
    print("\n\n" + "="*120)
    print("📊 FULL ANALYSIS RESULTS")
    print("="*120 + "\n")
    
    for report in all_reports:
        print(report)
        print()
    
    # Summary statistics
    total_existing = sum(r['existing_count'] for r in all_results)
    total_re_detected = sum(r['re_detected_count'] for r in all_results)
    total_missed = sum(r['missed_count'] for r in all_results)
    total_suggestions = sum(r['new_suggestions_count'] for r in all_results)
    
    avg_recall = (total_re_detected / total_existing * 100) if total_existing > 0 else 0
    
    print("="*120)
    print("📈 SUMMARY STATISTICS")
    print("="*120)
    print(f"\nFiles analyzed:      {len(all_results)}")
    print(f"Total existing tags: {total_existing}")
    print(f"Re-detected:         {total_re_detected}")
    print(f"Missed:              {total_missed}")
    print(f"Average recall:      {avg_recall:.1f}%")
    print(f"New suggestions:     {total_suggestions}")
    print()
    
    # Save results to JSON
    output_dir = Path(__file__).parent / "results"
    output_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().isoformat().replace(':', '-')
    json_output = output_dir / f"multifile_recall_analysis_{timestamp}.json"
    
    output_data = {
        'timestamp': datetime.now().isoformat(),
        'test_type': 'multifile_recall_quality_test',
        'summary': {
            'files_analyzed': len(all_results),
            'total_existing_tags': total_existing,
            'total_re_detected': total_re_detected,
            'total_missed': total_missed,
            'average_recall_percentage': round(avg_recall, 1),
            'total_new_suggestions': total_suggestions,
        },
        'files': all_results
    }
    
    with open(json_output, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Results saved to: {json_output}")
    
    # Also save text report
    text_output = output_dir / f"multifile_recall_analysis_{timestamp}.txt"
    with open(text_output, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(all_reports))
        f.write("\n\n" + "="*120 + "\n")
        f.write("SUMMARY STATISTICS\n")
        f.write("="*120 + "\n\n")
        f.write(f"Files analyzed:      {len(all_results)}\n")
        f.write(f"Total existing tags: {total_existing}\n")
        f.write(f"Re-detected:         {total_re_detected}\n")
        f.write(f"Missed:              {total_missed}\n")
        f.write(f"Average recall:      {avg_recall:.1f}%\n")
        f.write(f"New suggestions:     {total_suggestions}\n")
    
    print(f"✅ Text report saved to: {text_output}")
    print()


if __name__ == "__main__":
    main()

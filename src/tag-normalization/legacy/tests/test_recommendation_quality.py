#!/usr/bin/env python3
"""
Test: Check if recommendation system re-detects existing tags
This is a quality check - the system should suggest tags that are already in the file
"""

import sys
import os
from pathlib import Path

# Setup paths
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))
os.chdir(parent_dir)

from tag_system.core.canonical_tags import CanonicalTagsManager
from tag_system.validators.validation_engine import ValidationEngine
from tag_system.recommenders.recommendation_engine import RecommendationEngine


def test_recommendation_recall():
    """Test if system can re-detect existing tags"""
    
    print("\n" + "="*80)
    print("🧪 TEST: Recommendation System - Tag Re-detection Quality")
    print("="*80 + "\n")
    
    canonical_mgr = CanonicalTagsManager("canonical-tags.yml")
    validator = ValidationEngine(canonical_mgr)
    recommender = RecommendationEngine(canonical_mgr)
    
    # Find a real file with tags
    docs_path = Path("../../manuals_src/docs/sbd-toe")
    md_files = list(docs_path.rglob("*.md"))
    md_files = [f for f in md_files if not str(f).endswith('.2review')]
    
    test_count = 0
    total_existing = 0
    total_redetected = 0
    total_missed = 0
    
    print("Testing files with existing tags:\n")
    print(f"{'File':<50} {'Existing':<10} {'Re-detected':<12} {'Missed':<10}")
    print(f"{'-'*82}")
    
    for file_path in md_files[:30]:
        # Get existing tags
        result = validator.validate_file(str(file_path))
        existing_tags = set(result.existing_tags) if result.existing_tags else set()
        
        if not existing_tags:
            continue
        
        # Get recommendations (all, not just high confidence)
        recommendations = recommender.recommend_tags(
            str(file_path), 
            min_confidence=0.0,  # All recommendations
            max_recommendations=100
        )
        recommended_tags = set(rec.tag for rec in recommendations)
        
        # Analysis
        redetected = existing_tags & recommended_tags
        missed = existing_tags - recommended_tags
        
        file_name = file_path.name
        if len(file_name) > 45:
            file_name = "..." + file_name[-42:]
        
        print(f"{file_name:<50} {len(existing_tags):<10} {len(redetected):<12} {len(missed):<10}")
        
        if missed:
            print(f"  ⚠️  Missed: {', '.join(list(missed)[:3])}")
        
        test_count += 1
        total_existing += len(existing_tags)
        total_redetected += len(redetected)
        total_missed += len(missed)
    
    print(f"{'-'*82}")
    
    # Summary
    if test_count > 0:
        recall_rate = (total_redetected / total_existing * 100) if total_existing > 0 else 0
        
        print(f"\n📊 SUMMARY:")
        print(f"   Files tested:        {test_count}")
        print(f"   Total existing tags: {total_existing}")
        print(f"   Re-detected tags:    {total_redetected} ({recall_rate:.1f}% recall)")
        print(f"   Missed tags:         {total_missed}")
        
        print(f"\n{'='*80}")
        
        if recall_rate < 50:
            print("❌ PROBLEM: System has LOW recall - not re-detecting existing tags!")
            print("   This suggests recommendations are too generic or not contextual enough.")
            print("   The system should suggest tags that are already present in the file.")
        elif recall_rate < 80:
            print("⚠️  WARNING: System has MODERATE recall - missing some existing tags")
            print("   Could improve contextual analysis")
        else:
            print("✅ GOOD: System successfully re-detects most existing tags")
        
        print(f"{'='*80}\n")
    
    return total_redetected, total_existing, total_missed


def test_specific_file():
    """Test a specific file in detail"""
    
    print("\n" + "="*80)
    print("🔍 DETAILED TEST: Single File Analysis")
    print("="*80 + "\n")
    
    canonical_mgr = CanonicalTagsManager("canonical-tags.yml")
    validator = ValidationEngine(canonical_mgr)
    recommender = RecommendationEngine(canonical_mgr)
    
    # Use a file with multiple tags
    test_file = "../../manuals_src/docs/sbd-toe/002-cross-check-normativo/01-intro.md"
    
    if not Path(test_file).exists():
        print(f"❌ Test file not found: {test_file}")
        return
    
    result = validator.validate_file(test_file)
    existing_tags = result.existing_tags
    
    print(f"📄 File: {test_file}")
    print(f"\n✅ Existing tags ({len(existing_tags)}):")
    for tag in existing_tags:
        print(f"   • {tag}")
    
    # Get all recommendations
    all_recommendations = recommender.recommend_tags(
        test_file,
        min_confidence=0.0,
        max_recommendations=200
    )
    
    print(f"\n💡 Recommendations (all, sorted by confidence):\n")
    print(f"{'Tag':<25} {'Confidence':<12} {'Already Has':<12} {'Reason'}")
    print(f"{'-'*78}")
    
    # Sort by confidence
    all_recommendations.sort(key=lambda x: x.confidence, reverse=True)
    
    existing_set = set(existing_tags)
    redetected_shown = False
    new_shown = False
    
    for rec in all_recommendations[:40]:
        already_has = rec.tag in existing_set
        
        if already_has and not redetected_shown:
            print(f"\n--- RE-DETECTED TAGS ---")
            redetected_shown = True
        
        if not already_has and new_shown is False:
            print(f"\n--- NEW RECOMMENDATIONS ---")
            new_shown = True
        
        has_str = "✓ YES" if already_has else "  -"
        conf_str = f"{rec.confidence:.1%}"
        reason = rec.reason[:50]
        
        print(f"{rec.tag:<25} {conf_str:<12} {has_str:<12} {reason}")
    
    # Count re-detections
    redetected = sum(1 for rec in all_recommendations if rec.tag in existing_set)
    print(f"\n{'-'*78}")
    print(f"Total re-detected: {redetected}/{len(existing_tags)}")


if __name__ == "__main__":
    test_recommendation_recall()
    test_specific_file()

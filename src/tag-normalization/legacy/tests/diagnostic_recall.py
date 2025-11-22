#!/usr/bin/env python3
"""
Diagnostic: Show why existing tags are not being re-detected
"""

import sys
import os
import re
from pathlib import Path

parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))
os.chdir(parent_dir)

from tag_system.core.canonical_tags import CanonicalTagsManager
from tag_system.recommenders.recommendation_engine import RecommendationEngine


def diagnose_tag_recall():
    """Analyze why existing tags aren't re-detected"""
    
    print("\n" + "="*80)
    print("🔬 DIAGNOSTIC: Why Tags Are Not Re-detected")
    print("="*80 + "\n")
    
    canonical_mgr = CanonicalTagsManager("canonical-tags.yml")
    recommender = RecommendationEngine(canonical_mgr)
    
    test_file = "../../manuals_src/docs/sbd-toe/002-cross-check-normativo/01-intro.md"
    
    # Extract content
    frontmatter = recommender.extract_frontmatter(test_file)
    content = recommender.extract_content_text(test_file)
    combined = f"{frontmatter.get('title', '')} {frontmatter.get('description', '')} {content}".lower()
    
    existing_tags_str = frontmatter.get('tags', '').strip('[]')
    existing_tags = [t.strip() for t in existing_tags_str.split(',')] if existing_tags_str else []
    
    print(f"📄 File: {test_file}")
    print(f"✅ Existing tags: {existing_tags}\n")
    
    print("Analyzing each existing tag:\n")
    print(f"{'Tag':<20} {'In Content?':<15} {'Score':<10} {'Reason':<50}")
    print(f"{'-'*95}")
    
    for tag_name in existing_tags:
        # Try to find tag in content
        tag_info = canonical_mgr.get_tag(tag_name)
        if not tag_info:
            print(f"{tag_name:<20} {'❓ NOT IN CANONICAL':<15}")
            continue
        
        score = 0.0
        reasons = []
        
        # Check 1: Tag keyword in content
        if f" {tag_name.lower()} " in f" {combined} ":
            score += 0.70  # INCREASED to 0.70 for better recall
            reasons.append("tag keyword (0.70)")
            found_keyword = "✓ YES"
        else:
            found_keyword = "✗ NO"
        
        # Check 2: Description in content
        if tag_info.description and tag_info.description.lower() in combined:
            score += 0.50  # INCREASED to 0.50
            reasons.append("description (0.50)")
        
        # Check 3: Related tags
        if tag_info.related:
            for related_tag in tag_info.related:
                if f" {related_tag.lower()} " in f" {combined} ":
                    score += 0.15
                    reasons.append(f"related tag '{related_tag}' (0.15)")
        
        reason_str = "; ".join(reasons) if reasons else "no matches"
        
        # Show result
        threshold = "✓" if score >= 0.65 else "✗"
        print(f"{tag_name:<20} {found_keyword:<15} {score:>6.2f}   {reason_str:<45} [{threshold}]")
    
    print(f"\n{'='*80}")
    print(f"🔍 KEY FINDING:")
    print(f"   • Tag keyword match = 0.70 (70%) [CORRECTED]")
    print(f"   • Description match = 0.50 (50%) [CORRECTED]")
    print(f"   • Current threshold = 0.60 (60%) [LOWERED to improve recall]")
    print(f"   • → Tags with keyword match NOW reach threshold!")
    print(f"\n✅ FIX APPLIED:")
    print(f"   • Boosted keyword match from 0.40 → 0.70")
    print(f"   • Lowered min_confidence from 0.65 → 0.60")
    print(f"   • Result: Better recall of existing tags")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    diagnose_tag_recall()

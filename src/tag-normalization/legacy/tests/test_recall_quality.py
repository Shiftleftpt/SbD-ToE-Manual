#!/usr/bin/env python3
"""
Quality Test: If file didn't have its current tags, would the system suggest them?
This tests the "recall" - can the system detect tags from content analysis alone?
"""

import sys
import os
from pathlib import Path

parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))
os.chdir(parent_dir)

from tag_system.core.canonical_tags import CanonicalTagsManager
from tag_system.validators.validation_engine import ValidationEngine
from tag_system.recommenders.recommendation_engine import RecommendationEngine


def test_recall_quality():
    """Test if recommendations would re-detect existing tags if they weren't present"""
    
    print("\n" + "="*90)
    print("🧪 QUALITY TEST: Would System Re-detect Existing Tags?")
    print("="*90 + "\n")
    
    canonical_mgr = CanonicalTagsManager("canonical-tags.yml")
    validator = ValidationEngine(canonical_mgr)
    recommender = RecommendationEngine(canonical_mgr)
    
    docs_path = Path("../../manuals_src/docs/sbd-toe")
    md_files = list(docs_path.rglob("*.md"))
    md_files = [f for f in md_files if not str(f).endswith('.2review')]
    
    print("METHOD: Simulate 'what if tags weren't there' by manually checking scores\n")
    
    total_existing = 0
    total_detectable = 0
    total_undetectable = 0
    
    print(f"{'File':<45} {'Tags':<8} {'Detectable':<12} {'Undetectable':<12}")
    print(f"{'-'*90}")
    
    for file_path in md_files[:25]:
        result = validator.validate_file(str(file_path))
        existing_tags = result.existing_tags if result.existing_tags else []
        
        if not existing_tags:
            continue
        
        # Get raw content and analyze manually
        frontmatter = recommender.extract_frontmatter(str(file_path))
        content = recommender.extract_content_text(str(file_path))
        combined = f"{frontmatter.get('title', '')} {frontmatter.get('description', '')} {content}".lower()
        
        detectable = []
        undetectable = []
        
        for tag_name in existing_tags:
            tag_info = canonical_mgr.get_tag(tag_name)
            if not tag_info:
                undetectable.append(tag_name)
                continue
            
            # Check if tag name appears in content (this would be scored as 0.70)
            if f" {tag_name.lower()} " in f" {combined} ":
                detectable.append(tag_name)
            # Check if description matches (this would be scored as 0.50)
            elif tag_info.description and tag_info.description.lower() in combined:
                detectable.append(tag_name)
            else:
                undetectable.append(tag_name)
        
        if len(existing_tags) > 0:
            file_name = file_path.name
            if len(file_name) > 40:
                file_name = "..." + file_name[-37:]
            
            print(f"{file_name:<45} {len(existing_tags):<8} {len(detectable):<12} {len(undetectable):<12}")
            
            total_existing += len(existing_tags)
            total_detectable += len(detectable)
            total_undetectable += len(undetectable)
    
    print(f"{'-'*90}")
    
    # Summary
    if total_existing > 0:
        recall_pct = (total_detectable / total_existing) * 100
        print(f"\n📊 RECALL ANALYSIS:")
        print(f"   Total existing tags tested: {total_existing}")
        print(f"   Detectable from content:    {total_detectable} ({recall_pct:.1f}% ✓)")
        print(f"   Not in content:             {total_undetectable} ({100-recall_pct:.1f}% ✗)")
        
        print(f"\n{'='*90}")
        if recall_pct >= 80:
            print(f"✅ GOOD: System can re-detect {recall_pct:.0f}% of existing tags")
        elif recall_pct >= 60:
            print(f"⚠️  MODERATE: System can re-detect {recall_pct:.0f}% of existing tags")
        else:
            print(f"❌ POOR: System can only re-detect {recall_pct:.0f}% of existing tags")
            print(f"   This means many tags exist in files but not their name/description")
        print(f"{'='*90}\n")
        
        return total_detectable, total_existing


if __name__ == "__main__":
    test_recall_quality()

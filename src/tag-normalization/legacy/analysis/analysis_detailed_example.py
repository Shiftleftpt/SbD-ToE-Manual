#!/usr/bin/env python3
"""
Detailed analysis: Human vs Robot tag comparison
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


def detailed_analysis():
    """Analyze a specific file in detail"""
    
    print("\n" + "="*100)
    print("🔬 DETAILED ANALYSIS: Human vs Robot Tag Recommendations")
    print("="*100 + "\n")
    
    # Test file
    test_file = "/Volumes/G-DRIVE/Shared/Manual-SbD-ToE/SbD-ToE-Manual/manuals_src/docs/sbd-toe/002-cross-check-normativo/exemplo-playbook/01-exemplo-toolchain-options.md"
    
    print(f"📄 Ficheiro: {test_file}\n")
    
    # Read full content
    with open(test_file, 'r', encoding='utf-8') as f:
        full_content = f.read()
    
    # Initialize systems
    canonical_mgr = CanonicalTagsManager("canonical-tags.yml")
    validator = ValidationEngine(canonical_mgr)
    recommender = RecommendationEngine(canonical_mgr)
    
    # Get frontmatter
    frontmatter = recommender.extract_frontmatter(test_file)
    
    print(f"📋 FRONTMATTER INFO:")
    print(f"   Title: {frontmatter.get('title', 'N/A')}")
    print(f"   Description: {frontmatter.get('description', 'N/A')}")
    
    # Get existing tags
    result = validator.validate_file(test_file)
    existing_tags = result.existing_tags if result.existing_tags else []
    
    print(f"\n{'='*100}")
    print("1️⃣  EXISTING TAGS (Current)")
    print(f"{'='*100}\n")
    print(f"Tags in file ({len(existing_tags)}):")
    for i, tag in enumerate(existing_tags, 1):
        tag_info = canonical_mgr.get_tag(tag)
        status = "✓ VALID" if tag_info else "❌ INVALID"
        print(f"   {i}. {tag:<25} [{status}]")
    
    # Get robot recommendations (ALL, not filtered)
    all_recommendations = recommender.recommend_tags(
        test_file,
        min_confidence=0.0,
        max_recommendations=200
    )
    
    print(f"\n{'='*100}")
    print("2️⃣  ROBOT RECOMMENDATIONS (What the system suggests)")
    print(f"{'='*100}\n")
    
    # Group by confidence level
    high_conf = [r for r in all_recommendations if r.confidence >= 0.70]
    med_conf = [r for r in all_recommendations if 0.50 <= r.confidence < 0.70]
    low_conf = [r for r in all_recommendations if r.confidence < 0.50]
    
    print(f"🟢 HIGH CONFIDENCE (70%+): {len(high_conf)} tags")
    for rec in high_conf[:10]:
        already = "✓" if rec.tag in existing_tags else "+"
        print(f"   {already} {rec.tag:<25} {rec.confidence:.0%}  [{rec.reason[:40]}]")
    if len(high_conf) > 10:
        print(f"   ... + {len(high_conf) - 10} more")
    
    print(f"\n🟡 MEDIUM CONFIDENCE (50-70%): {len(med_conf)} tags")
    for rec in med_conf[:8]:
        already = "✓" if rec.tag in existing_tags else "+"
        print(f"   {already} {rec.tag:<25} {rec.confidence:.0%}  [{rec.reason[:40]}]")
    if len(med_conf) > 8:
        print(f"   ... + {len(med_conf) - 8} more")
    
    print(f"\n🔴 LOW CONFIDENCE (<50%): {len(low_conf)} tags")
    print(f"   (Ignored by system, threshold is 60%)")
    
    # Analysis
    print(f"\n{'='*100}")
    print("3️⃣  ANALYSIS & COMPARISON")
    print(f"{'='*100}\n")
    
    recommended_set = set(r.tag for r in all_recommendations if r.confidence >= 0.60)
    existing_set = set(existing_tags)
    
    re_detected = existing_set & recommended_set
    missed = existing_set - recommended_set
    new = recommended_set - existing_set
    
    print(f"📊 MATCH ANALYSIS:")
    print(f"   Tags re-detected:    {len(re_detected)}/{len(existing_set)} ({len(re_detected)/len(existing_set)*100:.0f}%)")
    print(f"   Tags NOT found:      {len(missed)}")
    print(f"   New suggestions:     {len(new)}")
    
    if re_detected:
        print(f"\n   ✓ RE-DETECTED (robot found these in content):")
        for tag in sorted(re_detected):
            print(f"      • {tag}")
    
    if missed:
        print(f"\n   ❌ NOT DETECTED (robot couldn't find these in content):")
        for tag in sorted(missed):
            tag_info = canonical_mgr.get_tag(tag)
            desc = f" - {tag_info.description[:50]}" if tag_info and tag_info.description else ""
            print(f"      • {tag}{desc}")
    
    if new:
        print(f"\n   💡 NEW SUGGESTIONS (robot thinks these should be added):")
        high_new = [r for r in all_recommendations if r.tag in new and r.confidence >= 0.70]
        med_new = [r for r in all_recommendations if r.tag in new and 0.60 <= r.confidence < 0.70]
        
        if high_new:
            print(f"\n      High confidence (70%+):")
            for rec in high_new[:5]:
                print(f"         • {rec.tag:<25} {rec.confidence:.0%}")
        
        if med_new:
            print(f"\n      Medium confidence (60-70%):")
            for rec in med_new[:5]:
                print(f"         • {rec.tag:<25} {rec.confidence:.0%}")
    
    # Human analysis
    print(f"\n{'='*100}")
    print("👨‍🏫 MY HUMAN ANALYSIS")
    print(f"{'='*100}\n")
    
    print("""
This document is a PRACTICAL EXAMPLE showing different toolchain options 
(Terraform, CloudFormation, Helm) for implementing infrastructure as code.

Key Topics Found in Content:
  • Infrastructure as Code (IaC) → terraform, helm, cloudformation
  • Audit/Logging → logs, auditoria, audit trails
  • Vulnerabilities → SCA, SAST analysis
  • Different tools/frameworks → toolchain, ferramentas
  • AWS-specific tools → CloudFormation, CloudTrail
  • Kubernetes → helm, containers

My Recommended Tags (contextual):
  1. iac              ← Central topic, IaC implementations
  2. toolchain        ← Different tool options (already has ✓)
  3. ferramentas      ← About tools/frameworks (already has ✓)
  4. auditoria        ← Audit trails discussed
  5. logs             ← Centralized logging examples (already has ✓)
  6. sca              ← Vulnerability analysis mentioned
  7. deployment       ← Different deployment methods
  8. kubernetes       ← Helm/K8s section substantial
  9. aws              ← Heavy AWS focus (Terraform, CloudFormation)
  10. exemplo         ← It's a practical example (already has ✓)
  
Maybe Remove/Reconsider:
  • vulnerabilidades ← Too generic, prefer 'sca' or 'sast'
""")
    
    print(f"\n{'='*100}")
    print("📋 SUMMARY TABLE")
    print(f"{'='*100}\n")
    
    print(f"{'Current Tags':<40} {'Robot Finds?':<15} {'My Analysis'}")
    print(f"{'-'*100}")
    
    for tag in sorted(existing_tags):
        robot_found = "✓ YES" if tag in re_detected else "✗ NO"
        
        if tag == "toolchain":
            analysis = "✓ GOOD - core topic"
        elif tag == "ferramentas":
            analysis = "✓ GOOD - all about tools"
        elif tag == "iac":
            analysis = "✓ GOOD - main section"
        elif tag == "logs":
            analysis = "✓ GOOD - logging discussed"
        elif tag == "exemplos":
            analysis = "✓ GOOD - it's an example"
        elif tag == "vulnerabilidades":
            analysis = "⚠️ GENERIC - prefer 'sca/sast'"
        else:
            analysis = "?"
        
        print(f"{tag:<40} {robot_found:<15} {analysis}")
    
    print(f"\n{'='*100}\n")


if __name__ == "__main__":
    detailed_analysis()

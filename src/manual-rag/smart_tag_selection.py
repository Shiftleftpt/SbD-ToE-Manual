#!/usr/bin/env python3
"""
Smart tag filtering strategy for Docusaurus rendering
- Keep mandatory tags (grp_*, cat_*)
- Limit total to ~7 tags max (configurable)
- Select highest confidence tags within limit
"""

import json
from pathlib import Path
from typing import Dict, List, Set
import sys
from dataclasses import dataclass

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "tag-normalization"))

from manual_rag.tagging import AutoTagger, FileTagUpdater
from manual_rag.config import MANUAL_ROOT


@dataclass
class TagPriority:
    """Tag with priority for display"""
    tag: str
    confidence: float
    source: str
    is_mandatory: bool
    category: str  # 'mandatory', 'existing', 'suggested'


def categorize_tags(tags: List[str]) -> Dict[str, List[str]]:
    """Categorize tags by prefix"""
    categories = {
        'mandatory': [],      # grp_*, cat_*, tipo:*
        'framework': [],      # Cross-framework tags (iso27001, gdpr, etc)
        'technical': [],      # Technical tags (cicd, containers, etc)
        'practice': [],       # Practice tags (playbook, exemplo, etc)
        'other': []
    }
    
    for tag in tags:
        if tag.startswith('grp_') or tag.startswith('cat_') or ':' in tag:
            categories['mandatory'].append(tag)
        elif tag in ['gdpr', 'iso27001', 'cra', 'dora', 'nis2', 'nist', 'cis', 'asvs', 'capec', 'stride']:
            categories['framework'].append(tag)
        elif tag in ['cicd', 'containers', 'kubernetes', 'docker', 'terraform', 'sast', 'dast', 'sbom', 'sca', 'devsecops']:
            categories['technical'].append(tag)
        elif tag in ['playbook', 'exemplo', 'exemplos', 'checklist', 'guidelines', 'implementacao']:
            categories['practice'].append(tag)
        else:
            categories['other'].append(tag)
    
    return categories


def select_tags_for_display(all_tags: List[str], suggested_tags: Dict, 
                           max_total: int = 7, existing_tags: List[str] = None) -> Dict:
    """
    Select tags for Docusaurus display
    
    Strategy:
    1. Keep ALL mandatory tags (grp_*, cat_*, tipo:*)
    2. Keep important existing tags
    3. Add highest-confidence suggestions to reach ~max_total
    
    Returns dict with:
    - selected_tags: Final list for display
    - rationale: Why each tag was kept
    - stats: Selection statistics
    """
    
    if existing_tags is None:
        existing_tags = []
    
    selected = {}
    remaining_slots = max_total
    
    # Step 1: Keep mandatory tags
    mandatory = [t for t in existing_tags if t.startswith('grp_') or t.startswith('cat_') or ':' in t]
    for tag in mandatory:
        selected[tag] = {
            'reason': 'MANDATORY (Docusaurus injector)',
            'confidence': 1.0,
            'source': 'mandatory'
        }
        remaining_slots -= 1
    
    if remaining_slots <= 0:
        return {
            'selected_tags': list(selected.keys()),
            'rationale': selected,
            'stats': {
                'total_selected': len(selected),
                'mandatory_count': len(mandatory),
                'suggested_count': 0,
                'max_total': max_total,
                'note': f'Reached max with mandatory tags only ({len(mandatory)} tags)'
            }
        }
    
    # Step 2: Keep existing non-mandatory tags (they have user intent)
    existing_non_mandatory = [t for t in existing_tags if t not in mandatory and t not in selected]
    for tag in existing_non_mandatory[:remaining_slots]:
        selected[tag] = {
            'reason': 'EXISTING (preserved)',
            'confidence': 1.0,
            'source': 'existing'
        }
        remaining_slots -= 1
    
    # Step 3: Add highest-confidence suggestions
    # Sort suggested tags by confidence
    sorted_suggestions = sorted(
        suggested_tags.items(),
        key=lambda x: x[1].get('confidence', 0),
        reverse=True
    )
    
    for tag, suggestion in sorted_suggestions:
        if remaining_slots <= 0:
            break
        
        if tag not in selected:
            selected[tag] = {
                'reason': f"SUGGESTED ({suggestion.get('source', 'rag')} confidence)",
                'confidence': suggestion.get('confidence', 0),
                'source': suggestion.get('source', 'rag')
            }
            remaining_slots -= 1
    
    return {
        'selected_tags': list(selected.keys()),
        'rationale': selected,
        'stats': {
            'total_selected': len(selected),
            'mandatory_count': len(mandatory),
            'existing_count': len([t for t in existing_non_mandatory if t in selected]),
            'suggested_count': len([s for s in selected.keys() if selected[s]['source'] != 'mandatory' and selected[s]['source'] != 'existing']),
            'max_total': max_total,
            'remaining_slots': remaining_slots
        }
    }


def analyze_file_with_smart_selection(file_path: Path, max_tags: int = 7) -> Dict:
    """Analyze file and select appropriate tags for display"""
    
    tagger = AutoTagger()
    frontmatter, content = FileTagUpdater.read_frontmatter(file_path)
    
    title = frontmatter.get('title', file_path.stem)
    existing_tags = frontmatter.get('tags', [])
    
    # Get suggestions
    suggestions = tagger.suggest_tags(
        str(file_path.relative_to(MANUAL_ROOT.parent)),
        content,
        title,
        existing_tags,
        min_confidence=0.60
    )
    
    # Merge using BALANCED strategy
    final_tags, new_tags = tagger.merge_tags(existing_tags, suggestions, strategy='balanced')
    
    # Convert suggestions to dict for selection
    suggestion_dict = {}
    for sugg in suggestions:
        suggestion_dict[sugg.tag] = {
            'confidence': sugg.confidence,
            'source': sugg.source,
            'reasoning': sugg.reasoning
        }
    
    # Select tags intelligently
    selection = select_tags_for_display(
        final_tags,
        suggestion_dict,
        max_total=max_tags,
        existing_tags=existing_tags
    )
    
    return {
        'file': str(file_path.relative_to(MANUAL_ROOT.parent)),
        'chapter': file_path.parent.name,
        'existing_tags': existing_tags,
        'all_suggested_tags': final_tags,
        'selected_tags': selection['selected_tags'],
        'selection_rationale': selection['rationale'],
        'stats': selection['stats'],
        'categories': categorize_tags(selection['selected_tags'])
    }


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--sample', type=int, default=0, help='Analyze N sample files')
    parser.add_argument('--max-tags', type=int, default=7, help='Max tags per document')
    parser.add_argument('--analysis', action='store_true', help='Show detailed analysis')
    args = parser.parse_args()
    
    print("\n" + "=" * 160)
    print("🎯 SMART TAG SELECTION FOR DOCUSAURUS")
    print("=" * 160)
    print(f"Strategy: Keep mandatory + select highest-confidence up to {args.max_tags} tags")
    print("=" * 160)
    
    # Find sample files
    base_path = MANUAL_ROOT.parent
    all_files = sorted(list(base_path.rglob("*.md")))
    all_files = [f for f in all_files if not str(f).endswith('.2review')]
    
    tagged_files = []
    for md_file in all_files:
        try:
            with open(md_file, 'r') as f:
                content = f.read()
                if 'tags: [' in content or "tags: '" in content:
                    tagged_files.append(md_file)
        except:
            pass
    
    if args.sample > 0:
        tagged_files = tagged_files[:args.sample]
    
    print(f"\nAnalyzing {len(tagged_files)} files...\n")
    
    results = []
    stats = {
        'total_files': len(tagged_files),
        'avg_existing_tags': 0,
        'avg_suggested_tags': 0,
        'avg_selected_tags': 0,
        'files_need_reduction': 0,
        'files_within_limit': 0
    }
    
    for i, file_path in enumerate(tagged_files, 1):
        print(f"\r[{i:3}/{len(tagged_files)}] {file_path.name:50}", end="", flush=True)
        
        try:
            analysis = analyze_file_with_smart_selection(file_path, args.max_tags)
            results.append(analysis)
            
            existing_count = len(analysis['existing_tags'])
            suggested_count = len(analysis['all_suggested_tags'])
            selected_count = len(analysis['selected_tags'])
            
            stats['avg_existing_tags'] += existing_count
            stats['avg_suggested_tags'] += suggested_count
            stats['avg_selected_tags'] += selected_count
            
            if suggested_count > args.max_tags:
                stats['files_need_reduction'] += 1
            else:
                stats['files_within_limit'] += 1
        
        except Exception as e:
            print(f"\n✗ ERROR: {file_path.name}: {str(e)}")
    
    print("\n")
    
    # Calculate averages
    if len(results) > 0:
        stats['avg_existing_tags'] /= len(results)
        stats['avg_suggested_tags'] /= len(results)
        stats['avg_selected_tags'] /= len(results)
    
    # Print summary
    print("=" * 160)
    print("📊 ANALYSIS SUMMARY")
    print("=" * 160)
    
    print(f"""
Files analyzed: {stats['total_files']}

TAG COUNT STATISTICS:
  Average existing tags: {stats['avg_existing_tags']:.1f}
  Average suggested tags: {stats['avg_suggested_tags']:.1f}
  Average selected tags (for display): {stats['avg_selected_tags']:.1f}
  Target max: {args.max_tags}

FILES STATUS:
  Within limit: {stats['files_within_limit']} ({stats['files_within_limit']/stats['total_files']*100:.1f}%)
  Need reduction: {stats['files_need_reduction']} ({stats['files_need_reduction']/stats['total_files']*100:.1f}%)
""")
    
    # Show samples
    print("=" * 160)
    print("📋 SAMPLE ANALYSIS")
    print("=" * 160)
    
    for i, result in enumerate(results[:3], 1):
        print(f"\n{i}. FILE: {Path(result['file']).name}")
        print(f"   Chapter: {result['chapter']}")
        print(f"   Existing: {len(result['existing_tags'])} tags")
        print(f"   Suggested: {len(result['all_suggested_tags'])} tags")
        print(f"   Selected for display: {len(result['selected_tags'])} tags")
        
        print(f"\n   TAG BREAKDOWN:")
        print(f"   ├─ Mandatory (grp_/cat_): {len(result['categories']['mandatory'])}")
        for tag in result['categories']['mandatory']:
            print(f"   │  • {tag}")
        
        if result['categories']['framework']:
            print(f"   ├─ Framework tags: {len(result['categories']['framework'])}")
            for tag in result['categories']['framework'][:3]:
                print(f"   │  • {tag}")
        
        if result['categories']['technical']:
            print(f"   ├─ Technical tags: {len(result['categories']['technical'])}")
            for tag in result['categories']['technical'][:3]:
                print(f"   │  • {tag}")
        
        if result['categories']['practice']:
            print(f"   ├─ Practice tags: {len(result['categories']['practice'])}")
            for tag in result['categories']['practice'][:3]:
                print(f"   │  • {tag}")
    
    # Save detailed results
    output_file = Path(__file__).parent / "smart_tag_selection_analysis.json"
    with open(output_file, 'w') as f:
        json.dump({
            'config': {
                'max_tags_per_document': args.max_tags,
                'strategy': 'keep_mandatory + highest_confidence'
            },
            'statistics': stats,
            'sample_results': results[:10]
        }, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Detailed analysis saved: {output_file}")
    
    print("\n" + "=" * 160)
    print("💡 RECOMMENDATIONS")
    print("=" * 160)
    print(f"""
STRATEGY FOR DOCUSAURUS:
1. Always keep mandatory tags (grp_*, cat_*, tipo:*, tema:*)
2. Keep existing tags (they have user intent)
3. Add high-confidence suggestions (>70%) to fill remaining slots
4. Target: 5-7 tags total per document (readable, visually clean)

IMPLEMENTATION:
- Update generate_review_report.py to use smart selection
- Modify FileTagUpdater to apply selected_tags instead of all_tags
- Configure max_tags per document or by chapter

This ensures:
✓ Docusaurus injectors work (mandatory tags preserved)
✓ Readable UI (7 tags max)
✓ High-quality suggestions only (>70% confidence)
✓ User intent preserved (existing tags kept)
""")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Pre-review analysis report - Detailed exploration of tag changes before CSV review

Generates a comprehensive JSON report showing:
- Current tags vs proposed tags
- Exact additions and removals per file
- Confidence scores and reasoning
- Statistics and patterns
- Recommendations

Usage:
    python3 analyze_tag_changes.py [--sample N] [--chapter NAME] [--output FILE]
"""

import json
from pathlib import Path
from typing import Dict, List, Set
import sys
from datetime import datetime

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from rag_tools.tagging import AutoTagger, FileTagUpdater
from rag_tools.tagging.utils import select_tags_for_display
from rag_core.config import MANUAL_ROOT


def analyze_file_detailed(file_path: Path, max_tags: int = 7) -> Dict:
    """
    Deep analysis of a single file's tag situation
    
    Returns structured data with all decisions explained
    """
    
    tagger = AutoTagger()
    frontmatter, content = FileTagUpdater.read_frontmatter(file_path)
    
    title = frontmatter.get('title', file_path.stem)
    existing_tags = frontmatter.get('tags', [])
    existing_set = set(existing_tags)
    
    # Get ALL suggestions (not filtered)
    suggestions = tagger.suggest_tags(
        str(file_path.relative_to(MANUAL_ROOT.parent)),
        content,
        title,
        existing_tags,
        min_confidence=0.30  # Low threshold to see everything
    )
    
    # Merge using BALANCED strategy
    final_tags, new_tags = tagger.merge_tags(existing_tags, suggestions, strategy='balanced')
    final_set = set(final_tags)
    
    # Convert suggestions to dict with full details
    suggestion_dict = {}
    for sugg in suggestions:
        suggestion_dict[sugg.tag] = {
            'confidence': sugg.confidence,
            'source': sugg.source,
            'reasoning': sugg.reasoning
        }
    
    # Apply smart selection for display
    selection = select_tags_for_display(
        final_tags,
        suggestion_dict,
        max_total=max_tags,
        existing_tags=existing_tags
    )
    
    selected_tags = selection['selected_tags']
    selected_set = set(selected_tags)
    
    # Calculate detailed decisions
    added = selected_set - existing_set
    removed = existing_set - selected_set
    retained = existing_set & selected_set
    
    # Build detailed rationale for EACH decision
    
    # A) RETAINED tags (existing + in proposed)
    retained_details = {}
    for tag in sorted(retained):
        if tag in suggestion_dict:
            retained_details[tag] = {
                'decision': 'KEEP',
                'existing': True,
                'suggested': True,
                'confidence': f"{suggestion_dict[tag]['confidence']*100:.0f}%",
                'source': suggestion_dict[tag].get('source', 'rag'),
                'reasoning': suggestion_dict[tag].get('reasoning', 'User selected'),
                'explanation': f"Tag exists + recomendado com {suggestion_dict[tag]['confidence']*100:.0f}% confidence"
            }
        else:
            # Existing tag but NOT in suggestions (e.g., low confidence but user chose it)
            retained_details[tag] = {
                'decision': 'KEEP',
                'existing': True,
                'suggested': False,
                'confidence': 'N/A',
                'reason': 'Low confidence or out of scope',
                'explanation': 'Tag preservado por user intent (não aparece nas recomendações atuais)'
            }
    
    # B) ADDED tags (in proposed but NOT existing)
    added_details = {}
    for tag in sorted(added):
        for sugg in suggestions:
            if sugg.tag == tag:
                added_details[tag] = {
                    'decision': 'ADD',
                    'existing': False,
                    'suggested': True,
                    'confidence': f"{sugg.confidence*100:.0f}%",
                    'source': sugg.source,
                    'reasoning': sugg.reasoning,
                    'explanation': f"Recomendado com {sugg.confidence*100:.0f}% confidence por: {sugg.reasoning}"
                }
                break
    
    # C) REMOVED tags (in existing but NOT in proposed)
    # This includes tags that either:
    # - Have low confidence
    # - Are overflowed (>7 tags)
    # - Don't match document context
    removed_details = {}
    for tag in sorted(removed):
        # Check if it was suggested with low confidence
        low_conf_suggestion = None
        for sugg in suggestions:
            if sugg.tag == tag:
                low_conf_suggestion = sugg
                break
        
        if low_conf_suggestion:
            removed_details[tag] = {
                'decision': 'REMOVE',
                'existing': True,
                'suggested': True,
                'confidence': f"{low_conf_suggestion.confidence*100:.0f}%",
                'reason': 'Low confidence (<60%) - filtered out',
                'explanation': f"Existente MAS com baixa confiança ({low_conf_suggestion.confidence*100:.0f}%). AutoTagger sugere remover. Razão: {low_conf_suggestion.reasoning}"
            }
        else:
            # Not suggested at all
            removed_details[tag] = {
                'decision': 'REMOVE',
                'existing': True,
                'suggested': False,
                'confidence': 'N/A',
                'reason': 'Not in current suggestions - possibly out of context',
                'explanation': 'Tag não aparece nas recomendações atuais. Pode não ser relevante para este documento/capítulo.'
            }
    
    # Build comprehensive analysis
    analysis = {
        'file': str(file_path.relative_to(MANUAL_ROOT.parent)),
        'chapter': file_path.parent.name,
        'title': title,
        
        # CLEAR DECISION BREAKDOWN
        'decisions': {
            'KEEP': {
                'count': len(retained),
                'tags': retained_details,
                'explanation': 'Tags mantidas (existem + são recomendadas OU preservadas por user intent)'
            },
            'ADD': {
                'count': len(added),
                'tags': added_details,
                'explanation': 'Tags a adicionar (recomendadas mas não existem)'
            },
            'REMOVE': {
                'count': len(removed),
                'tags': removed_details,
                'explanation': 'Tags a remover (existem mas não são recomendadas ou confiança baixa)'
            }
        },
        
        # Summary stats
        'current': {
            'tags': sorted(existing_tags),
            'count': len(existing_tags),
        },
        
        'proposed': {
            'tags': sorted(selected_tags),
            'count': len(selected_tags),
        },
        
        'stats': {
            'total_suggestions_considered': len(suggestions),
            'high_confidence_suggestions': len([s for s in suggestions if s.confidence >= 0.70]),
            'medium_confidence_suggestions': len([s for s in suggestions if 0.50 <= s.confidence < 0.70]),
            'low_confidence_suggestions': len([s for s in suggestions if s.confidence < 0.50]),
            'max_tags_setting': max_tags,
            'change_magnitude': 'small' if len(added) + len(removed) <= 2 else 'medium' if len(added) + len(removed) <= 4 else 'large',
            'net_change': len(added) - len(removed)
        },
        
        # Recommendation
        'recommendation': (
            '✅ APPROVE - Tags estão bem balanceadas' if len(added) <= 1 and len(removed) <= 1 else
            '⚠️  REVIEW - Várias mudanças, verifica rationale' if len(added) + len(removed) > 4 else
            '🤔 INVESTIGATE - Removals significativas' if len(removed) > 1 else
            '✅ APPROVE - Mudanças fazem sentido'
        )
    }
    
    return analysis


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Analyze tag changes before CSV review')
    parser.add_argument('--sample', type=int, default=0, help='Limit to N files (0 = all)')
    parser.add_argument('--chapter', help='Filter by chapter name')
    parser.add_argument('--output', help='Output file (default: tag_analysis_TIMESTAMP.json)')
    parser.add_argument('--max-tags', type=int, default=7, help='Max tags per document')
    args = parser.parse_args()
    
    print("\n" + "=" * 180)
    print("📊 PRE-REVIEW TAG ANALYSIS REPORT")
    print("=" * 180)
    print("Detailed exploration of all proposed tag changes\n")
    
    # Find files
    base_path = MANUAL_ROOT.parent
    all_files = sorted(list(base_path.rglob("*.md")))
    all_files = [f for f in all_files if not str(f).endswith('.2review')]
    
    tagged_files = []
    for md_file in all_files:
        try:
            with open(md_file, 'r') as f:
                content = f.read()
                if ('tags: [' in content or "tags: '" in content):
                    if args.chapter is None or args.chapter in str(md_file):
                        tagged_files.append(md_file)
        except:
            pass
    
    if args.sample > 0:
        tagged_files = tagged_files[:args.sample]
    
    print(f"Analyzing {len(tagged_files)} files...\n")
    
    analyses = []
    global_stats = {
        'total_files': len(tagged_files),
        'files_with_additions': 0,
        'files_with_removals': 0,
        'files_unchanged': 0,
        'total_tags_to_add': 0,
        'total_tags_to_remove': 0,
        'high_confidence_additions': 0,
        'by_confidence_level': {
            'high': 0,
            'medium': 0,
            'low': 0
        }
    }
    
    for i, file_path in enumerate(tagged_files, 1):
        print(f"\r[{i:3}/{len(tagged_files)}] {file_path.name:50}", end="", flush=True)
        
        try:
            analysis = analyze_file_detailed(file_path, max_tags=args.max_tags)
            analyses.append(analysis)
            
            # Update global stats
            if analysis['decisions']['ADD']['count'] > 0:
                global_stats['files_with_additions'] += 1
                global_stats['total_tags_to_add'] += analysis['decisions']['ADD']['count']
                
                for tag, details in analysis['decisions']['ADD']['tags'].items():
                    confidence_raw = float(details.get('confidence', '0%').rstrip('%')) / 100
                    if confidence_raw >= 0.70:
                        global_stats['high_confidence_additions'] += 1
            
            if analysis['decisions']['REMOVE']['count'] > 0:
                global_stats['files_with_removals'] += 1
                global_stats['total_tags_to_remove'] += analysis['decisions']['REMOVE']['count']
            
            if analysis['decisions']['ADD']['count'] == 0 and analysis['decisions']['REMOVE']['count'] == 0:
                global_stats['files_unchanged'] += 1
            
            # Confidence distribution
            global_stats['by_confidence_level']['high'] += analysis['stats']['high_confidence_suggestions']
            global_stats['by_confidence_level']['medium'] += analysis['stats']['medium_confidence_suggestions']
            global_stats['by_confidence_level']['low'] += analysis['stats']['low_confidence_suggestions']
        
        except Exception as e:
            print(f"\n✗ ERROR: {file_path.name}: {str(e)}")
    
    print("\n\n" + "=" * 180)
    print("📈 GLOBAL STATISTICS")
    print("=" * 180)
    print(f"""
Files analyzed: {global_stats['total_files']}
├─ With additions: {global_stats['files_with_additions']} ({global_stats['files_with_additions']/max(global_stats['total_files'], 1)*100:.1f}%)
├─ With removals: {global_stats['files_with_removals']} ({global_stats['files_with_removals']/max(global_stats['total_files'], 1)*100:.1f}%)
└─ Unchanged: {global_stats['files_unchanged']} ({global_stats['files_unchanged']/max(global_stats['total_files'], 1)*100:.1f}%)

Changes Summary:
├─ Total tags to add: {global_stats['total_tags_to_add']}
│  └─ High confidence (≥70%): {global_stats['high_confidence_additions']}
├─ Total tags to remove: {global_stats['total_tags_to_remove']}
└─ Net change: {global_stats['total_tags_to_add'] - global_stats['total_tags_to_remove']:+d}

Confidence Distribution of All Suggestions:
├─ High (≥70%): {global_stats['by_confidence_level']['high']}
├─ Medium (50-70%): {global_stats['by_confidence_level']['medium']}
└─ Low (<50%): {global_stats['by_confidence_level']['low']}
""")
    
    # Show samples of biggest changes
    print("=" * 180)
    print("🔍 TOP 5 BIGGEST CHANGES")
    print("=" * 180)
    
    by_magnitude = sorted(analyses, key=lambda a: a['decisions']['ADD']['count'] + a['decisions']['REMOVE']['count'], reverse=True)[:5]
    
    for i, analysis in enumerate(by_magnitude, 1):
        print(f"\n{i}. {Path(analysis['file']).name}")
        print(f"   Chapter: {analysis['chapter']}")
        print(f"   Current: {analysis['current']['count']} tags → Proposed: {analysis['proposed']['count']} tags")
        print(f"   Recommendation: {analysis['recommendation']}")
        print()
        
        # KEEP section
        keep_count = analysis['decisions']['KEEP']['count']
        if keep_count > 0:
            print(f"   ✅ MANTER ({keep_count} tags):")
            for tag, details in list(analysis['decisions']['KEEP']['tags'].items())[:3]:
                conf = details.get('confidence', 'N/A')
                if details.get('suggested'):
                    print(f"      • {tag} ({conf}) - Existente + Recomendado")
                else:
                    print(f"      • {tag} - Preservado (user intent)")
            if keep_count > 3:
                print(f"      ... e {keep_count - 3} mais")
        
        # ADD section
        add_count = analysis['decisions']['ADD']['count']
        if add_count > 0:
            print(f"   ➕ ADICIONAR ({add_count} tags):")
            for tag, details in list(analysis['decisions']['ADD']['tags'].items())[:3]:
                conf = details.get('confidence', 'N/A')
                reason = details.get('reasoning', '')[:50]
                print(f"      • {tag} ({conf}) - {reason}")
            if add_count > 3:
                print(f"      ... e {add_count - 3} mais")
        
        # REMOVE section
        remove_count = analysis['decisions']['REMOVE']['count']
        if remove_count > 0:
            print(f"   ➖ REMOVER ({remove_count} tags):")
            for tag, details in list(analysis['decisions']['REMOVE']['tags'].items())[:3]:
                reason = details.get('reason', 'Não recomendado')
                print(f"      • {tag} - {reason}")
            if remove_count > 3:
                print(f"      ... e {remove_count - 3} mais")
    
    # Save full report
    output_file = args.output or f"tag_analysis_{datetime.now().strftime('%Y-%m-%dT%H-%M-%S')}.json"
    output_path = Path(__file__).parent / output_file
    
    report = {
        'metadata': {
            'generated': datetime.now().isoformat(),
            'max_tags_setting': args.max_tags,
            'files_analyzed': len(tagged_files),
            'chapter_filter': args.chapter
        },
        'global_stats': global_stats,
        'files': analyses
    }
    
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print("\n\n" + "=" * 180)
    print("✅ FULL REPORT SAVED")
    print("=" * 180)
    print(f"Location: {output_path}")
    print(f"""
Report contains for EACH FILE:
├─ Current tags (breakdown by type)
├─ Proposed tags (breakdown by type)
├─ Detailed additions (confidence + reasoning)
├─ Detailed removals (why they're being removed)
├─ Retained tags (why they're staying)
├─ All suggestions considered (with decision)
└─ Recommendation for manual review

NEXT STEPS:
1. Open: {output_file}
2. Search for "INVESTIGATE" recommendations
3. Check high-impact files (biggest changes)
4. Identify patterns or concerns
5. Then run: generate_review_report.py to create CSV for final approval
""")


if __name__ == "__main__":
    main()

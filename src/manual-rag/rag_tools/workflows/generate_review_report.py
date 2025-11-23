#!/usr/bin/env python3
"""
Generate detailed auto-tagging review report with SMART tag selection
Lists current tags, proposed tags (limited to ~7 readable tags), rationale, and OK column
"""

import json
from pathlib import Path
from typing import Dict, List, Tuple
import sys
from datetime import datetime

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from rag_tools.tagging import AutoTagger, FileTagUpdater
from rag_tools.utils.smart_tag_selection import select_tags_for_display
from rag_core.config import MANUAL_ROOT


def get_document_summary(file_path: Path, content: str) -> str:
    """Extract 2-line summary about the document"""
    # Get first non-empty lines from content
    lines = content.strip().split('\n')
    summary_lines = []
    
    for line in lines:
        if line.strip() and not line.startswith('#'):
            # Skip yaml/frontmatter
            summary_lines.append(line.strip()[:80])
            if len(summary_lines) >= 2:
                break
    
    return ' | '.join(summary_lines[:2]) if summary_lines else "(No summary available)"


def analyze_file(file_path: Path, max_tags: int = 7) -> Dict:
    """Analyze a single file for tag review with smart selection"""
    
    tagger = AutoTagger()
    frontmatter, content = FileTagUpdater.read_frontmatter(file_path)
    
    title = frontmatter.get('title', file_path.stem)
    existing_tags = frontmatter.get('tags', [])
    existing_set = set(existing_tags)
    
    # Get suggestions
    suggestions = tagger.suggest_tags(
        str(file_path.relative_to(MANUAL_ROOT.parent)),
        content,
        title,
        existing_tags,
        min_confidence=0.60
    )
    
    # Merge using BALANCED strategy (full set for analysis)
    final_tags, new_tags = tagger.merge_tags(existing_tags, suggestions, strategy='balanced')
    final_set = set(final_tags)
    
    # Convert suggestions to dict for smart selection
    suggestion_dict = {}
    for sugg in suggestions:
        suggestion_dict[sugg.tag] = {
            'confidence': sugg.confidence,
            'source': sugg.source,
            'reasoning': sugg.reasoning
        }
    
    # Apply smart selection (keep readable number of tags)
    selection = select_tags_for_display(
        final_tags,
        suggestion_dict,
        max_total=max_tags,
        existing_tags=existing_tags
    )
    
    selected_tags = selection['selected_tags']
    selected_set = set(selected_tags)
    
    # Calculate changes based on SELECTION (not full suggestion)
    added = selected_set - existing_set
    removed = existing_set - selected_set
    retained = existing_set & selected_set
    
    # Build rationale for additions
    added_rationale = {}
    for suggestion in suggestions:
        if suggestion.tag in added:
            added_rationale[suggestion.tag] = {
                'confidence': f"{suggestion.confidence*100:.0f}%",
                'source': suggestion.source,
                'reasoning': suggestion.reasoning
            }
    
    # Build review record
    review = {
        'file': str(file_path.relative_to(MANUAL_ROOT.parent)),
        'chapter': file_path.parent.name,
        'summary': get_document_summary(file_path, content),
        'existing_tags': sorted(existing_tags),
        'existing_count': len(existing_set),
        'all_suggested_tags': sorted(final_tags),  # For reference
        'proposed_tags': sorted(selected_tags),     # Smart-selected for display
        'proposed_count': len(selected_set),
        'added': sorted(list(added)),
        'added_count': len(added),
        'added_rationale': added_rationale,
        'removed': sorted(list(removed)),
        'removed_count': len(removed),
        'retained': sorted(list(retained)),
        'retained_count': len(retained),
        'max_tags': max_tags,
        'approval_status': 'PENDING'  # User will set to 'OK' to approve
    }
    
    return review


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--sample', type=int, default=0, help='Limit to N files (0 = all)')
    parser.add_argument('--chapter', help='Filter by chapter name')
    parser.add_argument('--max-tags', type=int, default=7, help='Max tags per document for display')
    args = parser.parse_args()
    
    sample_size = args.sample
    chapter_filter = args.chapter
    max_tags = args.max_tags
    
    print("\n" + "=" * 180)
    print("📋 AUTO-TAGGING REVIEW REPORT GENERATOR")
    print("=" * 180)
    print("This report allows you to review all proposed tag changes before applying them.")
    print("Set approval_status to 'OK' for changes you want to apply.")
    print("=" * 180)
    
    # Find all markdown files
    base_path = MANUAL_ROOT.parent
    all_files = sorted(list(base_path.rglob("*.md")))
    all_files = [f for f in all_files if not str(f).endswith('.2review')]
    
    # Filter to files with tags
    tagged_files = []
    for md_file in all_files:
        try:
            with open(md_file, 'r') as f:
                content = f.read()
                if ('tags: [' in content or "tags: '" in content):
                    if chapter_filter is None or chapter_filter in str(md_file):
                        tagged_files.append(md_file)
        except:
            pass
    
    if sample_size > 0:
        tagged_files = tagged_files[:sample_size]
    
    print(f"\nProcessing: {len(tagged_files)} files with existing tags")
    print(f"Output format: CSV with detailed review information\n")
    
    reviews = []
    
    for i, file_path in enumerate(tagged_files, 1):
        print(f"\r[{i:3}/{len(tagged_files)}] Analyzing {file_path.name:50}", end="", flush=True)
        
        try:
            review = analyze_file(file_path, max_tags=max_tags)
            reviews.append(review)
        except Exception as e:
            print(f"\n✗ ERROR: {file_path.name}: {str(e)}")
    
    print("\n")
    
    # Generate CSV report
    timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    report_file = Path(__file__).parent / f"review_report_{timestamp}.csv"
    
    print(f"📝 Generating review report...\n")
    
    # Write CSV with detailed information
    with open(report_file, 'w', encoding='utf-8') as f:
        # Write header
        f.write("CHAPTER,FILE,SUMMARY,CURRENT_TAGS,PROPOSED_TAGS,TAGS_ADDED,TAGS_REMOVED,RATIONALE_ADDED,APPROVAL_STATUS\n")
        
        for review in reviews:
            # Escape and format data
            chapter = review['chapter'].replace(',', ';')
            file = review['file'].replace(',', ';')
            summary = review['summary'].replace(',', ';').replace('\n', ' ')[:100]
            
            current_tags = '|'.join(review['existing_tags'])
            proposed_tags = '|'.join(review['proposed_tags'])
            added_tags = '|'.join(review['added'])
            removed_tags = '|'.join(review['removed'])
            
            # Build detailed rationale for additions
            rationale_parts = []
            for tag in review['added']:
                if tag in review['added_rationale']:
                    r = review['added_rationale'][tag]
                    rationale_parts.append(f"{tag}({r['confidence']},{r['source']}:{r['reasoning'][:30]})")
            
            rationale = '; '.join(rationale_parts) if rationale_parts else ''
            
            # Write row
            f.write(f"{chapter},{file},\"{summary}\",\"{current_tags}\",\"{proposed_tags}\",\"{added_tags}\",\"{removed_tags}\",\"{rationale}\",PENDING\n")
    
    print(f"✅ CSV Report generated: {report_file}\n")
    
    # Also generate JSON for programmatic processing
    json_file = Path(__file__).parent / f"review_report_{timestamp}.json"
    with open(json_file, 'w') as f:
        json.dump(reviews, f, indent=2, ensure_ascii=False)
    
    print(f"✅ JSON Report generated: {json_file}\n")
    
    # Print statistics
    total_files = len(reviews)
    files_with_changes = sum(1 for r in reviews if r['added_count'] + r['removed_count'] > 0)
    total_added = sum(r['added_count'] for r in reviews)
    total_removed = sum(r['removed_count'] for r in reviews)
    
    print("=" * 180)
    print("📊 SUMMARY STATISTICS")
    print("=" * 180)
    print(f"Files analyzed: {total_files}")
    print(f"Files with changes: {files_with_changes} ({files_with_changes/total_files*100:.1f}%)")
    print(f"Total tags to add: {total_added}")
    print(f"Total tags to remove: {total_removed}")
    print(f"Net change: {total_added - total_removed:+d}\n")
    
    # Print sample records
    print("=" * 180)
    print("📋 SAMPLE RECORDS (first 5 files with changes)")
    print("=" * 180)
    
    changes_only = [r for r in reviews if r['added_count'] + r['removed_count'] > 0][:5]
    
    for i, review in enumerate(changes_only, 1):
        print(f"\n{i}. FILE: {review['file']}")
        print(f"   CHAPTER: {review['chapter']}")
        print(f"   SUMMARY: {review['summary'][:100]}...")
        print(f"   CURRENT TAGS ({review['existing_count']}): {', '.join(review['existing_tags'][:5])}{'...' if review['existing_count'] > 5 else ''}")
        print(f"   PROPOSED TAGS ({review['proposed_count']}): {', '.join(review['proposed_tags'][:5])}{'...' if review['proposed_count'] > 5 else ''}")
        
        if review['added']:
            print(f"   + ADDED ({review['added_count']}): {', '.join(review['added'][:3])}{'...' if review['added_count'] > 3 else ''}")
            for tag in review['added'][:2]:
                rat = review['added_rationale'].get(tag, {})
                print(f"      - {tag}: {rat.get('confidence', '')} ({rat.get('source', '')}) - {rat.get('reasoning', '')[:50]}")
        
        if review['removed']:
            print(f"   - REMOVED ({review['removed_count']}): {', '.join(review['removed'][:3])}{'...' if review['removed_count'] > 3 else ''}")
        
        print(f"   APPROVAL: {review['approval_status']}")
    
    print("\n" + "=" * 180)
    print("✅ NEXT STEPS:")
    print("=" * 180)
    print(f"""
1. REVIEW the reports:
   - CSV: {report_file.name}
   - JSON: {json_file.name}

2. EDIT the CSV file:
   - Change PENDING → OK to approve changes
   - Leave as PENDING to skip changes

3. APPLY approved changes:
   - Run: python3 apply_review_decisions.py {report_file.name}

This two-step process ensures you have full control over which tags are modified.
""")


if __name__ == "__main__":
    main()

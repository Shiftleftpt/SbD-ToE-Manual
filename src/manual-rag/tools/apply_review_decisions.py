#!/usr/bin/env python3
"""
Apply approved tag changes from review report
Only processes files marked with approval_status = OK
"""

import json
from pathlib import Path
from typing import Dict
import sys
import csv

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from manual_rag.tagging import FileTagUpdater
from manual_rag.config import MANUAL_ROOT


def apply_csv_decisions(csv_file: Path):
    """Apply tag changes from CSV review report"""
    
    if not csv_file.exists():
        print(f"❌ Report file not found: {csv_file}")
        sys.exit(1)
    
    print("\n" + "=" * 180)
    print("🔄 APPLYING TAG CHANGES FROM REVIEW REPORT")
    print("=" * 180)
    
    # Load decisions from CSV
    decisions = {}
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            file_path = row['FILE']
            approval = row['APPROVAL_STATUS'].strip().upper()
            proposed_tags = [t.strip() for t in row['PROPOSED_TAGS'].split('|') if t.strip()]
            
            decisions[file_path] = {
                'approval': approval,
                'proposed_tags': proposed_tags,
                'chapter': row['CHAPTER']
            }
    
    print(f"Loaded {len(decisions)} review decisions from {csv_file.name}\n")
    
    # Apply approved changes
    applied = 0
    skipped = 0
    errors = 0
    
    base_path = MANUAL_ROOT.parent
    
    for file_path_rel, decision in sorted(decisions.items()):
        if decision['approval'] != 'OK':
            skipped += 1
            continue
        
        # Construct full path
        full_path = base_path / file_path_rel
        
        if not full_path.exists():
            print(f"⚠️  FILE NOT FOUND: {file_path_rel}")
            errors += 1
            continue
        
        try:
            # Read current frontmatter
            frontmatter, content = FileTagUpdater.read_frontmatter(full_path)
            old_tags = frontmatter.get('tags', [])
            new_tags = decision['proposed_tags']
            
            # Update if different
            if old_tags != new_tags:
                frontmatter['tags'] = new_tags
                FileTagUpdater.write_frontmatter(full_path, frontmatter, content)
                
                added = set(new_tags) - set(old_tags)
                removed = set(old_tags) - set(new_tags)
                
                print(f"✅ {Path(file_path_rel).name}")
                if added:
                    print(f"   + {', '.join(sorted(list(added))[:3])}{'...' if len(added) > 3 else ''}")
                if removed:
                    print(f"   - {', '.join(sorted(list(removed))[:3])}{'...' if len(removed) > 3 else ''}")
                
                applied += 1
            else:
                print(f"⊘  {Path(file_path_rel).name} (no changes)")
        
        except Exception as e:
            print(f"❌ ERROR in {file_path_rel}: {str(e)}")
            errors += 1
    
    # Print summary
    print("\n" + "=" * 180)
    print("📊 APPLICATION SUMMARY")
    print("=" * 180)
    print(f"Files processed: {len(decisions)}")
    print(f"Changes applied: {applied}")
    print(f"Changes skipped: {skipped} (PENDING status)")
    print(f"Errors: {errors}")
    
    if errors == 0 and applied > 0:
        print(f"\n✅ SUCCESS: {applied} files updated with approved tags")
        print("\n📝 NEXT STEPS:")
        print("   1. Review the changes: git diff")
        print("   2. Commit: git add -A && git commit -m 'feat(tags): auto-tag corpus with BALANCED strategy'")
        print("   3. Push: git push")
    elif applied == 0:
        print(f"\n⊘  No changes applied (all files marked as PENDING)")
    else:
        print(f"\n⚠️  {errors} errors encountered")


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('report_file', help='CSV review report file to process')
    args = parser.parse_args()
    
    report_path = Path(__file__).parent / args.report_file
    
    if not report_path.exists():
        # Try without directory
        report_path = Path(args.report_file)
    
    apply_csv_decisions(report_path)


if __name__ == "__main__":
    main()

"""
Tagging workflows - Batch tag processing with multi-stage review

COMPLETE WORKFLOW (3 stages):

1. ANALYZE (analyze_tag_changes.py)
   └─ Detailed JSON report of all proposed changes
   └─ Shows: current vs proposed, confidence levels, rationale
   └─ Identifies patterns and high-impact files
   └─ Output: tag_analysis_TIMESTAMP.json

2. REVIEW (generate_review_report.py)
   └─ CSV report for manual approval/rejection
   └─ Shows: current tags | proposed tags | approval status
   └─ Editable: change proposals or mark PENDING to skip
   └─ Output: review_report_TIMESTAMP.csv + .json

3. APPLY (apply_review_decisions.py)
   └─ Applies only the CSV rows marked as OK
   └─ Updates file frontmatter with approved tags
   └─ Output: updated .md files

ALSO:
- regen_intro_tags.py: Special workflow to regenerate tags for intro.md files

Scripts (Entry Points):
- analyze_tag_changes.py: Deep exploration of changes
- generate_review_report.py: CSV review interface
- apply_review_decisions.py: Apply approved changes
- regen_intro_tags.py: Regenerate intro.md tags
"""

__all__ = [
    'analyze_tag_changes',
    'generate_review_report',
    'apply_review_decisions', 
    'regen_intro_tags'
]

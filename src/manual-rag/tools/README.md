#!/usr/bin/env python3
"""
Manual RAG Tools - Production Scripts

Three main workflows:
1. build_chunked_index.py    - Build JSONL dataset + Chroma vector index
2. generate_review_report.py - Generate tag suggestions with approval workflow
3. apply_review_decisions.py - Apply approved tag changes to files

Typical workflow:
-----------
# Step 1: Build or rebuild the index
python tools/build_chunked_index.py

# Step 2: Generate review report (all files or sample)
python tools/generate_review_report.py --max-tags 7
# or for testing:
python tools/generate_review_report.py --sample 5 --max-tags 7

# Step 3: Review the CSV file
# Edit review_report_TIMESTAMP.csv
# Change PENDING → OK for changes to apply

# Step 4: Apply approved changes
python tools/apply_review_decisions.py review_report_TIMESTAMP.csv

# Step 5: Commit to repository
git add -A
git commit -m "feat: Apply auto-tagged suggestions"
"""

#!/bin/bash
set -e

# Move core tools
mv -v build_chunked_index.py tools/ 2>/dev/null || echo "build_chunked_index.py already moved"
mv -v generate_review_report.py tools/ 2>/dev/null || echo "generate_review_report.py already moved"
mv -v apply_review_decisions.py tools/ 2>/dev/null || echo "apply_review_decisions.py already moved"

# Move utilities to scripts/utils
mv -v smart_tag_selection.py scripts/utils/ 2>/dev/null || echo "smart_tag_selection.py already moved"
mv -v manual_rag/batch.py scripts/utils/ 2>/dev/null || echo "batch.py already moved"

# Move testing scripts
mv -v test_*.py scripts/testing/ 2>/dev/null || echo "test_*.py already moved"
mv -v audit_tags_comprehensive.py scripts/testing/ 2>/dev/null || echo "audit_tags_comprehensive.py already moved"

# Archive legacy/deprecated scripts
mkdir -p scripts/legacy
mv -v build_index.py scripts/legacy/ 2>/dev/null || echo "build_index.py already moved"
mv -v auto_tag_corpus.py scripts/legacy/ 2>/dev/null || echo "auto_tag_corpus.py already moved"
mv -v analyze_recall_variance.py scripts/legacy/ 2>/dev/null || echo "analyze_recall_variance.py already moved"
mv -v run_extended_comparison.py scripts/legacy/ 2>/dev/null || echo "run_extended_comparison.py already moved"
mv -v run_four_way_comparison.py scripts/legacy/ 2>/dev/null || echo "run_four_way_comparison.py already moved"
mv -v quality_analysis.py scripts/legacy/ 2>/dev/null || echo "quality_analysis.py already moved"
mv -v audit_tags.py scripts/legacy/ 2>/dev/null || echo "audit_tags.py already moved"

echo "✓ File reorganization complete"

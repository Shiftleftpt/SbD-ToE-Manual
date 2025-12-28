#!/bin/bash
# Test script: Complete tagging workflow demonstration
# Shows: ANALYZE -> REVIEW -> APPLY

set -e

cd /Volumes/G-DRIVE/Shared/Manual-SbD-ToE/SbD-ToE-Manual/src/manual-rag

echo "════════════════════════════════════════════════════════════════════════"
echo "🧪 TAGGING WORKFLOW TEST"
echo "════════════════════════════════════════════════════════════════════════"
echo ""

# STEP 1: ANALYZE
echo "📊 STEP 1: ANALYZE - Deep exploration of tag changes"
echo "────────────────────────────────────────────────────────────────────────"
TIMESTAMP=$(date +%s)
python3 rag_tools/tagging/workflows/analyze_tag_changes.py --sample 3 --output "test_analysis_${TIMESTAMP}.json" 2>&1 | tail -30
echo ""

# STEP 2: REVIEW
echo "📋 STEP 2: REVIEW - Generate CSV for human approval"
echo "────────────────────────────────────────────────────────────────────────"
python3 rag_tools/tagging/workflows/generate_review_report.py --sample 3 2>&1 | tail -30
echo ""

# Find the latest CSV file
LATEST_CSV=$(ls -t rag_tools/tagging/workflows/review_report*.csv 2>/dev/null | head -1)

if [ -n "$LATEST_CSV" ]; then
    echo "✅ Review CSV created: $(basename $LATEST_CSV)"
    echo ""
    echo "CSV Content (preview):"
    echo "─────────────────────────────────────────────────────────────────────"
    head -1 "$LATEST_CSV" | tr ',' '\n' | nl
    echo ""
    echo "Sample rows:"
    head -3 "$LATEST_CSV" | tail -2 | cut -c1-120
    echo ""
    
    # STEP 3: APPLY (simulated - mark one as OK)
    echo "✅ STEP 3: APPLY - Simulated application (dry-run)"
    echo "────────────────────────────────────────────────────────────────────────"
    echo "To apply changes:"
    echo "  1. Edit CSV: $LATEST_CSV"
    echo "  2. Change PENDING → OK for rows to apply"
    echo "  3. Run: python3 rag_tools/tagging/workflows/apply_review_decisions.py $(basename $LATEST_CSV)"
    echo ""
else
    echo "❌ No CSV file found"
fi

echo "════════════════════════════════════════════════════════════════════════"
echo "✅ WORKFLOW TEST COMPLETE"
echo "════════════════════════════════════════════════════════════════════════"

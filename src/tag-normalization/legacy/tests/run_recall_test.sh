#!/bin/bash
# Quick runner for multi-file recall quality test
# This script runs the test and displays results

cd "$(dirname "$0")/.." || exit 1

if [ ! -d ".venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Run: python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

echo "🚀 Starting multi-file recall quality test..."
echo "=========================================="
echo ""

source .venv/bin/activate
python3 tests/recall_quality_test_multifile.py

echo ""
echo "=========================================="
echo "✅ Test complete!"
echo ""
echo "📊 Results saved in: tests/results/"
echo ""
echo "📋 To view latest results:"
echo "   cat tests/results/multifile_recall_analysis_*.txt | tail -150"
echo ""
echo "📁 To view as JSON:"
echo "   cat tests/results/multifile_recall_analysis_*.json | python3 -m json.tool | head -50"

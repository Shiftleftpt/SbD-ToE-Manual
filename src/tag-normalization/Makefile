.PHONY: help demo validate recommend audit scan view-report export-csv setup clean

BASE_PATH ?= /Volumes/G-DRIVE/Shared/Manual-SbD-ToE/SbD-ToE-Manual/manuals_src/docs/sbd-toe
REPORT ?= tag-analysis-report.json

help:
	@echo "🎯 Tag System - Makefile Commands"
	@echo "=================================="
	@echo ""
	@echo "DEMO:"
	@echo "  make demo              Run interactive demonstration"
	@echo ""
	@echo "SCANNING:"
	@echo "  make scan              Scan all chapters and generate report"
	@echo "  make view-report       View existing report with summary"
	@echo "  make export-csv        Export report to CSV"
	@echo ""
	@echo "CLI COMMANDS:"
	@echo "  make validate          Validate tags in BASE_PATH"
	@echo "  make recommend         Get tag recommendations for BASE_PATH"
	@echo "  make audit             Full validation + recommendations"
	@echo ""
	@echo "EXAMPLES:"
	@echo "  make scan BASE_PATH=/path/to/docs"
	@echo "  make view-report REPORT=my-report.json"
	@echo ""

demo:
	@echo "🎯 Running demo..."
	@python3 demos/demo.py

scan:
	@echo "🔍 Scanning chapters..."
	@echo "   Base: $(BASE_PATH)"
	@echo "   Report: $(REPORT)"
	@python3 reports/scan_chapters.py "$(BASE_PATH)" -o "$(REPORT)"

view-report:
	@echo "📊 Viewing report: $(REPORT)"
	@python3 reports/view_report.py -r "$(REPORT)" --all

view-summary:
	@python3 reports/view_report.py -r "$(REPORT)" --summary

view-no-tags:
	@python3 reports/view_report.py -r "$(REPORT)" --no-tags

export-csv:
	@echo "📁 Exporting to CSV..."
	@python3 reports/view_report.py -r "$(REPORT)" --export-csv tag-analysis.csv

validate:
	@cd tag_system && make validate BASE_PATH="$(BASE_PATH)"

recommend:
	@cd tag_system && make recommend BASE_PATH="$(BASE_PATH)"

audit:
	@cd tag_system && make audit BASE_PATH="$(BASE_PATH)"

test:
	@echo "🧪 Running tests..."
	@cd tag_system && make test

clean:
	@echo "🧹 Cleaning..."
	@find . -name "*.pyc" -delete
	@find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	@echo "✓ Clean"

setup:
	@echo "🔧 Setting up environment..."
	@./setup-env.sh

.DEFAULT_GOAL := help

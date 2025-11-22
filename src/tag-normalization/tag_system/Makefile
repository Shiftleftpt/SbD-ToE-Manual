.PHONY: help validate recommend audit test clean

SCRIPT_DIR := $(shell pwd)
BASE_PATH ?= ../../../manuals_src/docs/sbd-toe
PYTHON := python3

help:
	@echo "Tag System - Validation & Recommendation"
	@echo "=========================================="
	@echo ""
	@echo "Commands:"
	@echo "  make validate    - Validate existing tags"
	@echo "  make recommend   - Recommend missing tags"
	@echo "  make audit       - Full audit (validate + recommend)"
	@echo "  make test        - Run tests"
	@echo "  make clean       - Clean cache"
	@echo ""
	@echo "Options:"
	@echo "  BASE_PATH=path   - Base path for analysis"
	@echo "  LIMIT=N          - Limit files (for recommend)"
	@echo ""

validate:
	@$(PYTHON) -m cli.main_cli --base-path $(BASE_PATH) validate

recommend:
	@$(PYTHON) -m cli.main_cli --base-path $(BASE_PATH) recommend $(if $(LIMIT),--limit $(LIMIT))

audit:
	@$(PYTHON) -m cli.main_cli --base-path $(BASE_PATH) audit

test:
	@$(PYTHON) -m pytest tests/ -v

clean:
	@rm -rf __pycache__ **/__pycache__ .pytest_cache
	@echo "✓ Cleaned cache"

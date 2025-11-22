.PHONY: help setup install build search tag gaps xref health auto-tag auto-tag-dry tag-validate clean rebuild

# Colors for output
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[0;33m
RED := \033[0;31m
NC := \033[0m # No Color

VENV := rag_env
PYTHON := $(VENV)/bin/python3
PIP := $(VENV)/bin/pip

help:
	@echo "$(BLUE)Manual RAG System - Commands$(NC)"
	@echo ""
	@echo "$(GREEN)Setup & Installation:$(NC)"
	@echo "  make setup          - Setup Python environment (one-time)"
	@echo "  make install        - Install Python dependencies"
	@echo "  make build          - Build index for all 294 manual files (~2 min)"
	@echo ""
	@echo "$(GREEN)Queries & Analysis:$(NC)"
	@echo "  make search Q=...   - Search for similar documents (e.g. make search Q='secure coding')"
	@echo "  make tag F=...      - Suggest tags for a file (e.g. make tag F='010-sbd-manual/...')"
	@echo "  make gaps F=...     - Analyze gaps in a file"
	@echo "  make xref T=...     - Find cross-references (e.g. make xref T='authentication')"
	@echo ""
	@echo "$(GREEN)Auto-tagging (Phase B):$(NC)"
	@echo "  make auto-tag-dry   - Preview auto-tagging changes (dry run)"
	@echo "  make auto-tag       - Apply auto-tagging to all files"
	@echo "  make tag-validate   - Validate all tags against canonical"
	@echo ""
	@echo "$(GREEN)Utilities:$(NC)"
	@echo "  make health         - Check system status (Ollama, index, etc)"
	@echo "  make clean          - Remove virtual environment & cache"
	@echo "  make rebuild        - Clean and rebuild everything"
	@echo ""
	@echo "$(YELLOW)Examples:$(NC)"
	@echo "  $$ make setup                    # First time setup"
	@echo "  $$ make build                    # Build index (~2 min)"
	@echo "  $$ make search Q='authentication in microservices'"
	@echo "  $$ make tag F='010-sbd-manual/06-desenvolvimento-seguro/01-intro.md'"
	@echo "  $$ make auto-tag-dry             # Preview all changes"
	@echo "  $$ make auto-tag                 # Apply auto-tagging"

# Setup Python virtual environment (one-time)
setup: $(VENV)
	@echo "$(GREEN)✓ Environment setup complete$(NC)"

$(VENV):
	@echo "$(BLUE)Setting up Python virtual environment...$(NC)"
	python3 -m venv $(VENV)
	$(PIP) install -q --upgrade pip
	$(PIP) install -q -r requirements.txt
	@echo "$(GREEN)✓ Virtual environment created$(NC)"

# Install/update dependencies
install: $(VENV)
	@echo "$(BLUE)Installing dependencies...$(NC)"
	$(PIP) install -q -r requirements.txt
	@echo "$(GREEN)✓ Dependencies installed$(NC)"

# Build/rebuild the index
build: $(VENV)
	@echo "$(BLUE)Building index for 294 manual files...$(NC)"
	@echo "$(YELLOW)This may take 1-2 minutes...$(NC)"
	$(PYTHON) build_index.py
	@echo "$(GREEN)✓ Index ready$(NC)"

# Rebuild from scratch (clean + build)
rebuild: clean build
	@echo "$(GREEN)✓ Rebuild complete$(NC)"

# Search for similar documents
search: $(VENV) check_index
	@if [ -z "$(Q)" ]; then \
		echo "$(RED)Error: Query required$(NC)"; \
		echo "Usage: make search Q='your query'"; \
		exit 1; \
	fi
	$(PYTHON) __main__.py search "$(Q)"

# Suggest tags for a file
tag: $(VENV) check_index
	@if [ -z "$(F)" ]; then \
		echo "$(RED)Error: File path required$(NC)"; \
		echo "Usage: make tag F='path/to/file.md'"; \
		exit 1; \
	fi
	$(PYTHON) __main__.py tag "$(F)"

# Analyze gaps in a file
gaps: $(VENV) check_index
	@if [ -z "$(F)" ]; then \
		echo "$(RED)Error: File path required$(NC)"; \
		echo "Usage: make gaps F='path/to/file.md'"; \
		exit 1; \
	fi
	$(PYTHON) __main__.py gaps "$(F)"

# Find cross-references for a topic
xref: $(VENV) check_index
	@if [ -z "$(T)" ]; then \
		echo "$(RED)Error: Topic required$(NC)"; \
		echo "Usage: make xref T='topic'"; \
		exit 1; \
	fi
	$(PYTHON) __main__.py xref "$(T)"

# Check system health
health: $(VENV)
	$(PYTHON) __main__.py health

# Check if index exists
check_index:
	@if [ ! -d "index/chroma" ]; then \
		echo "$(RED)Error: Index not found$(NC)"; \
		echo "$(YELLOW)Build it first: make build$(NC)"; \
		exit 1; \
	fi

# Auto-tagging
auto-tag-dry: $(VENV) check_index
	@echo "$(BLUE)Auto-tagging all files (DRY RUN)...$(NC)"
	@echo "$(YELLOW)Preview changes without modifying files$(NC)"
	$(PYTHON) __main__.py auto-tag --dry-run --verbose --report auto-tag-preview.json
	@echo ""
	@echo "$(GREEN)✓ Dry run complete. Review report: auto-tag-preview.json$(NC)"

auto-tag: $(VENV) check_index
	@echo "$(BLUE)Auto-tagging all files...$(NC)"
	@echo "$(YELLOW)This will update frontmatter tags in all 294 files$(NC)"
	@read -p "Continue? [y/N] " confirm; \
	if [ "$$confirm" = "y" ]; then \
		$(PYTHON) __main__.py auto-tag --strategy balanced --verbose --report auto-tag-report.json; \
		echo ""; \
		echo "$(GREEN)✓ Auto-tagging complete$(NC)"; \
	else \
		echo "$(YELLOW)Cancelled$(NC)"; \
	fi

tag-validate: $(VENV) check_index
	@echo "$(BLUE)Validating tags against canonical...$(NC)"
	$(PYTHON) __main__.py tag-validate

# Clean up (remove venv and cache)
clean:
	@echo "$(YELLOW)Cleaning...$(NC)"
	rm -rf $(VENV) __pycache__ .pytest_cache *.pyc
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@echo "$(GREEN)✓ Cleaned$(NC)"

# Print current status
status: $(VENV)
	@echo "$(BLUE)System Status:$(NC)"
	@echo ""
	@echo "Environment: $$([ -d $(VENV) ] && echo '$(GREEN)✓ Ready$(NC)' || echo '$(RED)✗ Not set up$(NC)')"
	@echo "Index: $$([ -d index/chroma ] && echo '$(GREEN)✓ Built$(NC)' || echo '$(RED)✗ Not built$(NC)')"
	@$(PYTHON) __main__.py health 2>/dev/null || echo "$(YELLOW)Checking Ollama...$(NC)"

.DEFAULT_GOAL := help

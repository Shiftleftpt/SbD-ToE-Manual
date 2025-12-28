.PHONY: help setup install build rebuild test search clean

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
	@echo "$(BLUE)Manual RAG System - Make Commands$(NC)"
	@echo ""
	@echo "$(GREEN)Setup & Installation (one-time):$(NC)"
	@echo "  make setup              - Full setup: venv + dependencies + index"
	@echo "  make install            - Install/update dependencies only"
	@echo ""
	@echo "$(GREEN)Building & Indexing:$(NC)"
	@echo "  make build              - Build index (advanced chunked indexing)"
	@echo "  make build-simple       - Build simple index (all files at once)"
	@echo "  make rebuild            - Clean and rebuild everything"
	@echo ""
	@echo "$(GREEN)Auto-Tagging Workflow:$(NC)"
	@echo "  make generate-tags      - Generate tag suggestions"
	@echo "  make apply-tags         - Apply approved tag changes"
	@echo ""
	@echo "$(GREEN)Testing & Verification:$(NC)"
	@echo "  make test               - Run all tests (26 tests)"
	@echo "  make test-core          - Run RAG core tests only"
	@echo "  make test-cov           - Run tests with coverage report"
	@echo ""
	@echo "$(GREEN)Utilities:$(NC)"
	@echo "  make clean              - Remove venv and cache"
	@echo "  make activate           - Show activation command"
	@echo ""
	@echo "$(YELLOW)Examples:$(NC)"
	@echo "  $$ make setup                 # First time (full setup)"
	@echo "  $$ make build                 # Build index"
	@echo "  $$ make test                  # Run all tests"
	@echo "  $$ make generate-tags         # Get tag suggestions"

# Full setup (venv + dependencies + index)
setup: $(VENV) install build
	@echo ""
	@echo "$(GREEN)════════════════════════════════════════$(NC)"
	@echo "$(GREEN)✨ Setup Complete! ✨$(NC)"
	@echo "$(GREEN)════════════════════════════════════════$(NC)"
	@echo ""
	@echo "Next steps:"
	@echo "  1. Activate environment:"
	@echo "     source rag_env/bin/activate"
	@echo ""
	@echo "  2. Generate tag suggestions:"
	@echo "     python3 -m rag_tools.workflows.generate_review_report --max-tags 7"
	@echo ""
	@echo "  3. Run tests anytime:"
	@echo "     python3 -m pytest"
	@echo ""

# Create virtual environment
$(VENV):
	@echo "$(BLUE)Creating virtual environment...$(NC)"
	python3 -m venv $(VENV)
	$(PIP) install -q --upgrade pip setuptools wheel
	@echo "$(GREEN)✓ Virtual environment created$(NC)"

# Install/update dependencies
install: $(VENV)
	@echo "$(BLUE)Installing dependencies...$(NC)"
	$(PIP) install -q -r requirements.txt
	@echo "$(GREEN)✓ Dependencies installed$(NC)"

# Build advanced chunked index (recommended)
build: $(VENV)
	@echo "$(BLUE)Building RAG index (advanced chunked)...$(NC)"
	@echo "$(YELLOW)This may take 2-3 minutes...$(NC)"
	$(PYTHON) -m rag_core.indexing.chunked_build
	@echo "$(GREEN)✓ Index built successfully$(NC)"

# Build simple index
build-simple: $(VENV)
	@echo "$(BLUE)Building RAG index (simple)...$(NC)"
	$(PYTHON) -m rag_core.indexing.build
	@echo "$(GREEN)✓ Index built$(NC)"

# Rebuild from scratch
rebuild: clean setup
	@echo "$(GREEN)✓ Rebuild complete$(NC)"

# Generate tag suggestions
generate-tags: $(VENV)
	@echo "$(BLUE)Generating tag suggestions...$(NC)"
	$(PYTHON) -m rag_tools.workflows.generate_review_report --max-tags 7
	@echo "$(GREEN)✓ Review report generated$(NC)"
	@echo "$(YELLOW)Edit the CSV file and change PENDING → OK to approve$(NC)"

# Apply approved tag changes
apply-tags: $(VENV)
	@if [ -z "$(CSV)" ]; then \
		echo "$(RED)Error: CSV file required$(NC)"; \
		echo "Usage: make apply-tags CSV=review_report_*.csv"; \
		exit 1; \
	fi
	@echo "$(BLUE)Applying tag changes from $(CSV)...$(NC)"
	$(PYTHON) -m rag_tools.workflows.apply_review_decisions $(CSV)
	@echo "$(GREEN)✓ Tags applied$(NC)"

# Run all tests
test: $(VENV)
	@echo "$(BLUE)Running all tests...$(NC)"
	$(PYTHON) -m pytest -v
	@echo "$(GREEN)✓ Tests complete$(NC)"

# Run core tests only
test-core: $(VENV)
	@echo "$(BLUE)Running RAG core tests...$(NC)"
	$(PYTHON) -m pytest rag_core/tests/ -v
	@echo "$(GREEN)✓ Core tests complete$(NC)"

# Run tests with coverage
test-cov: $(VENV)
	@echo "$(BLUE)Running tests with coverage...$(NC)"
	$(PYTHON) -m pytest --cov=rag_core --cov=rag_tools --cov-report=html
	@echo "$(GREEN)✓ Coverage report: htmlcov/index.html$(NC)"

# Clean up
clean:
	@echo "$(YELLOW)Cleaning...$(NC)"
	rm -rf $(VENV) __pycache__ .pytest_cache *.pyc
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@echo "$(GREEN)✓ Cleaned$(NC)"

# Show activation command
activate:
	@echo "To activate the environment, run:"
	@echo "  source rag_env/bin/activate"

.DEFAULT_GOAL := help

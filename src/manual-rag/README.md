# Manual RAG - Semantic Search & Auto-Tagging System

Intelligent RAG (Retrieval-Augmented Generation) system for the SbD-ToE manual with chapter-aware semantic search and automatic tag suggestions.

## 🎯 Features

- **Chunked JSONL Indexing**: Document chunking with metadata (chapter, domain, section)
- **Chapter-Aware Search**: 100% precision - searches prioritize same-chapter content
- **Auto-Tagging**: Combine semantic search + pattern matching + existing tags
- **Smart Tag Selection**: Limit to ~7 tags for Docusaurus readability
- **Two-Step Approval Workflow**: Review suggestions, approve/reject, apply

## 📁 Organization

```
manual-rag/
├── rag_core/              # RAG Infrastructure (CREATE indexes & search)
│   ├── tests/             # Unit tests (26 passing)
│   ├── indexing/          # Build indexes
│   ├── query/             # Semantic search
│   ├── local_llm/         # Optional LLM integration
│   ├── config.py          # Configuration (single source of truth)
│   └── README.md          # Infrastructure details
│
├── rag_tools/             # RAG Usage (USE RAG for tasks)
│   ├── tagging/           # Auto-tagging system
│   │   ├── tests/         # Tagging tests
│   │   ├── data/          # canonical-tags.yml
│   │   ├── *.py
│   │   └── README.md      # Auto-tagging documentation
│   ├── workflows/         # Business workflows
│   │   ├── generate_review_report.py
│   │   ├── apply_review_decisions.py
│   │   └── tests/         # Workflow tests (ready)
│   ├── utils/             # Utilities
│   │   ├── smart_tag_selection.py
│   │   └── tests/         # Utils tests (ready)
│   └── README.md          # Tools documentation
│
├── pytest.ini             # Global test configuration
├── conftest.py            # Pytest fixtures
└── requirements.txt       # Dependencies
```

## 🚀 Quick Start

### Setup Environment
```bash
# Create and activate virtual environment
python3 -m venv rag_env
source rag_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Optional: Start Ollama for LLM fallback
ollama pull mistral
ollama serve &
```

### Build Index
```bash
# Simple indexing (all files at once)
python3 -m rag_core.indexing.build

# Advanced chunked indexing (with JSONL dataset)
python3 -m rag_core.indexing.chunked_build
```

### Run Auto-Tagging Workflow
```bash
# 1. Generate tag suggestions
python3 -m rag_tools.workflows.generate_review_report --max-tags 7

# 2. Review the CSV (edit and mark PENDING → OK)

# 3. Apply approved changes
python3 -m rag_tools.workflows.apply_review_decisions review_report_TIMESTAMP.csv
```

## 🧪 Testing

```bash
# All tests
python3 -m pytest

# RAG core tests only (26 tests)
python3 -m pytest rag_core/tests/ -v

# Tagging tests only
python3 -m pytest rag_tools/tagging/tests/ -v

# With coverage report
python3 -m pytest --cov=rag_core --cov=rag_tools --cov-report=html
```

## 📊 Results

- **276 files** analyzed
- **252 files** with suggestions (91.3%)
- **+405 tags** added, **-74** removed = **+331 net**
- **100%** chapter accuracy in search tests

## 📚 Documentation

- **[rag_core/README.md](rag_core/README.md)** - Infrastructure details & API
- **[rag_tools/README.md](rag_tools/README.md)** - Tools & workflows
- **[rag_tools/tagging/README.md](rag_tools/tagging/README.md)** - Auto-tagging system
- **[rag_core/config.py](rag_core/config.py)** - Configuration options

## 📦 Dependencies

- `chromadb` - Vector database (embedded)
- `sentence-transformers` - Embeddings
- `pyyaml` - YAML parsing
- `pytest` - Testing framework
- `ollama` - Optional LLM client

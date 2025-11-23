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

### Setup Environment (First Time)
```bash
cd src/manual-rag
make setup
```

**⏱️ This takes ~10 minutes and does everything:**
- Creates virtual environment
- Installs dependencies
- Builds RAG index
- Runs tests to verify

### Activate Environment (Every Session)
```bash
source rag_env/bin/activate
```

### Run Auto-Tagging Workflow
```bash
# 1. Generate tag suggestions
make generate-tags

# 2. Review the CSV (edit and mark PENDING → OK)

# 3. Apply approved changes
make apply-tags CSV=review_report_*.csv
```

## 🧪 Testing

```bash
# All tests
make test

# RAG core tests only (26 tests)
make test-core

# With coverage report
make test-cov
```

## 📊 Results

- **276 files** analyzed
- **252 files** with suggestions (91.3%)
- **+405 tags** added, **-74** removed = **+331 net**
- **100%** chapter accuracy in search tests

## 📚 Documentation

- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Setup instructions
- **[EXECUTION_GUIDE.md](EXECUTION_GUIDE.md)** - Tagging workflow guide
- **[rag_core/README.md](rag_core/README.md)** - Infrastructure API
- **[rag_tools/README.md](rag_tools/README.md)** - Tools & workflows
- **[rag_tools/tagging/README.md](rag_tools/tagging/README.md)** - Auto-tagging system
- **[rag_core/config.py](rag_core/config.py)** - Configuration options

## 📦 Dependencies

- `chromadb` - Vector database (embedded)
- `sentence-transformers` - Embeddings
- `pyyaml` - YAML parsing
- `pytest` - Testing framework
- `ollama` - Optional LLM client

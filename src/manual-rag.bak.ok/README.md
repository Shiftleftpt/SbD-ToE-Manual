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
│   ├── tagging_tools/     # Tag suggestion & comparison tools
│   │   ├── data/          # Canonical tags & embeddings
│   │   ├── reports/       # Generated reports
│   │   ├── suggest_tags.py           # Main tagging script
│   │   ├── suggest_tags_canonical.py # Canonical-based tagging
│   │   ├── compare_tags.py           # Tag comparison
│   │   ├── generate_report.py        # Report generation
│   │   └── README.md                 # Tagging documentation
│   ├── utils/             # Utilities
│   │   └── smart_tag_selection.py    # Tag selection logic
│   └── README.md          # Tools documentation
│
├── ollama/                # Ollama LLM setup
│   ├── OLLAMA_GUIDE.md    # Setup guide
│   └── install_ollama.sh  # Installation script
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
# Generate tag suggestions for a chapter
python3 rag_tools/tagging_tools/suggest_tags.py "002-cross-check" --top-n 15

# Or with canonical tag matching
python3 rag_tools/tagging_tools/suggest_tags_canonical.py "010-sbd" --subfolder "04-arquitetura"

# Compare tag suggestions
python3 rag_tools/tagging_tools/compare_tags.py

# See full options in rag_tools/tagging_tools/README.md
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

- **[rag_core/README.md](rag_core/README.md)** - Infrastructure API
- **[rag_tools/README.md](rag_tools/README.md)** - Tools overview
- **[rag_tools/tagging_tools/README.md](rag_tools/tagging_tools/README.md)** - Tagging tools guide
- **[ollama/OLLAMA_GUIDE.md](ollama/OLLAMA_GUIDE.md)** - Ollama setup
- **[rag_core/config.py](rag_core/config.py)** - Configuration options

## 📦 Dependencies

- `chromadb` - Vector database (embedded)
- `sentence-transformers` - Embeddings
- `pyyaml` - YAML parsing
- `pytest` - Testing framework
- `ollama` - Optional LLM client

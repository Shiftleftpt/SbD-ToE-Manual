"""RAG Core - Complete Architecture Overview

## 📦 Package Structure

```
rag_core/                          # Core RAG Infrastructure
├── __init__.py                   # Exports: ManualIndexer, SemanticSearch, OllamaClient
├── config.py                     # Configuration: paths, parameters, constants
├── metadata.py                   # NEW: ChaptersMetadata (structure parsing)
│
├── indexing/                     # Document Indexing (Create RAG)
│   ├── __init__.py              # Exports: ManualIndexer, DocumentChunker, JSONLDatasetBuilder, ChunkedIndexBuilder
│   ├── build.py                 # CLI: python -m rag_core.indexing.build
│   ├── chunked.py               # NEW: DocumentChunker, JSONLDatasetBuilder, ChunkedIndexBuilder
│   └── chunked_build.py         # NEW: CLI: python -m rag_core.indexing.chunked_build
│
├── query/                        # Semantic Search (Query RAG)
│   ├── __init__.py              # SemanticSearch - only search() method
│   └── [no other methods]
│
└── local_llm/                    # LLM Integration (Optional enhancement)
    └── __init__.py              # OllamaClient for chat/generation

rag_tools/                        # RAG Usage (Tools & Workflows)
├── tagging/                      # AUTO-TAGGING workflow
│   ├── _tags.py                 # CanonicalTags (from rag_core.config)
│   ├── _auto_tagger.py          # AutoTagger (imports from rag_core.config)
│   └── _file_updater.py         # FileTagUpdater
│
├── workflows/                    # High-level workflows
│   ├── build_chunked_index.py   # DEPRECATED (delegates to rag_core)
│   ├── generate_review_report.py
│   └── apply_review_decisions.py
│
└── utils/                        # Utilities
    └── smart_tag_selection.py

tests/rag/                        # Test Suite
├── conftest.py                  # NEW: Pytest fixtures (isolated test data)
├── test_indexing.py             # NEW: Tests for simple indexing
├── test_chunked_indexing.py     # NEW: Tests for chunked indexing
└── README_TESTING.md            # NEW: Testing guide
```

## 🎯 Core Components

### 1. Indexing - Two Strategies

#### Strategy 1: Simple Indexing (Fast, Easy)
```python
from rag_core.indexing import ManualIndexer

indexer = ManualIndexer(manual_root, index_dir)
stats = indexer.index_all(force_rebuild=False)
# Stores at: index_dir/chroma/
# Collection: "manual"
```

#### Strategy 2: Chunked Indexing (Advanced, Better Retrieval)
```python
from rag_core.indexing.chunked import JSONLDatasetBuilder, ChunkedIndexBuilder

# Step 1: Build JSONL dataset with chunks
dataset_builder = JSONLDatasetBuilder(manual_root, index_dir)
jsonl_path = dataset_builder.build_dataset()

# Step 2: Build Chroma index from chunks
index_builder = ChunkedIndexBuilder(index_dir)
stats = index_builder.build_from_jsonl(jsonl_path)
# Stores at: index_dir/chroma_chunked/
# Collection: "manual_chunked"
```

### 2. Querying - Semantic Search
```python
from rag_core import SemanticSearch

search = SemanticSearch()  # Uses INDEX_DIR from config
results = search.search("query text", top_k=5)
# Returns: List of similar documents
```

### 3. LLM Enhancement - Optional
```python
from rag_core import OllamaClient

llm = OllamaClient()
response = llm.generate("prompt")  # Needs ollama serve running
```

### 4. Metadata Parsing - Automatic
```python
from rag_core.metadata import ChaptersMetadata

metadata = ChaptersMetadata.parse_path("010-sbd-manual/02-requisitos-seguranca/intro.md")
# Returns:
# {
#   "chapter": "010-sbd-manual",
#   "chapter_name": "Security by Design Manual",
#   "section": "02-requisitos-seguranca",
#   "domain": "Security Requirements",
#   ...
# }
```

## 📂 Storage Structure

```
index/
├── chroma/                  # Simple indexing (ManualIndexer)
│   ├── data/               # Vector embeddings
│   ├── metadata/           # Document metadata
│   └── [...chroma files]
│
├── chroma_chunked/         # Chunked indexing (ChunkedIndexBuilder)
│   ├── data/               # Chunk vectors
│   ├── metadata/           # Chunk metadata
│   └── [...chroma files]
│
└── manual_chunks.jsonl     # JSONL dataset (intermediate output)
```

**Key**: Two indexes don't interfere with each other!

## 🧪 Testing

### Fixtures (Isolated Test Data)
```python
@pytest.fixture
def temp_manual_root():
    # Creates temporary markdown files
    # Never touches production
    
@pytest.fixture
def temp_index_dir():
    # Creates temporary index directory
    # Isolated from production index/
```

### Test Coverage

| Component | Tests | Status |
|-----------|-------|--------|
| ManualIndexer | 8 tests | ✅ Complete |
| DocumentChunker | 5 tests | ✅ Complete |
| ChaptersMetadata | 3 tests | ✅ Complete |
| JSONLDatasetBuilder | 4 tests | ✅ Complete |
| ChunkedIndexBuilder | 3 tests | ✅ Complete |
| Integration | 2 tests | ✅ Complete |

### Run Tests
```bash
# All tests
pytest tests/rag/

# With coverage
pytest tests/rag/ --cov=rag_core --cov-report=html

# Specific test
pytest tests/rag/test_indexing.py -v
```

## 🔄 Workflow Examples

### Example 1: Build Production Index
```bash
# Simple indexing (fast)
python build_index.py

# Or chunked indexing (better retrieval)
python -m rag_core.indexing.chunked_build
```

### Example 2: Query the Index
```python
from rag_core import SemanticSearch

search = SemanticSearch()
results = search.search("security requirements", top_k=10)

for result in results:
    print(f"Title: {result['title']}")
    print(f"Similarity: {result['similarity']:.1%}")
    print(f"Content: {result['content'][:200]}...")
```

### Example 3: Auto-Tag Files
```python
from rag_tools.tagging import AutoTagger
from rag_core.config import MANUAL_ROOT

auto_tagger = AutoTagger()
tags = auto_tagger.suggest_tags(
    file_path=MANUAL_ROOT / "010-sbd-manual/02-requisitos-seguranca/intro.md",
    top_k=5
)
```

## 🛡️ Safety Features

### 1. Production Data Protection
- Tests use isolated temporary directories
- Different Chroma directories for different indexes
- Easy to restore from backup

### 2. Validation
- Frontmatter parsing validates YAML
- Chunk size configurable
- Statistics tracked for every operation

### 3. Isolation
```python
# These don't interfere:
- Simple indexing (chroma/)
- Chunked indexing (chroma_chunked/)
- Auto-tagging (reads from core, writes to files)
```

## 📊 Performance

| Operation | Time | Notes |
|-----------|------|-------|
| Index 100 files | ~20-30s | Depends on model |
| Query | ~100ms | Semantic search |
| Chunk large doc | ~1s | Overlap processing |
| Build JSONL | ~15-20s | All documents |
| Rebuild with chunks | ~1-2min | Full pipeline |

## 📋 Checklists

### Before Running in Production
- [ ] Run tests: `pytest tests/rag/`
- [ ] Check config: `python -c "from rag_core.config import *; print('OK')"`
- [ ] Verify paths: `ls -la index/`
- [ ] Test search: `python -m manual_rag search "test query"`

### Troubleshooting

**Problem**: "No such file or directory: index/chroma"
```bash
# Solution: Build index
python build_index.py
```

**Problem**: "Embedding model not found"
```bash
# Solution: Download model (happens automatically)
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"
```

**Problem**: "OllamaClient connection refused"
```bash
# Solution: Ollama is optional, start it if needed
ollama serve
# In another terminal:
ollama pull mistral
```

## 🔗 Dependencies

### Required
- `chromadb` - Vector database
- `sentence-transformers` - Embedding model
- `pyyaml` - Frontmatter parsing

### Optional
- `ollama` - LLM integration (for enhancement only)
- `pytest` - Testing

### Install
```bash
pip install chromadb sentence-transformers pyyaml
pip install pytest pytest-cov  # for testing
```

## 📚 Documentation Files

- `CHROMA_ARCHITECTURE.md` - Vector database deep dive
- `tests/rag/README_TESTING.md` - Testing guide
- This file - Architecture overview
"""

# rag_core - RAG Infrastructure

Core library for building and querying RAG indexes. This module contains everything needed to **CREATE** semantic search capabilities.

## 🏗️ Architecture

### Components

#### 1. **Indexing** (`indexing/`)
- `build.py` - Simple manual indexing (entry point: `python3 -m rag_core.indexing.build`)
- `chunked.py` - Advanced document chunking with metadata
  - `DocumentChunker` - Split documents into semantic chunks
  - `JSONLDatasetBuilder` - Create JSONL datasets with metadata
  - `ChunkedIndexBuilder` - Build Chroma vector indexes
- `chunked_build.py` - Advanced indexing CLI (entry point: `python3 -m rag_core.indexing.chunked_build`)

#### 2. **Query** (`query/`)
- `SemanticSearch` - Chapter-aware vector search
  - `search(query, n_results)` - Find similar documents
  - Uses Chroma embeddings with sentence-transformers

#### 3. **Local LLM** (`local_llm/`)
- `OllamaClient` - Optional fallback LLM integration
  - Requires Ollama running locally
  - Used by tagging workflows

#### 4. **Configuration** (`config.py`)
- Single source of truth for all paths and parameters
- Key settings:
  - `MANUAL_DIR` - Source markdown files
  - `INDEX_DIR` - Where Chroma index is stored
  - `DATASET_DIR` - JSONL datasets
  - `TAGS_FILE` - Canonical tags reference

#### 5. **Metadata** (`metadata.py`)
- `ChaptersMetadata` - Parse document structure
  - Extract chapter/domain/section from frontmatter
  - Organize documents hierarchically

## 🔧 Building Indexes

### Simple Indexing
```bash
python3 -m rag_core.indexing.build
```
Creates a basic Chroma index from all markdown files.

### Advanced Chunked Indexing
```bash
python3 -m rag_core.indexing.chunked_build
```
Advanced pipeline:
1. Read all markdown files
2. Extract frontmatter (chapter, domain, tags, etc.)
3. Split into semantic chunks (~500 tokens each)
4. Create JSONL dataset with metadata
5. Build Chroma vector index
6. Generate statistics

## 🔍 Using Semantic Search

```python
from rag_core.query import SemanticSearch

# Initialize searcher
search = SemanticSearch()

# Search for similar content
results = search.search(
    query="security requirements",
    n_results=5
)

for result in results:
    print(f"File: {result['file']}")
    print(f"Chapter: {result['chapter']}")
    print(f"Score: {result['score']}")
    print(f"Content: {result['content'][:200]}...")
```

## 🧪 Testing

### Run Tests
```bash
# All RAG core tests (26 tests)
python3 -m pytest rag_core/tests/ -v

# Specific test file
python3 -m pytest rag_core/tests/test_indexing.py -v
python3 -m pytest rag_core/tests/test_chunked_indexing.py -v

# With coverage
python3 -m pytest rag_core/tests/ --cov=rag_core --cov-report=html
```

### Test Structure

```
rag_core/tests/
├── conftest.py              # Shared fixtures
├── test_indexing.py         # Manual indexing (8 tests)
└── test_chunked_indexing.py # Chunked pipeline (18 tests)
```

**Test Coverage:**
- ✅ Index creation and persistence
- ✅ Document parsing and chunking
- ✅ Metadata extraction
- ✅ Embedding generation
- ✅ Search functionality
- ✅ Temporary directory cleanup

## ⚙️ Configuration

Edit `rag_core/config.py` to customize:

```python
# Paths
MANUAL_DIR = ...        # Source markdown files
INDEX_DIR = ...         # Chroma index storage
DATASET_DIR = ...       # JSONL datasets
TAGS_FILE = ...         # Canonical tags

# Search parameters
CHUNK_SIZE = 500        # Tokens per chunk
CHUNK_OVERLAP = 50      # Overlap between chunks
EMBEDDING_MODEL = ...   # Sentence transformer model
CHROMA_COLLECTION = ... # Collection name
```

## 📦 Dependencies

- `chromadb` - Vector database (embedded)
- `sentence-transformers` - Embeddings
- `pyyaml` - YAML parsing
- `pytest` - Testing framework
- `ollama` - Optional LLM client

## 🔗 See Also

- [Main README](../README.md) - Project overview
- [rag_tools README](../rag_tools/README.md) - How to use RAG
- [rag_core/config.py](config.py) - Configuration details

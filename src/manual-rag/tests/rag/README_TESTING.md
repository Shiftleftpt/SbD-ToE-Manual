"""RAG Core Testing Guide

## Setup Requirements

### Chroma
- **No setup needed!** Chroma can work in two modes:
  1. **In-Memory** (ephemeral): Data lost on restart - good for tests
  2. **Persistent** (file-based): Data stored in directory - production ready
  
- Our code uses `PersistentClient` which stores data in `index/chroma/` directory
- Tests use isolated `temp_index_dir` to avoid corrupting production data

### Ollama (for LLM features)
- **OPTIONAL** - Not needed for indexing/chunking tests
- Only needed for RAG queries that use the LLM
- Start with: `ollama serve` (in separate terminal)
- Models available: mistral, llama, etc.

## Running Tests

### Install test dependencies
```bash
pip install pytest pytest-cov
```

### Run all tests
```bash
pytest tests/rag/
```

### Run specific test file
```bash
pytest tests/rag/test_indexing.py
pytest tests/rag/test_chunked_indexing.py
```

### Run with verbose output
```bash
pytest tests/rag/ -v
```

### Run with coverage report
```bash
pytest tests/rag/ --cov=rag_core --cov-report=html
```

## Test Isolation Strategy

### Problem: Tests could corrupt production index
- Production index at `index/chroma/`
- Tests create temporary directories
- Each test gets fresh isolated environment

### Solution: Fixtures

#### `temp_manual_root`
- Creates temporary directory with test markdown files
- Includes proper chapter structure and frontmatter
- Cleaned up after test

#### `temp_index_dir`
- Temporary directory for index outputs
- Isolated from production `index/` directory
- Cleaned up after test

#### `temp_chroma_dir`
- For tests that specifically need Chroma isolation
- Separate Chroma storage
- Never touches production

### Example test using fixtures:
```python
def test_indexing(temp_manual_root, temp_index_dir):
    # temp_manual_root and temp_index_dir are isolated directories
    # Production data is never touched
    indexer = ManualIndexer(temp_manual_root, temp_index_dir)
    stats = indexer.index_all()
    assert stats["indexed"] > 0
```

## Separation: Simple vs Chunked Indexing

### Simple Indexing (ManualIndexer)
- Stores: `temp_index_dir/chroma/`
- Collection: `"manual"`
- Full documents, no chunking
- Fast, simple

### Chunked Indexing (ChunkedIndexBuilder)
- Stores: `temp_index_dir/chroma_chunked/`
- Collection: `"manual_chunked"`
- Split documents, rich metadata
- Slower, more accurate retrieval

**They don't interfere with each other** - different directories, different collections!

### Test proof of isolation:
```python
def test_isolation_from_simple_indexing():
    # Both can exist in same temp_index_dir
    ManualIndexer(temp_manual_root, temp_index_dir).index_all()
    ChunkedIndexBuilder(temp_index_dir).build_from_jsonl(jsonl_path)
    
    # Both work independently
    assert (temp_index_dir / "chroma").exists()
    assert (temp_index_dir / "chroma_chunked").exists()
```

## What Tests Cover

### test_indexing.py
- ✅ ManualIndexer initialization
- ✅ File reading with frontmatter parsing
- ✅ Indexing all files
- ✅ Chroma collection population
- ✅ Force rebuild clearing index
- ✅ Embedding creation
- ✅ .2review file exclusion
- ✅ Persistent storage

### test_chunked_indexing.py
- ✅ DocumentChunker with overlap
- ✅ Small/large content chunking
- ✅ Frontmatter extraction
- ✅ Chunk metadata creation
- ✅ ChaptersMetadata parsing for all chapter types
- ✅ JSONL dataset generation and structure
- ✅ ChunkedIndexBuilder initialization and indexing
- ✅ Separation of simple vs chunked indexes
- ✅ Full pipeline integration

## Debugging Tests

### See what test data looks like:
```python
def test_debug_fixtures(temp_manual_root):
    # List all files created
    for f in temp_manual_root.rglob("*.md"):
        print(f)
        print(f.read_text())
```

### Check Chroma collection contents:
```python
def test_inspect_index(temp_manual_root, temp_index_dir):
    indexer = ManualIndexer(temp_manual_root, temp_index_dir)
    indexer.index_all()
    
    # See all documents
    results = indexer.collection.get(include=["documents", "metadatas"])
    for doc_id, doc, meta in zip(results["ids"], results["documents"], results["metadatas"]):
        print(f"ID: {doc_id}")
        print(f"Title: {meta['title']}")
        print(f"Content preview: {doc[:100]}...")
```

## Production Data Safety

### How to avoid corrupting production index:
1. ✅ **Tests use temp directories** - handled by fixtures
2. ✅ **Different Chroma paths** - `chroma/` vs `chroma_chunked/`
3. ✅ **Different collections** - `"manual"` vs `"manual_chunked"`

### Worst case: Manually restore
```bash
# If you accidentally cleared production index:
python build_index.py --rebuild
python -m rag_core.indexing.chunked_build
```

## Next Steps

1. Run the tests to ensure everything works:
   ```bash
   pytest tests/rag/ -v
   ```

2. Add more tests for:
   - SemanticSearch (query tests)
   - OllamaClient (LLM integration)
   - Error handling and edge cases
   - Performance benchmarks

3. Set up CI/CD to run tests on every commit
"""

# This is a docstring-only module with testing documentation

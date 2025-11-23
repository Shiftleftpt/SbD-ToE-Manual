"""RAG Core Testing Guide

## Quick Start

### Run RAG tests only (from your module)
```bash
python run_tests.py rag
python run_tests.py rag -v           # Verbose
python run_tests.py rag --coverage   # With coverage report
```

### Direct pytest
```bash
pytest rag_core/tests/
pytest rag_core/tests/ -v
pytest rag_core/tests/ --cov=rag_core --cov-report=html
```

## Structure

Tests live inside their module:
```
rag_core/
├── __init__.py
├── config.py
├── metadata.py
├── indexing/
├── query/
├── local_llm/
└── tests/                  # Tests INSIDE the module!
    ├── conftest.py         # rag_core fixtures
    ├── test_indexing.py    # ManualIndexer tests
    └── test_chunked_indexing.py  # ChunkedIndexBuilder tests
```

## Test Isolation

**Key**: Tests don't corrupt production data.

### How?
1. **Temporary directories**: Each test gets `/tmp/...`
2. **conftest.py**: Provides isolated fixtures
3. **Cleanup**: Automatic after each test

### Fixtures Available in rag_core/tests/conftest.py

```python
# Created temporarily, cleaned up after test
temp_manual_root   # Temporary markdown files with structure
temp_index_dir     # Temporary index directory
temp_chroma_dir    # Temporary Chroma storage
```

## What's Tested

### Simple Indexing (ManualIndexer)
- ✅ Initialization
- ✅ File reading with frontmatter
- ✅ Full indexing pipeline
- ✅ Chroma collection population
- ✅ Persistence
- ✅ Force rebuild

### Chunked Indexing
- ✅ Document chunking with overlap
- ✅ Metadata parsing (ChaptersMetadata)
- ✅ JSONL dataset generation
- ✅ Chroma index building
- ✅ Isolation from simple indexing

### Integration
- ✅ Full pipeline
- ✅ Both strategies coexist

## Coverage

```bash
# Generate coverage report for rag_core
python run_tests.py rag --coverage

# View report
open htmlcov/index.html
```

## Adding New Tests

1. **Create in rag_core/tests/**: `test_*.py`
2. **Use fixtures**: `temp_manual_root`, `temp_index_dir`
3. **Add docstring**: Explain what's being tested

Example:
```python
# rag_core/tests/test_new_feature.py

def test_feature_works(temp_manual_root, temp_index_dir):
    \"\"\"Test that feature works\"\"\"
    indexer = ManualIndexer(temp_manual_root, temp_index_dir)
    result = indexer.do_something()
    assert result is not None
```

## Dependencies

Already in requirements.txt:
- pytest>=7.0.0
- pytest-cov>=4.0.0

## Markers

Tests are automatically marked by location:
```bash
# Run only rag_core tests
pytest -m rag rag_core/tests/

# Run only tagging tests  
pytest -m tagging rag_tools/tests/
```
"""

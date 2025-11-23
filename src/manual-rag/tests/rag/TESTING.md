"""RAG Core Testing Guide

## Quick Start

### Run RAG tests only (context-isolated)
```bash
python run_tests.py rag
python run_tests.py rag -v           # Verbose
python run_tests.py rag --coverage   # With coverage report
```

### Run tagging tests only
```bash
python run_tests.py tagging
```

### Run all tests
```bash
python run_tests.py
pytest tests/rag/       # Direct pytest
```

## Structure

Tests are organized by context:
```
tests/
├── rag/                     # RAG CORE tests only
│   ├── conftest.py         # RAG fixtures (temp_manual_root, temp_index_dir)
│   ├── test_indexing.py    # ManualIndexer tests
│   └── test_chunked_indexing.py  # ChunkedIndexBuilder tests
│
└── tagging/                # TAGGING tests only
    └── conftest.py         # Tagging fixtures (separate from rag)
```

## Test Isolation

**Key Principle**: Tests don't corrupt production data.

### How?
1. **Separate directories**: Each test gets temp directories (`/tmp/...`)
2. **Separate conftest.py**: `tests/rag/conftest.py` vs `tests/tagging/conftest.py`
3. **Separate markers**: `@pytest.mark.rag` vs `@pytest.mark.tagging`

### Fixtures Available in tests/rag/

```python
# Created temporarily, cleaned up after test
temp_manual_root   # Temporary markdown files with structure
temp_index_dir     # Temporary index directory
temp_chroma_dir    # Temporary Chroma storage
```

## What's Tested

### Simple Indexing (ManualIndexer)
- ✅ Initialization and configuration
- ✅ File reading with frontmatter
- ✅ Full indexing pipeline
- ✅ Chroma collection population
- ✅ Persistence to disk
- ✅ Force rebuild

### Chunked Indexing
- ✅ Document chunking with overlap
- ✅ Metadata parsing (ChaptersMetadata)
- ✅ JSONL dataset generation
- ✅ Chroma index building
- ✅ Isolation from simple indexing

### Integration
- ✅ Full pipeline (data → JSONL → Chroma)
- ✅ Both indexing strategies coexist

## Context Separation (Pytest Markers)

```bash
# Run only rag tests
pytest -m rag

# Run only tagging tests
pytest -m tagging

# Run both (default)
pytest
```

## Production Data Safety

✅ Tests use temporary directories
✅ No test modifies `index/chroma` or `index/chroma_chunked`
✅ No test modifies canonical-tags.yml
✅ Easy to run tests repeatedly without side effects

## Troubleshooting

**"pytest: command not found"**
```bash
pip install -r requirements.txt
```

**"No such file or directory: tests/rag"**
```bash
# Make sure you're in the right directory
cd src/manual-rag
python run_tests.py rag
```

**"ModuleNotFoundError: rag_core"**
```bash
# Make sure rag_core is in Python path
cd src/manual-rag
python run_tests.py rag
```

## Coverage

```bash
# Generate coverage report
python run_tests.py rag --coverage

# View report
open htmlcov/index.html
```

## Adding New Tests

1. **Create in correct folder**: `tests/rag/test_*.py`
2. **Use RAG fixtures**: `temp_manual_root`, `temp_index_dir`
3. **Add docstring**: Explain what's being tested
4. **Mark as RAG**: Automatically done by `conftest.py`

Example:
```python
# tests/rag/test_new_feature.py

def test_feature_works(temp_manual_root, temp_index_dir):
    \"\"\"Test that new feature works correctly\"\"\"
    indexer = ManualIndexer(temp_manual_root, temp_index_dir)
    result = indexer.do_something()
    assert result is not None
```

## Dependencies

- pytest (automatic with `pip install -r requirements.txt`)
- pytest-cov (for coverage reports)
"""

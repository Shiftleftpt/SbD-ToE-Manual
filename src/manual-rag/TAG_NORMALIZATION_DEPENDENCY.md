# Tag Normalization Dependency

## Status: REQUIRED ✅

The `tag-normalization` folder at `src/tag-normalization` is **actively used** by the production manual-rag system and should **NOT be removed**.

## Why It's Needed

### Production Dependencies

1. **`manual_rag/tagging/__init__.py`**
   - Uses: `CanonicalTags` class
   - Purpose: Load, validate, and normalize tag names
   - Usage: Tag validation, alias resolution, canonical name lookup

2. **`tools/build_chunked_index.py`**
   - Uses: `TAGS_FILE` from config
   - Purpose: Load canonical tags for index building
   - Usage: Tag validation during chunk indexing

3. **`__main__.py`**
   - Uses: `CanonicalTags` class
   - Purpose: Tag validation when applying manual changes

### Data Resource

- **`canonical-tags.yml`**: Authoritative source of:
  - Valid tag names
  - Tag aliases (e.g., Portuguese variants)
  - Tag descriptions
  - Tag metadata

## Current Structure

```
src/
├── tag-normalization/        # REQUIRED - Do not remove
│   ├── canonical-tags.yml    # Authoritative tag definitions
│   ├── tag_system/           # Tag system implementation
│   ├── legacy/               # Legacy experiments
│   └── ...
├── manual-rag/               # Main RAG system
│   ├── manual_rag/           # Core library
│   ├── tools/                # Production tools
│   ├── scripts/              # Tests & utilities
│   └── ...
```

## Usage Pattern

```python
# In manual_rag/config.py:
TAGS_FILE = REPO_ROOT / "src" / "tag-normalization" / "canonical-tags.yml"

# In manual_rag/tagging/__init__.py:
from ..config import TAGS_FILE

class CanonicalTags:
    def __init__(self, tags_file: Path = TAGS_FILE):
        self.tags = self._load_tags()
```

## Legacy Code References

These legacy scripts import from `tag-normalization` but are not used in production:

- ❌ `scripts/legacy/run_extended_comparison.py`
- ❌ `scripts/legacy/analyze_recall_variance.py`
- ❌ `scripts/legacy/auto_tag_corpus.py`
- ❌ `scripts/legacy/run_four_way_comparison.py`
- ⚠️ `scripts/utils/smart_tag_selection.py` - Imports unused, can be cleaned
- ⚠️ `scripts/testing/test_strategies.py` - Legacy test
- ⚠️ `scripts/testing/test_monitorizacao.py` - Legacy test

## Recommendation

**Keep tag-normalization as external dependency**. It provides:
- ✅ Centralized tag definitions
- ✅ Reusability for other projects
- ✅ Clear separation of concerns
- ✅ Easier maintenance of tag taxonomy

The manual-rag system correctly depends on it through:
- Import: `from ..config import TAGS_FILE`
- Access: `CanonicalTags()` class

This is a well-designed dependency relationship.

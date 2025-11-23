# Manual RAG - Modular Structure

## Overview

The Manual RAG system is organized into **4 modular layers** with clear separation of concerns:

```
manual-rag/
├── rag_core/              # Layer 1: RAG Infrastructure (Build)
│   ├── indexing/          # Build and manage vector index
│   ├── query/             # Query index for similar documents
│   └── local_llm/         # Interface to local LLM
│
├── rag_tools/             # Layer 2-4: RAG-Based Operations
│   ├── tagging/           # Layer 3: Tag Management (Suggestions, Normalization)
│   │   ├── _tags.py       # Canonical tag loading and normalization
│   │   ├── _auto_tagger.py # RAG+Pattern-based auto-tagging
│   │   └── _file_updater.py # YAML frontmatter I/O
│   ├── workflows/         # Layer 4: High-level workflows (CLIs)
│   │   ├── build_chunked_index.py
│   │   ├── generate_review_report.py
│   │   └── apply_review_decisions.py
│   └── utils/             # Utility functions
│       ├── batch.py
│       └── smart_tag_selection.py
│
├── tests/                 # Testing
│   ├── rag/               # Tests for RAG infrastructure
│   └── tagging/           # Tests for tagging workflows
│
├── results/               # Outputs (git-ignored)
│   └── .gitignore         # Excludes *.csv, *.json, *.db
│
├── manual_rag/            # Configuration package
│   ├── config.py          # Centralized configuration
│   └── __init__.py
│
├── canonical-tags.yml     # Tag vocabulary (ESSENTIAL)
├── requirements.txt       # Python dependencies
└── README.md
```

---

## Layer Responsibilities

### **Layer 1: RAG Infrastructure** (`rag_core/`)

**Purpose**: Build and manage the semantic search index

| Module | Class | Responsibility |
|--------|-------|-----------------|
| `indexing/` | `ManualIndexer` | Reads markdown files, generates embeddings, stores in Chroma |
| `query/` | `SemanticSearch` | Queries index for similar documents, chapter-aware ranking |
| `local_llm/` | `OllamaClient` | Interface to local Ollama LLM for text generation |

**Entry Point**: `rag_tools/workflows/build_chunked_index.py`

---

### **Layer 2-4: RAG-Based Operations** (`rag_tools/`)

#### **Layer 2: Tag Management** (`rag_tools/tagging/`)

Responsible for tag-related operations:

| Module | Class | Responsibility |
|--------|-------|-----------------|
| `_tags.py` | `CanonicalTags` | Load YAML tag vocabulary, validate, normalize aliases |
| `_auto_tagger.py` | `AutoTagger` | Combine RAG + regex patterns to suggest tags |
| `_auto_tagger.py` | `TagSuggestion` | Data class for tag suggestions with confidence |
| `_file_updater.py` | `FileTagUpdater` | Read/write YAML frontmatter, manage tag lists |

**Key Methods**:
```python
# Get tag suggestions
auto_tagger = AutoTagger()  # Uses RAG internally
suggestions = auto_tagger.suggest_tags(file_path, content, title, existing_tags)
# Returns: List[TagSuggestion] with confidence + reasoning

# Merge with threshold
final_tags, new_tags = auto_tagger.merge_tags(existing, suggestions, strategy='balanced')
# Returns: (sorted list of final tags, list of newly added tags)

# Write tags to file
FileTagUpdater.update_tags(Path("docs/file.md"), final_tags)
```

#### **Layer 3: Workflows** (`rag_tools/workflows/`)

High-level CLI scripts for production operations:

| Script | Purpose |
|--------|---------|
| `build_chunked_index.py` | Build JSONL index with chapter metadata |
| `generate_review_report.py` | Analyze all files, generate CSV review |
| `apply_review_decisions.py` | Apply approved tags from CSV to files |

#### **Layer 4: Utilities** (`rag_tools/utils/`)

Helper functions used by workflows:

| Module | Purpose |
|--------|---------|
| `batch.py` | Batch processing utilities |
| `smart_tag_selection.py` | Select top N tags for readability |

---

## Data Flow

### **Phase 1: Index Building** (one-time)
```
build_chunked_index.py
    ↓
    ManualIndexer
    ├─ Read docs/*.md
    ├─ Extract metadata (chapter, domain, section)
    ├─ Generate embeddings (SentenceTransformer)
    └─ Store in Chroma (persistent DB)
    
Output: index/chroma/ with 5000+ chunks
```

### **Phase 2: Tag Suggestions** (per-file analysis)
```
generate_review_report.py
    ↓
    for each file:
        ├─ FileTagUpdater.read_frontmatter()
        ├─ AutoTagger.suggest_tags():
        │   ├─ SemanticSearch.search() [RAG]
        │   ├─ AutoTagger.extract_patterns() [Regex]
        │   └─ CanonicalTags.normalize() [Validation]
        └─ Merge with threshold (strategy='balanced')
    
Output: review_report.csv (file | tags | confidence | OK?)
```

### **Phase 3: Apply Decisions** (batch update)
```
apply_review_decisions.py < review_report.csv
    ↓
    for each row with OK status:
        ├─ FileTagUpdater.update_tags()
        ├─ Write new frontmatter
        └─ Commit changes
    
Output: 250+ files with updated tags
```

---

## Import Examples

### From Other Packages

```python
# Import from rag_core (RAG infrastructure)
from rag_core import SemanticSearch, ManualIndexer, OllamaClient

# Import from rag_tools (tagging operations)
from rag_tools.tagging import AutoTagger, CanonicalTags, FileTagUpdater, TagSuggestion

# Import utilities
from rag_tools.utils import smart_tag_selection
```

### From Workflows

```python
# In rag_tools/workflows/generate_review_report.py
from rag_tools.tagging import AutoTagger, FileTagUpdater
from rag_tools.utils.smart_tag_selection import select_tags_for_display
from manual_rag.config import MANUAL_ROOT

# AutoTagger internally uses SemanticSearch (RAG core)
tagger = AutoTagger()  # Creates SemanticSearch inside
```

---

## Testing

Tests are organized by layer:

```
tests/
├── rag/              # Tests for RAG infrastructure
│   ├── test_chapter_aware.py
│   ├── test_improved_search.py
│   └── test_strategies.py
│
└── tagging/          # Tests for tagging workflows
    └── (add tests here)
```

**Run tests**:
```bash
pytest tests/                # All tests
pytest tests/rag/            # Only RAG tests
pytest tests/tagging/        # Only tagging tests
```

---

## Results Directory

The `results/` directory stores temporary outputs (NOT tracked in git):

```
results/
├── .gitignore        # Excludes: *.csv, *.json, *.db, chroma/, etc.
├── review_report.csv # Generated by generate_review_report.py
├── comparison_*.json # Generated by test scripts
└── chroma/           # Vector index (if moved here)
```

**Why not in git?**
- Generated outputs (reports, indexes)
- Temporary test results
- Large binary files
- Intermediate artifacts

---

## Key Design Decisions

### 1. **Separation by Concern**
- `rag_core/` = Infrastructure (no tagging logic)
- `rag_tools/` = Operations (uses RAG infrastructure)
- `tests/` = Validation
- `results/` = Outputs

### 2. **Modular Tagging Package**
Split large `tagging/__init__.py` into:
- `_tags.py`: CanonicalTags (data)
- `_auto_tagger.py`: AutoTagger (logic)
- `_file_updater.py`: FileTagUpdater (I/O)

Benefits:
- Easier to test each component
- Clear dependencies
- Re-usable modules
- Smaller file sizes

### 3. **Configuration Centralization**
All paths and settings in `manual_rag/config.py`:
```python
MANUAL_ROOT = Path(__file__).parent.parent.parent / "manuals_src" / "docs" / "sbd-toe"
INDEX_DIR = Path(__file__).parent.parent / "index"
TAGS_FILE = Path(__file__).parent.parent / "canonical-tags.yml"
```

### 4. **Git Ignore for Results**
`results/.gitignore` prevents large generated files from bloating repo:
- Reports: `*.csv`, `*.json`
- Indexes: `chroma/`, `*.db`
- Logs: `*.log`
- Temp: `*.tmp`

---

## Future Modularization

### Potential additions:

1. **More specialized workflows**:
   - `rag_tools/workflows/batch_auto_tagger.py` - Process many files at once
   - `rag_tools/workflows/tag_validator.py` - Validate tags across corpus

2. **More tests**:
   - `tests/tagging/test_canonicalization.py`
   - `tests/tagging/test_auto_tagger.py`
   - `tests/integration/` - End-to-end tests

3. **New RAG consumers** (future):
   - `rag_tools/semantic_search/` - UI for searching manual
   - `rag_tools/gap_analysis/` - Find missing content
   - `rag_tools/duplicate_detection/` - Find similar sections

---

## Summary

This modular structure enables:

✅ **Clear responsibilities**: Each module has one job  
✅ **Easy testing**: Test each layer independently  
✅ **Reusability**: Import tagging logic from other projects  
✅ **Extensibility**: Add new workflows without modifying core  
✅ **Maintainability**: Small, focused files  
✅ **Scalability**: Can grow to 100+ modules without confusion  

Every new feature follows this pattern:
1. **Data layer** (e.g., `_tags.py`) - Load/validate data
2. **Logic layer** (e.g., `_auto_tagger.py`) - Process data
3. **I/O layer** (e.g., `_file_updater.py`) - Read/write files
4. **Workflow layer** (e.g., `workflows/my_workflow.py`) - CLI entrypoint

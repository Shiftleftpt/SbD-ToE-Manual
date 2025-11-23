# rag_tools - RAG Usage Tools

Tools and workflows for **USING** the RAG system. This includes auto-tagging, document processing, and various utilities.

## 🎯 Organization

```
rag_tools/
├── tagging/          # Auto-tagging system
│   ├── tests/        # Tagging tests
│   ├── data/         # canonical-tags.yml
│   ├── _tags.py      # Tag management
│   ├── _auto_tagger.py
│   └── README.md
├── workflows/        # Business workflows
│   ├── generate_review_report.py
│   ├── apply_review_decisions.py
│   └── tests/        # Workflow tests (ready)
└── utils/            # Utilities
    ├── smart_tag_selection.py
    └── tests/        # Utils tests (ready)
```

## 📋 Available Tools

### 1. Auto-Tagging System
**Location:** `tagging/`

Combines semantic search, pattern matching, and LLM suggestions for intelligent tag suggestions.

```python
from rag_tools.tagging import AutoTagger, CanonicalTags

# Load canonical tags
tags = CanonicalTags.from_file("rag_tools/tagging/data/canonical-tags.yml")

# Create auto-tagger
tagger = AutoTagger(tags=tags)

# Get suggestions for a file
suggestions = tagger.suggest_tags("path/to/file.md")
```

See [tagging/README.md](tagging/README.md) for details.

### 2. Workflows

#### Generate Review Report
```bash
python3 -m rag_tools.workflows.generate_review_report --max-tags 7
```

Creates a CSV with tag suggestions for all files:
```
file | chapter | current_tags | suggested_tags | confidence | status
...
```

Marks each suggestion as `PENDING` for manual review.

#### Apply Review Decisions
```bash
python3 -m rag_tools.workflows.apply_review_decisions review_report_TIMESTAMP.csv
```

Applies approved changes (status = `OK`) to markdown frontmatter:
1. Read the CSV
2. Filter for `OK` status
3. Update file frontmatter with new tags
4. Create backup of original files

### 3. Utilities

#### Smart Tag Selection
```python
from rag_tools.utils import smart_tag_selection

# Limit tags to ~7 for readability
limited_tags = smart_tag_selection(
    tags=["tag1", "tag2", ...],
    max_tags=7
)
```

## 🚀 Full Tagging Workflow

### Step 1: Build Index
```bash
python3 -m rag_core.indexing.chunked_build
```

### Step 2: Generate Suggestions
```bash
python3 -m rag_tools.workflows.generate_review_report --max-tags 7
```
Output: `review_report_TIMESTAMP.csv`

### Step 3: Review CSV
Edit the CSV, change `PENDING` → `OK` for suggestions to apply:
```csv
file,chapter,current_tags,suggested_tags,confidence,status
docs/chapter/file.md,Chapter 1,"tag1,tag2","tag1,tag2,tag3,tag4",0.85,OK
docs/chapter/file2.md,Chapter 2,"old","new1,new2",0.72,PENDING
```

### Step 4: Apply Changes
```bash
python3 -m rag_tools.workflows.apply_review_decisions review_report_20251123_143022.csv
```

Files updated with new tags in frontmatter.

## 🧪 Testing

### Tagging Tests
```bash
python3 -m pytest rag_tools/tagging/tests/ -v
```

### Workflow Tests
```bash
python3 -m pytest rag_tools/workflows/tests/ -v
```

### Utils Tests
```bash
python3 -m pytest rag_tools/utils/tests/ -v
```

### All Tools Tests
```bash
python3 -m pytest rag_tools/ -v
```

## 📊 Results Example

After running the full workflow:
- **276 files** analyzed
- **252 files** with suggestions (91.3%)
- **+405 tags** added, **-74** removed = **+331 net**
- **100%** chapter accuracy in search tests

## 🔗 Dependencies

This module depends on:
- `rag_core` - For indexing and search
- `ollama` - For LLM-based tagging (optional)
- `pyyaml` - For canonical tags file
- `sentence-transformers` - For embeddings

## 🔗 See Also

- [Main README](../README.md) - Project overview
- [rag_core README](../rag_core/README.md) - Infrastructure details
- [tagging/README.md](tagging/README.md) - Auto-tagging details

# Manual RAG Project Structure

## Core RAG System
```
manual_rag/              # Core RAG library (no dependencies on scripts)
├── config.py            # Configuration
├── __init__.py
├── query/               # Semantic search interface
│   └── __init__.py
├── indexing/            # Index building
│   └── __init__.py
├── tagging/             # Auto-tagging engine
│   └── __init__.py
└── local_llm/           # LLM integration
    └── __init__.py
```

## Tools (Production)
```
tools/
├── build_chunked_index.py      # Build JSONL + Chroma index
├── generate_review_report.py   # Generate tag suggestions
└── apply_review_decisions.py   # Apply approved changes
```

## Scripts (Development/Testing)
```
scripts/
├── utils/
│   ├── smart_tag_selection.py  # Tag filtering logic
│   └── batch.py                # Batch operations
│
└── testing/
    ├── test_improved_search.py
    ├── test_chapter_aware.py
    ├── test_monitorizacao.py
    ├── test_strategies.py
    └── audit_tags_comprehensive.py
    
Deprecated/archived scripts:
    ├── build_index.py              # Old document-level indexing
    ├── auto_tag_corpus.py
    ├── analyze_recall_variance.py
    ├── run_extended_comparison.py
    ├── run_four_way_comparison.py
    ├── quality_analysis.py
    ├── audit_tags.py
    └── (legacy)
```

## Key Distinction

**Core (`manual_rag/`)**: Reusable library - no side effects
- Indexing: Build index from files
- Query: Search semantically
- Tagging: Suggest tags
- LLM: Generate text

**Tools (`tools/`)**: Command-line scripts - orchestrate core components
- Build indexes
- Generate reports
- Apply decisions

**Scripts (`scripts/`)**: Testing and utilities
- Unit tests
- Tag filtering helpers
- Archive of development experiments

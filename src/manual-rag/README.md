# Manual RAG - Semantic Search & Auto-Tagging System

Intelligent RAG (Retrieval-Augmented Generation) system for the SbD-ToE manual with chapter-aware semantic search and automatic tag suggestions.

## 🎯 Features

- **Chunked JSONL Indexing**: 5066 chunks with metadata (chapter, domain, section)
- **Chapter-Aware Search**: 100% precision - searches prioritize same-chapter content
- **Auto-Tagging**: Combine semantic search + pattern matching + existing tags
- **Smart Tag Selection**: Limit to ~7 tags for Docusaurus readability
- **Two-Step Approval Workflow**: Review suggestions, approve/reject, apply

## 📁 Organization

**Core Library** (`manual_rag/`): Reusable components
- `config.py` - Configuration
- `indexing/` - Build indexes
- `query/` - Semantic search
- `tagging/` - Auto-tagging
- `local_llm/` - LLM integration

**Production Tools** (`tools/`): CLI scripts
- `build_chunked_index.py` - Build JSONL + index
- `generate_review_report.py` - Suggest tags
- `apply_review_decisions.py` - Apply changes

**Scripts** (`scripts/`): Testing and utilities
- `utils/` - Helper modules
- `testing/` - Test scripts
- `legacy/` - Deprecated experiments

## 🚀 Quick Start

### 1. Build Index
```bash
python tools/build_chunked_index.py
```

### 2. Generate Review Report
```bash
python tools/generate_review_report.py --max-tags 7
```

### 3. Review & Approve
Edit the CSV: Change `PENDING` → `OK` to approve

### 4. Apply Changes
```bash
python tools/apply_review_decisions.py review_report_TIMESTAMP.csv
```

## 📊 Results

- **276 files** analyzed
- **252 files** with suggestions (91.3%)
- **+405 tags** added, **-74** removed = **+331 net**
- **100%** chapter accuracy in search tests

## 🔧 Setup

```bash
# Create environment
python3 -m venv rag_env
source rag_env/bin/activate
pip install -r requirements.txt

# Start Ollama (for LLM fallback)
ollama pull mistral
ollama serve &
```

## 🧪 Testing

```bash
python scripts/testing/test_improved_search.py
python scripts/testing/test_chapter_aware.py
python scripts/testing/audit_tags_comprehensive.py
```

## 📝 See Also

- `STRUCTURE.md` - Detailed directory structure
- `tools/README.md` - Tool usage guide
- `manual_rag/config.py` - Configuration options

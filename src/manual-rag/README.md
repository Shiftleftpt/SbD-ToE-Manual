# Manual RAG System

Local Retrieval-Augmented Generation system for the SbD-ToE manual.

## Overview

This system indexes the entire manual and provides intelligent analysis beyond simple search:

- **Auto-tagging**: Suggest tags for documents based on semantic similarity
- **Gap analysis**: Identify missing content compared to similar documents  
- **Content validation**: Check coverage against compliance frameworks
- **Cross-referencing**: Find related content automatically
- **Terminology consistency**: Normalize language across the manual

## Quick Start

### Prerequisites

- Python 3.10+
- 4GB RAM (7B LLM) or 16GB RAM (larger models)
- Ollama (for local LLM)

### Installation

```bash
# 1. Setup environment
python3 -m venv rag_env
source rag_env/bin/activate
pip install -r requirements.txt

# 2. Install & start Ollama (one-time)
brew install ollama  # macOS
ollama pull mistral
ollama serve &

# 3. Index the manual (one-time, ~2 min)
python3 build_index.py

# 4. Use the system
python3 -m manual_rag query --help
```

## Architecture

```
manual/ (294 MD files)
  ↓
indexing/
  ├─ build_index.py      # Index all files with embeddings
  └─ embeddings.py       # Embedding model management
  ↓
query/
  ├─ retrieval.py        # RAG document retrieval
  └─ analyzer.py         # Analysis with local LLM
  ↓
local_llm/
  └─ ollama_client.py    # Ollama integration
```

## Usage Examples

### Auto-tag a document

```bash
python3 -m manual_rag tag --file new_doc.md
```

### Analyze gaps

```bash
python3 -m manual_rag gaps --file 03-threat-modeling/01-intro.md
```

### Semantic search

```bash
python3 -m manual_rag search "How to implement authentication in microservices"
```

### Check compliance coverage

```bash
python3 -m manual_rag compliance --standard iso27001
```

## Files

- `build_index.py` - Build/rebuild manual index
- `manual_rag/` - Main package
  - `query/` - Query interface
  - `indexing/` - Indexing functions  
  - `local_llm/` - LLM integration
- `requirements.txt` - Python dependencies
- `config.yaml` - Configuration (embeddings, LLM model, etc)

## Configuration

Edit `config.yaml` to change:

- Embedding model (default: `multilingual-MiniLM-L6-v2`)
- LLM model (default: `mistral` - via Ollama)
- Vector store location (default: `./index/`)
- Top-K similar documents for RAG (default: 3)

## Performance

- Index build: ~2 minutes (294 files)
- Query latency: 100-200ms (retrieval) + 2-3s (LLM analysis)
- Index size: ~200MB
- Vector store: Local SQLite (Chroma)

## Cost

- **Zero** - everything runs locally
- No API costs
- No external dependencies
- Works completely offline after indexing

## Roadmap

- [ ] Web UI for manual browser + RAG queries
- [ ] Bulk operations (tag all files, compliance report)
- [ ] Diff-based change impact analysis
- [ ] Learning path generation
- [ ] Integration with git hooks

## Development

Add new use cases in `query/analyzer.py`. The pattern is:

```python
def new_use_case(query, context_docs, llm_client):
    """Your analysis here"""
    prompt = f"..."
    return llm_client.generate(prompt)
```

## Troubleshooting

**Ollama connection failed?**
- Check: `ollama serve` is running
- URL should be: `http://localhost:11434`

**Slow embeddings?**
- First run caches model (~500MB download)
- Use `multilingual-MiniLM-L6-v2` for speed

**"Model not found" from Ollama?**
- Run: `ollama pull mistral`

## License

Same as SbD-ToE-Manual

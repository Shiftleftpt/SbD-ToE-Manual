"""Chroma Vector Database Architecture and Setup

## What is Chroma?

Chroma is a **vector database** optimized for LLMs and embeddings.
- Stores documents as vectors (embeddings)
- Enables semantic similarity search
- Can be in-memory or persistent (file-based)

## Chroma Setup: No Configuration Needed!

Unlike databases that need servers (PostgreSQL, MongoDB), Chroma is:
- **Embedded**: Runs in-process with your Python code
- **Zero Configuration**: Just import and use
- **No External Service**: Doesn't need a running server

### How it works in our RAG:

```python
from rag_core.indexing import ManualIndexer

indexer = ManualIndexer(manual_root, index_dir)
# ↓
# Automatically creates:
#   - index_dir/chroma/ directory (file-based storage)
#   - Collection "manual" with your embeddings
#   - Everything is persistent!
```

## Storage Modes

### Mode 1: In-Memory (Tests)
```python
import chromadb

# Ephemeral - data lost on exit
client = chromadb.EphemeralClient()
collection = client.get_or_create_collection("test")
```

### Mode 2: Persistent (Production)
```python
import chromadb

# Persistent - data saved to disk
client = chromadb.PersistentClient(path="/path/to/index/chroma")
collection = client.get_or_create_collection("manual")
```

**Our code uses Persistent mode** - data is safe!

## Directory Structure

```
index/
├── chroma/                    # Simple indexing storage
│   ├── data/                  # Vector embeddings
│   ├── metadata/              # Document metadata
│   └── [chroma internals]
├── chroma_chunked/            # Chunked indexing storage
│   ├── data/
│   ├── metadata/
│   └── [chroma internals]
└── manual_chunks.jsonl        # JSONL dataset (optional)
```

## No Ollama Required for Indexing

Ollama is for the **LLM part**, not the database:

```
RAG System:
├── Indexing (uses embeddings model)
│   ├── Sentence-Transformers (embeds text)
│   └── Chroma (stores embeddings) ← NO OLLAMA NEEDED
│
└── Querying (uses LLM)
    ├── Chroma (finds similar documents)
    ├── Sentence-Transformers (embeds query)
    └── Ollama (optional, for enhancement)
```

### Setup needed:
- ✅ **For indexing**: `pip install sentence-transformers chromadb`
- ✅ **For basic queries**: ↑ (same as indexing)
- ⚠️ **For LLM enhancement**: `ollama serve` (in separate terminal)

## Testing Without Data Corruption

Tests use **isolated directories** so production data is never touched:

```python
# Production (never touched by tests)
index/
├── chroma/
└── chroma_chunked/

# Tests (temporary, cleaned up)
/tmp/index_test_xxx/
├── chroma/
└── chroma_chunked/
```

This is why we have fixtures:

```python
@pytest.fixture
def temp_index_dir():
    temp_dir = Path(tempfile.mkdtemp(prefix="index_test_"))
    yield temp_dir
    shutil.rmtree(temp_dir)  # Cleaned up after test
```

## API: Key Chroma Operations

### Create/Open Collection
```python
client = chromadb.PersistentClient(path="./index/chroma")
collection = client.get_or_create_collection("manual")
```

### Add Documents
```python
collection.add(
    ids=["doc1", "doc2"],
    documents=["Document text 1", "Document text 2"],
    embeddings=[vector1, vector2],  # Already computed by embedding model
    metadatas=[{"title": "Doc 1"}, {"title": "Doc 2"}]
)
```

### Search
```python
results = collection.query(
    query_embeddings=[query_vector],
    n_results=5,
    include=["documents", "metadatas", "distances"]
)
# Returns top 5 similar documents
```

### Delete Collection
```python
client.delete_collection("manual")
# Creates fresh collection
```

## Performance Characteristics

| Operation | Time | Notes |
|-----------|------|-------|
| Add 1000 docs | ~10-30s | Depends on embedding model |
| Query | ~100ms | Fast semantic search |
| Rebuild index | ~1-5 min | Full re-embedding |
| Startup (load existing) | ~1-2s | File I/O |

## Common Issues & Solutions

### Issue: "Collection not found"
```python
# Solution: use get_or_create_collection
collection = client.get_or_create_collection("manual")
# Not: collection = client.get_collection("manual")  # Fails if not exists
```

### Issue: "Duplicate IDs"
```python
# Problem: adding document with ID that already exists
collection.add(ids=["doc1"], documents=["text"])
collection.add(ids=["doc1"], documents=["new text"])  # ✗ Error

# Solution: upsert instead
collection.upsert(ids=["doc1"], documents=["new text"])  # ✓ OK
```

### Issue: "Embeddings don't match documents"
```python
# Problem: different number of embeddings and documents
collection.add(
    ids=["doc1", "doc2"],
    documents=["text1", "text2"],
    embeddings=[vector1]  # ✗ Only 1, but 2 documents
)

# Solution: match counts
embeddings = [embed_model.encode(doc) for doc in docs]
collection.add(
    ids=ids,
    documents=docs,
    embeddings=embeddings  # ✓ Same count
)
```

## Production Deployment

### Backup Strategy
```bash
# Back up Chroma data
cp -r index/chroma index/chroma.backup

# Restore from backup
cp -r index/chroma.backup index/chroma
```

### Monitoring
```python
# Check collection stats
collection = client.get_collection("manual")
collection_info = collection.get(include=[])

print(f"Documents: {len(collection_info['ids'])}")
print(f"Collection: {collection_info}")
```

### Scaling
- Single Chroma instance: millions of documents
- For larger scale: consider Chroma in server mode (future enhancement)

## References

- Chroma docs: https://docs.trychroma.com/
- Sentence-Transformers: https://www.sbert.net/
- Vector database concepts: https://en.wikipedia.org/wiki/Vector_database
"""

# Docstring-only module with architecture documentation

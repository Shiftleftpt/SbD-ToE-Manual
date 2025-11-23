"""
RAG Core Module - RAG Infrastructure

Responsible for:
- Building and managing the semantic search index
- Querying the index for similar documents
- Managing embeddings and LLM interactions

Key Classes:
- ManualIndexer: Builds and maintains the vector index
- SemanticSearch: Queries the index for similar documents
- OllamaClient: Interface to local LLM
"""

from .indexing import ManualIndexer
from .query import SemanticSearch
from .local_llm import OllamaClient

__all__ = [
    "ManualIndexer",
    "SemanticSearch", 
    "OllamaClient",
]

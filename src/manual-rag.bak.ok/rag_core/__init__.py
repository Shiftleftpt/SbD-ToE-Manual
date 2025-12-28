"""
RAG Core Module - RAG Infrastructure

Responsibility: Semantic search infrastructure only (index building and querying).
Does NOT handle tagging, analysis, or application-specific logic.

Key Classes:
- ManualIndexer: Builds and maintains the vector index
- SemanticSearch: Queries the index for similar documents
- OllamaClient: Interface to local LLM (utility for core operations)
"""

from .indexing import ManualIndexer
from .query import SemanticSearch
from .local_llm import OllamaClient

__all__ = [
    "ManualIndexer",
    "SemanticSearch", 
    "OllamaClient",
]

"""Manual RAG System - Main Package"""

__version__ = "0.1.0"
__title__ = "Manual RAG"

from .query import SemanticSearch
from .local_llm import OllamaClient

__all__ = ["SemanticSearch", "OllamaClient"]

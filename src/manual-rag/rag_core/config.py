"""Configuration for RAG Core (models, parameters)

This module contains configuration for the RAG infrastructure only.
Path and tool-specific configuration is in rag_tools/config.py
"""

# Embedding model
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# LLM (Ollama)
OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_MODEL = "mistral"

# RAG parameters
TOP_K = 5  # Documents to retrieve for context
MIN_SIMILARITY = 0.3  # Lowered threshold for better results
CHUNK_SIZE = 500  # Characters per document chunk

print(f"RAG Core config loaded:")
print(f"  Embedding model: {EMBEDDING_MODEL}")
print(f"  LLM: {OLLAMA_MODEL} @ {OLLAMA_BASE_URL}")


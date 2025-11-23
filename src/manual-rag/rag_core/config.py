"""Configuration for RAG Core - everything needed to build and run RAG

This module contains configuration for RAG infrastructure only:
- Paths: where to find docs, where to store index
- Parameters: models, LLM settings, search thresholds

rag_core is completely self-contained and independent from applications.
"""

from pathlib import Path

# Paths - Required for building and querying the RAG
CURRENT_FILE = Path(__file__).resolve()  # rag_core/config.py
RAG_CORE_DIR = CURRENT_FILE.parent  # rag_core/
WORKSPACE_DIR = RAG_CORE_DIR.parent  # src/manual-rag/
REPO_ROOT = WORKSPACE_DIR.parent.parent  # SbD-ToE-Manual/

MANUAL_ROOT = REPO_ROOT / "manuals_src" / "docs" / "sbd-toe"
INDEX_DIR = WORKSPACE_DIR / "index"
TAGS_FILE = WORKSPACE_DIR / "canonical-tags.yml"

# Embedding model
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# LLM (Ollama)
OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_MODEL = "mistral"

# RAG parameters
TOP_K = 5  # Documents to retrieve for context
MIN_SIMILARITY = 0.3  # Lowered threshold for better results
CHUNK_SIZE = 500  # Characters per document chunk

# Ensure paths exist
INDEX_DIR.mkdir(parents=True, exist_ok=True)

print(f"RAG Core config loaded:")
print(f"  Manual root: {MANUAL_ROOT}")
print(f"  Index dir: {INDEX_DIR}")
print(f"  Tags file: {TAGS_FILE}")
print(f"  Embedding model: {EMBEDDING_MODEL}")
print(f"  LLM: {OLLAMA_MODEL} @ {OLLAMA_BASE_URL}")



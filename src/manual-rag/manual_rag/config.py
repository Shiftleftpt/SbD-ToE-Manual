"""Configuration for Manual RAG system"""

import os
from pathlib import Path

# Paths
REPO_ROOT = Path(__file__).parent.parent.parent.parent  # src/manual-rag/../..
MANUAL_ROOT = REPO_ROOT / "manuals_src" / "docs" / "sbd-toe"
INDEX_DIR = Path(__file__).parent.parent / "index"
TAGS_FILE = REPO_ROOT / "tag-normalization" / "canonical-tags.yml"

# Embedding model
# Using all-MiniLM-L6-v2 instead - more reliable and faster
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# LLM (Ollama)
OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_MODEL = "mistral"

# RAG parameters
TOP_K = 5  # Documents to retrieve for context
MIN_SIMILARITY = 0.3  # Lowered threshold for better results
CHUNK_SIZE = 500  # Characters per document chunk

# Ensure index dir exists
INDEX_DIR.mkdir(parents=True, exist_ok=True)

print(f"Config loaded:")
print(f"  Manual root: {MANUAL_ROOT}")
print(f"  Index dir: {INDEX_DIR}")
print(f"  Embedding model: {EMBEDDING_MODEL}")
print(f"  LLM: {OLLAMA_MODEL} @ {OLLAMA_BASE_URL}")

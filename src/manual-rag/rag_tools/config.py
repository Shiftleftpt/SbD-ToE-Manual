"""Configuration for RAG Tools (tagging, workflows)"""

from pathlib import Path

# Paths
CURRENT_FILE = Path(__file__).resolve()  # src/manual-rag/rag_tools/config.py
ROOT_DIR = CURRENT_FILE.parent.parent  # src/manual-rag/

MANUAL_ROOT = ROOT_DIR.parent.parent / "manuals_src" / "docs" / "sbd-toe"
INDEX_DIR = ROOT_DIR / "index"
TAGS_FILE = ROOT_DIR / "canonical-tags.yml"

# Ensure paths exist
INDEX_DIR.mkdir(parents=True, exist_ok=True)

print(f"RAG Tools config loaded:")
print(f"  Manual root: {MANUAL_ROOT}")
print(f"  Index dir: {INDEX_DIR}")
print(f"  Tags file: {TAGS_FILE}")

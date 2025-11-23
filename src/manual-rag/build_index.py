#!/usr/bin/env python3
"""Standalone script to build the RAG index

This is the primary way to build the index. Can be run directly:
    python build_index.py
    python build_index.py --rebuild

Or through the module:
    python -m rag_core.indexing.build
    python -m manual_rag index --rebuild
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from rag_core.indexing.build import main

if __name__ == "__main__":
    sys.exit(main())

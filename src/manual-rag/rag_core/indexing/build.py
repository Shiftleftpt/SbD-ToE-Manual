#!/usr/bin/env python3
"""Build the manual index - CLI entry point for creating RAG infrastructure

Usage:
    python -m rag_core.indexing.build [--rebuild]

Options:
    --rebuild   Clear existing index and rebuild from scratch
"""

import sys
import argparse
from pathlib import Path

from . import ManualIndexer
from ..config import MANUAL_ROOT, INDEX_DIR


def main():
    """Build the semantic search index"""
    parser = argparse.ArgumentParser(description="Build manual semantic search index")
    parser.add_argument(
        "--rebuild",
        action="store_true",
        help="Clear existing index and rebuild from scratch"
    )
    args = parser.parse_args()
    
    print(f"Building index from: {MANUAL_ROOT}")
    indexer = ManualIndexer(MANUAL_ROOT, INDEX_DIR)
    stats = indexer.index_all(force_rebuild=args.rebuild)
    
    print(f"\nIndex saved to: {INDEX_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

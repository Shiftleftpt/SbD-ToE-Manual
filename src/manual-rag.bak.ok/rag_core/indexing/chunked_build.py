#!/usr/bin/env python3
"""Build chunked JSONL dataset and index - Core RAG infrastructure

This is the advanced RAG indexing pipeline that creates:
1. JSONL dataset with chunked documents and rich metadata
2. Chroma vector index optimized for chunk-level retrieval

Usage:
    python -m rag_core.indexing.chunked_build [--no-index]
    
Options:
    --no-index  Build JSONL only, don't create Chroma index
"""

import sys
import argparse
from pathlib import Path

from .chunked import JSONLDatasetBuilder, ChunkedIndexBuilder
from ..config import MANUAL_ROOT, INDEX_DIR


def main():
    """Build chunked JSONL dataset and vector index"""
    parser = argparse.ArgumentParser(
        description="Build chunked JSONL dataset and Chroma index for advanced RAG"
    )
    parser.add_argument(
        "--no-index",
        action="store_true",
        help="Build JSONL only, don't create Chroma index"
    )
    args = parser.parse_args()
    
    # Step 1: Build JSONL dataset
    print("=" * 60)
    print("STEP 1: Building JSONL Dataset")
    print("=" * 60)
    builder = JSONLDatasetBuilder(MANUAL_ROOT, INDEX_DIR, chunk_size=500, overlap=100)
    jsonl_path = builder.build_dataset()
    
    # Step 2: Build Chroma index (optional)
    if not args.no_index:
        print("\n" + "=" * 60)
        print("STEP 2: Building Chroma Index")
        print("=" * 60)
        index_builder = ChunkedIndexBuilder(INDEX_DIR)
        index_builder.build_from_jsonl(jsonl_path, force_rebuild=True)
        print(f"\n{'=' * 60}")
        print("🎉 RAG pipeline complete! Ready for queries.")
        print(f"{'=' * 60}")
    else:
        print(f"\n✓ JSONL dataset ready at: {jsonl_path}")
        print("Run without --no-index to build Chroma index")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

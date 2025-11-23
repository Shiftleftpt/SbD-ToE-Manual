#!/usr/bin/env python3
"""Build chunked JSONL dataset with metadata for improved RAG indexing

DEPRECATED: This module now delegates to rag_core.indexing.chunked

Use instead:
    from rag_core.indexing import JSONLDatasetBuilder, ChunkedIndexBuilder
    from rag_core.metadata import ChaptersMetadata

Or run directly:
    python -m rag_core.indexing.chunked_build
"""

import sys
import warnings
from pathlib import Path

# Keep backwards compatibility - redirect to new location
warnings.warn(
    "rag_tools.workflows.build_chunked_index is deprecated. "
    "Use rag_core.indexing.chunked or rag_core.indexing.chunked_build instead.",
    DeprecationWarning,
    stacklevel=2
)

from rag_core.indexing.chunked_build import main

if __name__ == "__main__":
    print("⚠️  Deprecated: Use 'python -m rag_core.indexing.chunked_build' instead")
    sys.exit(main())


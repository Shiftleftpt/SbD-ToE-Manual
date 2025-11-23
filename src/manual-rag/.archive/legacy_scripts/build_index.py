#!/usr/bin/env python3
"""Build index for Manual RAG system"""

from rag_core import ManualIndexer
from rag_core.config import MANUAL_ROOT, INDEX_DIR

if __name__ == "__main__":
    import sys
    
    force_rebuild = "--rebuild" in sys.argv
    
    print(f"Manual RAG Index Builder")
    print(f"Manual location: {MANUAL_ROOT}")
    print()
    
    indexer = ManualIndexer(MANUAL_ROOT, INDEX_DIR)
    stats = indexer.index_all(force_rebuild=force_rebuild)
    
    print(f"\n✓ Index ready for queries")

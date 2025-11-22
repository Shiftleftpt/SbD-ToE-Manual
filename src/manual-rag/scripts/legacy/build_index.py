#!/usr/bin/env python3
"""Build index for Manual RAG system"""

from manual_rag.indexing import ManualIndexer
from manual_rag.config import MANUAL_ROOT

if __name__ == "__main__":
    import sys
    
    force_rebuild = "--rebuild" in sys.argv
    
    print(f"Manual RAG Index Builder")
    print(f"Manual location: {MANUAL_ROOT}")
    print()
    
    indexer = ManualIndexer()
    stats = indexer.index_all(force_rebuild=force_rebuild)
    
    print(f"\n✓ Index ready for queries")

"""Query interface - Semantic search only

Responsibility: Pure semantic search - query the index for similar documents.
This module does NOT handle:
- Tag suggestion (belongs to rag_tools.tagging.AutoTagger)
- Gap analysis (belongs to analysis tools)
- Duplicate detection (belongs to analysis tools)
- Cross-referencing (belongs to analysis tools)
"""

import json
from typing import List, Dict
from sentence_transformers import SentenceTransformer
import chromadb

from ..config import INDEX_DIR, EMBEDDING_MODEL, TOP_K, MIN_SIMILARITY


class SemanticSearch:
    """Semantic search interface - query similar documents from the index"""
    
    def __init__(self):
        self.embedding_model = SentenceTransformer(EMBEDDING_MODEL)
        
        # Connect to persistent index (new Chroma API)
        self.client = chromadb.PersistentClient(path=str(INDEX_DIR / "chroma"))
        self.collection = self.client.get_collection("manual")
    
    @staticmethod
    def _extract_chapter(path: str) -> str:
        """Extract chapter prefix from file path
        
        Args:
            path: File path like "010-sbd-manual/02-requisitos-seguranca/file.md"
            
        Returns:
            Chapter prefix like "010-sbd-manual" or "002-cross-check-normativo"
        """
        parts = path.split("/")
        if parts:
            return parts[0]
        return ""
    
    def search(self, query: str, top_k: int = TOP_K, context_file: str = None) -> List[Dict]:
        """Semantic search for similar documents with optional chapter context
        
        Args:
            query: Search query
            top_k: Number of results to return
            context_file: Optional file path to prioritize same-chapter results
            
        Returns:
            List of similar documents with metadata, chapter-aware ranked
        """
        embedding = self.embedding_model.encode(query).tolist()
        
        # Get more results initially if we have chapter context
        # So we can filter/rerank them
        initial_k = top_k * 2 if context_file else top_k
        
        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=initial_k
        )
        
        docs = []
        if results["ids"] and results["ids"][0]:
            for i, doc_id in enumerate(results["ids"][0]):
                distance = results["distances"][0][i]
                similarity = 1 - (distance / 2)  # Convert distance to similarity
                
                if similarity >= MIN_SIMILARITY:
                    metadata = results["metadatas"][0][i]
                    
                    # Handle both old (document-level) and new (chunk-level) metadata formats
                    path = metadata.get("path") or metadata.get("file_path", "unknown")
                    title = metadata.get("title", path.split("/")[-1] if path != "unknown" else "")
                    
                    docs.append({
                        "path": path,
                        "title": title,
                        "content": results["documents"][0][i],
                        "similarity": float(similarity),
                        "tags": json.loads(metadata.get("tags", "[]")),
                        "metadata": metadata,  # Include full metadata (chunk context)
                    })
        
        # Apply chapter-aware ranking if context provided
        if context_file and docs:
            context_chapter = self._extract_chapter(context_file)
            
            # Separate same-chapter and cross-chapter results
            same_chapter = []
            cross_chapter = []
            
            for doc in docs:
                doc_chapter = self._extract_chapter(doc["path"])
                if doc_chapter == context_chapter:
                    same_chapter.append(doc)
                else:
                    cross_chapter.append(doc)
            
            # Rerank: same-chapter results first (already sorted by similarity within each group)
            # Boost same-chapter similarity scores slightly to maintain relevance ranking
            docs = same_chapter + cross_chapter
        
        # Return requested number of results
        return docs[:top_k]


if __name__ == "__main__":
    print("Initializing semantic search...")
    searcher = SemanticSearch()
    
    # Example usage
    results = searcher.search("authentication and authorization")
    print(f"\nFound {len(results)} related documents:")
    for doc in results:
        print(f"  - {doc['path']} ({doc['similarity']:.2%})")


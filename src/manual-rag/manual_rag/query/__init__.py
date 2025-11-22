"""Query interface - Semantic search and analysis"""

import json
from typing import List, Dict
from sentence_transformers import SentenceTransformer
import chromadb

from ..config import INDEX_DIR, EMBEDDING_MODEL, TOP_K, MIN_SIMILARITY
from ..local_llm import OllamaClient


class SemanticSearch:
    def __init__(self):
        self.embedding_model = SentenceTransformer(EMBEDDING_MODEL)
        
        # Connect to persistent index (new Chroma API)
        self.client = chromadb.PersistentClient(path=str(INDEX_DIR / "chroma"))
        self.collection = self.client.get_collection("manual")
        self.llm = OllamaClient()
    
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
    
    def suggest_tags(self, file_path: str, query: str = None) -> Dict:
        """Suggest tags by finding similar documents
        
        Args:
            file_path: Path to file to tag
            query: Optional query to search similar docs
            
        Returns:
            Dict with suggested tags and reasoning
        """
        if not query:
            query = file_path.replace("_", " ").replace("/", " ")
        
        similar_docs = self.search(query, top_k=3)
        
        if not similar_docs:
            return {"tags": [], "reasoning": "No similar documents found"}
        
        # Collect tags from similar docs
        suggested_tags = {}
        for doc in similar_docs:
            for tag in doc["tags"]:
                suggested_tags[tag] = suggested_tags.get(tag, 0) + doc["similarity"]
        
        # Sort by frequency/similarity
        sorted_tags = sorted(
            suggested_tags.items(),
            key=lambda x: x[1],
            reverse=True
        )[:5]
        
        # Use LLM to refine suggestions
        context = "\n".join([
            f"- {doc['path']}: {doc['tags']}"
            for doc in similar_docs
        ])
        
        prompt = f"""Based on similar documents in the manual:
{context}

What tags would be most appropriate for: {file_path}?
Suggest 3-5 tags that fit this document."""
        
        reasoning = self.llm.generate(prompt)
        
        return {
            "suggested_tags": [tag for tag, _ in sorted_tags],
            "confidence": float(similar_docs[0]["similarity"]) if similar_docs else 0,
            "similar_documents": [d["path"] for d in similar_docs],
            "reasoning": reasoning,
        }
    
    def analyze_gaps(self, file_path: str) -> Dict:
        """Analyze what content might be missing compared to similar files
        
        Args:
            file_path: Path to analyze
            
        Returns:
            Gap analysis results
        """
        similar = self.search(file_path, top_k=3)
        
        if not similar:
            return {"gaps": [], "recommendation": "No similar documents found for comparison"}
        
        # Build context from similar docs
        context = "\n".join([
            f"Document: {doc['path']}\nTags: {doc['tags']}\nPreview: {doc['content'][:200]}..."
            for doc in similar
        ])
        
        prompt = f"""Comparing {file_path} with similar documents:

{context}

What sections or topics might be missing from {file_path}?
List 3-5 potential gaps."""
        
        gaps = self.llm.generate(prompt, temperature=0.5)
        
        return {
            "file": file_path,
            "similar_documents": [d["path"] for d in similar],
            "potential_gaps": gaps,
        }
    
    def find_duplicates(self, similarity_threshold: float = 0.85) -> List[List[str]]:
        """Find potentially duplicate or near-duplicate content
        
        Args:
            similarity_threshold: Minimum similarity to consider duplicates
            
        Returns:
            List of document groups with high similarity
        """
        # This would require checking all pairs - simplified version:
        duplicates = []
        return duplicates  # TODO: Implement full duplicate detection
    
    def cross_reference(self, query: str) -> Dict:
        """Find all related content across the manual
        
        Args:
            query: Topic to find references for
            
        Returns:
            Organized cross-references
        """
        results = self.search(query, top_k=10)
        
        # Organize by chapter
        by_chapter = {}
        for doc in results:
            chapter = doc["path"].split("/")[0]
            if chapter not in by_chapter:
                by_chapter[chapter] = []
            by_chapter[chapter].append(doc)
        
        return {
            "query": query,
            "total_related": len(results),
            "by_chapter": by_chapter,
            "documents": results,
        }


if __name__ == "__main__":
    print("Initializing semantic search...")
    searcher = SemanticSearch()
    
    # Example usage
    results = searcher.search("authentication and authorization")
    print(f"\nFound {len(results)} related documents:")
    for doc in results:
        print(f"  - {doc['path']} ({doc['similarity']:.2%})")

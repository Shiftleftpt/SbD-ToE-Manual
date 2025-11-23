"""Indexing module - Build and manage manual index"""

import os
import json
from pathlib import Path
from typing import List, Dict
from sentence_transformers import SentenceTransformer
import chromadb
import yaml

from ..config import MANUAL_ROOT, INDEX_DIR, EMBEDDING_MODEL, TOP_K, TAGS_FILE

class ManualIndexer:
    def __init__(self):
        self.embedding_model = SentenceTransformer(EMBEDDING_MODEL)
        
        # Setup Chroma with new API (persistent storage)
        self.client = chromadb.PersistentClient(path=str(INDEX_DIR / "chroma"))
        self.collection = self.client.get_or_create_collection("manual")
        
        # Load canonical tags
        self.tags = self._load_tags()
        
    def _load_tags(self) -> Dict[str, any]:
        """Load canonical tags from YAML"""
        if not TAGS_FILE.exists():
            print(f"Warning: Tags file not found at {TAGS_FILE}")
            return {}
        
        try:
            with open(TAGS_FILE, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {}
        except Exception as e:
            print(f"Error loading tags: {e}")
            return {}
    
    def _read_file(self, path: Path) -> Dict:
        """Read markdown file and extract metadata"""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract frontmatter if present
            frontmatter = {}
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    try:
                        frontmatter = yaml.safe_load(parts[1]) or {}
                        content = parts[2]
                    except:
                        pass
            
            return {
                "path": str(path.relative_to(MANUAL_ROOT)),
                "content": content.strip(),
                "frontmatter": frontmatter,
                "title": frontmatter.get("title", path.stem),
                "tags": frontmatter.get("tags", [])
            }
        except Exception as e:
            print(f"Error reading {path}: {e}")
            return None
    
    def index_all(self, force_rebuild: bool = False) -> Dict:
        """Index all markdown files in manual
        
        Args:
            force_rebuild: If True, clear existing index first
            
        Returns:
            Statistics about indexing
        """
        if force_rebuild:
            self.client.delete_collection("manual")
            self.collection = self.client.get_or_create_collection("manual")
        
        # Find all markdown files
        md_files = list(MANUAL_ROOT.rglob("*.md"))
        md_files = [f for f in md_files if not f.name.endswith(".2review")]
        
        stats = {
            "total_files": len(md_files),
            "indexed": 0,
            "failed": 0,
            "total_chars": 0,
        }
        
        for i, file_path in enumerate(md_files):
            if (i + 1) % 50 == 0:
                print(f"Processing {i+1}/{len(md_files)}...")
            
            doc_data = self._read_file(file_path)
            if not doc_data:
                stats["failed"] += 1
                continue
            
            try:
                # Embed and store
                embedding = self.embedding_model.encode(doc_data["content"]).tolist()
                
                doc_id = doc_data["path"].replace("/", "_").replace(".md", "")
                
                self.collection.add(
                    ids=[doc_id],
                    documents=[doc_data["content"]],
                    embeddings=[embedding],
                    metadatas=[{
                        "path": doc_data["path"],
                        "title": doc_data["title"],
                        "tags": json.dumps(doc_data["tags"]),
                    }]
                )
                
                stats["indexed"] += 1
                stats["total_chars"] += len(doc_data["content"])
                
            except Exception as e:
                print(f"Error indexing {file_path}: {e}")
                stats["failed"] += 1
        
        # New Chroma API persists automatically
        print(f"\nIndexing complete:")
        print(f"  Indexed: {stats['indexed']}/{len(md_files)}")
        print(f"  Failed: {stats['failed']}")
        print(f"  Total chars: {stats['total_chars']:,}")
        
        return stats

if __name__ == "__main__":
    import sys
    
    force_rebuild = "--rebuild" in sys.argv
    
    print(f"Building index from: {MANUAL_ROOT}")
    indexer = ManualIndexer()
    stats = indexer.index_all(force_rebuild=force_rebuild)
    
    print(f"\nIndex saved to: {INDEX_DIR}")

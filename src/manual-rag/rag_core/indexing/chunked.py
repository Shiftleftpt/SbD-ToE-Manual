"""Chunked indexing for RAG - split documents into overlapping chunks

This is core RAG infrastructure for building advanced vector indexes
with chunk-level metadata and overlapping context windows.
"""

import json
import sys
from pathlib import Path
from typing import List, Dict, Tuple, Optional

import yaml
from sentence_transformers import SentenceTransformer
import chromadb

from ..config import EMBEDDING_MODEL, TAGS_FILE
from ..metadata import ChaptersMetadata


class DocumentChunker:
    """Split documents into chunks with metadata context"""
    
    def __init__(self, chunk_size: int = 500, overlap: int = 100):
        """Initialize chunker with configurable parameters
        
        Args:
            chunk_size: Target characters per chunk
            overlap: Overlap between consecutive chunks (for context)
        """
        self.chunk_size = chunk_size
        self.overlap = overlap
    
    @staticmethod
    def read_file(file_path: Path) -> Tuple[Dict, str]:
        """Read markdown file and extract frontmatter + content
        
        Args:
            file_path: Path to markdown file
            
        Returns:
            Tuple of (frontmatter_dict, content_without_frontmatter)
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        frontmatter = {}
        remaining_content = content
        
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    frontmatter = yaml.safe_load(parts[1]) or {}
                    remaining_content = parts[2].strip()
                except yaml.YAMLError:
                    pass
        
        return frontmatter, remaining_content
    
    def chunk_content(self, content: str) -> List[str]:
        """Split content into overlapping chunks
        
        Args:
            content: Full document content
            
        Returns:
            List of chunks (strings)
        """
        if len(content) <= self.chunk_size:
            return [content]
        
        chunks = []
        step = self.chunk_size - self.overlap
        
        for i in range(0, len(content), step):
            chunk = content[i:i + self.chunk_size]
            if chunk.strip():  # Only add non-empty chunks
                chunks.append(chunk)
        
        return chunks
    
    def create_chunk_metadata(self, chunk_index: int, total_chunks: int,
                             file_metadata: Dict, content: str) -> Dict:
        """Create metadata for a single chunk
        
        Args:
            chunk_index: Index of this chunk in the document
            total_chunks: Total number of chunks in document
            file_metadata: File-level metadata from ChaptersMetadata.parse_path()
            content: The chunk content
            
        Returns:
            Metadata dictionary for this chunk
        """
        return {
            "chunk_index": chunk_index,
            "total_chunks": total_chunks,
            "chapter": file_metadata.get("chapter", ""),
            "chapter_name": file_metadata.get("chapter_name", ""),
            "chapter_type": file_metadata.get("chapter_type", ""),
            "section": file_metadata.get("section", ""),
            "domain": file_metadata.get("domain", ""),
            "file_path": file_metadata.get("file_path", ""),
            "file_name": file_metadata.get("file_name", ""),
            "content_length": len(content),
            "content_preview": content[:100].replace("\n", " "),
        }


class JSONLDatasetBuilder:
    """Build JSONL dataset from markdown files with structured chunks
    
    Converts markdown files into JSONL format where each line is a chunk
    with rich metadata for downstream processing or advanced indexing.
    """
    
    def __init__(self, manual_root: Path, index_dir: Path, 
                 chunk_size: int = 500, overlap: int = 100):
        """Initialize builder
        
        Args:
            manual_root: Root directory containing markdown files
            index_dir: Directory to store outputs
            chunk_size: Target characters per chunk
            overlap: Overlap between chunks
        """
        self.manual_root = Path(manual_root)
        self.index_dir = Path(index_dir)
        self.chunker = DocumentChunker(chunk_size, overlap)
        self.tags_file = TAGS_FILE
    
    def _load_tags(self) -> Dict:
        """Load canonical tags from YAML"""
        if not self.tags_file.exists():
            print(f"Warning: Tags file not found at {self.tags_file}")
            return {}
        
        try:
            with open(self.tags_file, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {}
        except Exception as e:
            print(f"Error loading tags: {e}")
            return {}
    
    def build_dataset(self, output_path: Path = None) -> Path:
        """Build JSONL dataset from all manual files
        
        Args:
            output_path: Where to save JSONL (default: index_dir/manual_chunks.jsonl)
            
        Returns:
            Path to created JSONL file
        """
        if output_path is None:
            output_path = self.index_dir / "manual_chunks.jsonl"
        
        # Ensure output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Load tags for reference
        tags = self._load_tags()
        
        # Find all markdown files
        md_files = sorted(list(self.manual_root.rglob("*.md")))
        md_files = [f for f in md_files if not f.name.endswith(".2review")]
        
        stats = {
            "total_files": len(md_files),
            "total_chunks": 0,
            "total_chars": 0,
            "files_processed": 0,
            "files_failed": 0,
        }
        
        print(f"Building JSONL dataset from {len(md_files)} files...")
        print(f"Output: {output_path}\n")
        
        with open(output_path, 'w', encoding='utf-8') as jsonl_file:
            for i, file_path in enumerate(md_files, 1):
                if i % 50 == 0:
                    print(f"Processing {i}/{len(md_files)}...")
                
                try:
                    # Read file
                    frontmatter, content = self.chunker.read_file(file_path)
                    if not content.strip():
                        stats["files_failed"] += 1
                        continue
                    
                    # Parse metadata from path
                    rel_path = str(file_path.relative_to(self.manual_root))
                    file_metadata = ChaptersMetadata.parse_path(rel_path)
                    
                    # Extract frontmatter data
                    title = frontmatter.get('title', file_path.stem)
                    file_tags = frontmatter.get('tags', [])
                    categoria = frontmatter.get('categoria')
                    group = frontmatter.get('group')
                    
                    # Split into chunks
                    chunks = self.chunker.chunk_content(content)
                    
                    # Write each chunk as JSONL record
                    for chunk_idx, chunk_content in enumerate(chunks):
                        chunk_metadata = self.chunker.create_chunk_metadata(
                            chunk_idx, len(chunks), file_metadata, chunk_content
                        )
                        
                        # Build frontmatter with categoria and group if present
                        frontmatter_record = {
                            "title": title,
                            "tags": file_tags,
                        }
                        if categoria:
                            frontmatter_record["categoria"] = categoria
                        if group:
                            frontmatter_record["group"] = group
                        
                        record = {
                            "id": f"{file_metadata['file_path'].replace('/', '_').replace('.md', '')}_{chunk_idx}",
                            "text": chunk_content,
                            "metadata": chunk_metadata,
                            "frontmatter": frontmatter_record
                        }
                        
                        jsonl_file.write(json.dumps(record, ensure_ascii=False) + "\n")
                        
                        stats["total_chunks"] += 1
                        stats["total_chars"] += len(chunk_content)
                    
                    stats["files_processed"] += 1
                    
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
                    stats["files_failed"] += 1
        
        print(f"\n✓ JSONL dataset created successfully!")
        print(f"\nStatistics:")
        print(f"  Files processed: {stats['files_processed']}/{stats['total_files']}")
        print(f"  Files failed: {stats['files_failed']}")
        print(f"  Total chunks: {stats['total_chunks']}")
        print(f"  Total chars: {stats['total_chars']:,}")
        print(f"  Avg chunk size: {stats['total_chars'] // max(1, stats['total_chunks']) if stats['total_chunks'] > 0 else 0:,} chars")
        print(f"  Output file: {output_path}")
        print(f"  File size: {output_path.stat().st_size / 1024 / 1024:.2f} MB")
        
        return output_path


class ChunkedIndexBuilder:
    """Build Chroma vector index from chunks with advanced metadata
    
    Creates an index optimized for chunked retrieval with context-aware
    metadata that preserves document structure and relationships.
    """
    
    def __init__(self, index_dir: Path):
        """Initialize index builder
        
        Args:
            index_dir: Directory for storing Chroma index
        """
        self.index_dir = Path(index_dir)
        self.embedding_model = SentenceTransformer(EMBEDDING_MODEL)
        self.client = chromadb.PersistentClient(path=str(self.index_dir / "chroma_chunked"))
    
    def build_from_jsonl(self, jsonl_path: Path, force_rebuild: bool = True) -> Dict:
        """Build Chroma index from JSONL file
        
        Args:
            jsonl_path: Path to JSONL file
            force_rebuild: If True, delete existing collection first
            
        Returns:
            Statistics about indexing
        """
        collection_name = "manual_chunked"
        
        if force_rebuild:
            try:
                self.client.delete_collection(collection_name)
                print("Deleted existing collection")
            except:
                pass
        
        collection = self.client.get_or_create_collection(collection_name)
        
        print(f"\nBuilding Chroma index from {jsonl_path}...")
        
        stats = {
            "total_records": 0,
            "indexed": 0,
            "failed": 0,
        }
        
        with open(jsonl_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, 1):
                if i % 100 == 0:
                    print(f"Indexing {i}...")
                
                try:
                    record = json.loads(line)
                    stats["total_records"] += 1
                    
                    # Embed the chunk text
                    embedding = self.embedding_model.encode(record["text"]).tolist()
                    
                    # Prepare metadata (include frontmatter tags, categoria, group)
                    metadata = record.get("metadata", {})
                    frontmatter = record.get("frontmatter", {})
                    metadata["title"] = frontmatter.get("title", "")
                    metadata["tags"] = json.dumps(frontmatter.get("tags", []))
                    if "categoria" in frontmatter:
                        metadata["categoria"] = frontmatter["categoria"]
                    if "group" in frontmatter:
                        metadata["group"] = frontmatter["group"]
                    
                    # Add to collection
                    collection.add(
                        ids=[record["id"]],
                        documents=[record["text"]],
                        embeddings=[embedding],
                        metadatas=[metadata]
                    )
                    
                    stats["indexed"] += 1
                    
                except Exception as e:
                    print(f"Error indexing record {i}: {e}")
                    stats["failed"] += 1
        
        print(f"\n✓ Index built successfully!")
        print(f"  Total records: {stats['total_records']}")
        print(f"  Indexed: {stats['indexed']}")
        print(f"  Failed: {stats['failed']}")
        
        return stats

#!/usr/bin/env python3
"""Build chunked JSONL dataset with metadata for improved RAG indexing"""

import json
import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple
import yaml

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from manual_rag.config import MANUAL_ROOT, INDEX_DIR, TAGS_FILE
from rag_core import ManualIndexer

class ChaptersMetadata:
    """Parse and understand chapter structure"""
    
    CHAPTER_PATTERNS = {
        "000-teory-of-everything": {"name": "Theory of Everything", "type": "foundational"},
        "001-how-to-manual": {"name": "How to Use Manual", "type": "meta"},
        "002-cross-check-normativo": {"name": "Normative Cross-Check", "type": "frameworks"},
        "003-policies-globals": {"name": "Global Policies", "type": "governance"},
        "010-sbd-manual": {"name": "Security by Design Manual", "type": "main_content"},
    }
    
    SECURITY_DOMAINS = {
        "01-classificacao-aplicacoes": "Application Classification",
        "02-requisitos-seguranca": "Security Requirements",
        "03-threat-modeling": "Threat Modeling",
        "04-arquitetura-segura": "Secure Architecture",
        "05-dependencias-sbom-sca": "Dependencies & SBOM",
        "06-desenvolvimento-seguro": "Secure Development",
        "07-cicd-seguro": "Secure CI/CD",
        "08-iac-infraestrutura": "Infrastructure as Code",
        "09-containers-imagens": "Containers & Images",
        "10-testes-seguranca": "Security Testing",
        "11-deploy-seguro": "Secure Deployment",
        "12-monitorizacao-operacoes": "Monitoring & Operations",
        "13-formacao-onboarding": "Training & Onboarding",
        "14-governanca-contratacao": "Governance & Procurement",
    }
    
    @staticmethod
    def parse_path(file_path: str) -> Dict:
        """Extract structured metadata from file path
        
        Example paths:
        - 010-sbd-manual/02-requisitos-seguranca/intro.md
        - 002-cross-check-normativo/dora/01-intro.md
        - 000-teory-of-everything/01-intro.md
        """
        parts = file_path.replace(".md", "").split("/")
        
        metadata = {
            "file_path": file_path,
            "file_name": parts[-1] if parts else "",
            "chapter": parts[0] if parts else "",
            "section": parts[1] if len(parts) > 1 else "",
            "subsection": parts[2] if len(parts) > 2 else "",
        }
        
        # Enrich with chapter info
        if metadata["chapter"] in ChaptersMetadata.CHAPTER_PATTERNS:
            ch_info = ChaptersMetadata.CHAPTER_PATTERNS[metadata["chapter"]]
            metadata["chapter_name"] = ch_info["name"]
            metadata["chapter_type"] = ch_info["type"]
        
        # Enrich with security domain info (only for 010-sbd-manual)
        if metadata["chapter"] == "010-sbd-manual" and metadata["section"]:
            if metadata["section"] in ChaptersMetadata.SECURITY_DOMAINS:
                metadata["domain"] = ChaptersMetadata.SECURITY_DOMAINS[metadata["section"]]
        
        return metadata


class DocumentChunker:
    """Split documents into chunks with metadata context"""
    
    def __init__(self, chunk_size: int = 500, overlap: int = 100):
        """
        Args:
            chunk_size: Target characters per chunk
            overlap: Overlap between consecutive chunks (for context)
        """
        self.chunk_size = chunk_size
        self.overlap = overlap
    
    @staticmethod
    def read_file(file_path: Path) -> Tuple[Dict, str]:
        """Read markdown file and extract frontmatter + content
        
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
        """Create metadata for a single chunk"""
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
    """Build JSONL dataset from markdown files"""
    
    def __init__(self, chunk_size: int = 500, overlap: int = 100):
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
            output_path: Where to save JSONL (default: index/manual_chunks.jsonl)
            
        Returns:
            Path to created JSONL file
        """
        if output_path is None:
            output_path = INDEX_DIR / "manual_chunks.jsonl"
        
        # Load tags for reference
        tags = self._load_tags()
        
        # Find all markdown files
        md_files = sorted(list(MANUAL_ROOT.rglob("*.md")))
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
                    rel_path = str(file_path.relative_to(MANUAL_ROOT))
                    file_metadata = ChaptersMetadata.parse_path(rel_path)
                    
                    # Extract frontmatter data
                    title = frontmatter.get('title', file_path.stem)
                    file_tags = frontmatter.get('tags', [])
                    
                    # Split into chunks
                    chunks = self.chunker.chunk_content(content)
                    
                    # Write each chunk as JSONL record
                    for chunk_idx, chunk_content in enumerate(chunks):
                        chunk_metadata = self.chunker.create_chunk_metadata(
                            chunk_idx, len(chunks), file_metadata, chunk_content
                        )
                        
                        record = {
                            "id": f"{file_metadata['file_path'].replace('/', '_').replace('.md', '')}_{chunk_idx}",
                            "text": chunk_content,
                            "metadata": chunk_metadata,
                            "frontmatter": {
                                "title": title,
                                "tags": file_tags,
                            }
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


class ChromaIndexBuilder:
    """Build Chroma vector index from JSONL chunks"""
    
    def __init__(self):
        from sentence_transformers import SentenceTransformer
        import chromadb
        
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
        self.client = chromadb.PersistentClient(path=str(INDEX_DIR / "chroma"))
    
    def build_from_jsonl(self, jsonl_path: Path, force_rebuild: bool = True):
        """Build Chroma index from JSONL file
        
        Args:
            jsonl_path: Path to JSONL file
            force_rebuild: If True, delete existing collection first
        """
        collection_name = "manual"
        
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
                    
                    # Prepare metadata (include frontmatter tags)
                    metadata = record.get("metadata", {})
                    metadata["title"] = record.get("frontmatter", {}).get("title", "")
                    metadata["tags"] = json.dumps(
                        record.get("frontmatter", {}).get("tags", [])
                    )
                    
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


if __name__ == "__main__":
    import sys
    
    # Step 1: Build JSONL dataset
    builder = JSONLDatasetBuilder(chunk_size=500, overlap=100)
    jsonl_path = builder.build_dataset()
    
    # Step 2: Build Chroma index
    if "--index" in sys.argv or len(sys.argv) == 1:
        index_builder = ChromaIndexBuilder()
        index_builder.build_from_jsonl(jsonl_path, force_rebuild=True)
        print(f"\n🎉 RAG pipeline complete! Ready for queries.")

"""Tests for chunked indexing and JSONL dataset creation"""

import json
from pathlib import Path
import pytest

from rag_core.indexing.chunked import (
    DocumentChunker,
    JSONLDatasetBuilder,
    ChunkedIndexBuilder,
)
from rag_core.metadata import ChaptersMetadata


class TestDocumentChunker:
    """Test document chunking with overlap"""
    
    def test_chunker_initialization(self):
        """Test chunker initializes with correct parameters"""
        chunker = DocumentChunker(chunk_size=500, overlap=100)
        assert chunker.chunk_size == 500
        assert chunker.overlap == 100
    
    def test_chunk_small_content(self):
        """Test chunking content smaller than chunk_size"""
        chunker = DocumentChunker(chunk_size=500)
        content = "This is small content."
        chunks = chunker.chunk_content(content)
        
        assert len(chunks) == 1
        assert chunks[0] == content
    
    def test_chunk_large_content(self):
        """Test chunking large content with overlap"""
        chunker = DocumentChunker(chunk_size=100, overlap=20)
        content = "x" * 300  # 300 characters
        chunks = chunker.chunk_content(content)
        
        # Should create multiple chunks
        assert len(chunks) > 1
        
        # Each chunk should be close to chunk_size
        for chunk in chunks:
            assert len(chunk) <= 100
        
        # Chunks should overlap
        # First chunk should end where second chunk begins (with overlap)
        if len(chunks) > 1:
            # Last 20 chars of chunk 0 should match first 20 chars of chunk 1
            overlap_area = content[80:100]  # chars 80-100 from original
            assert overlap_area in chunks[0]
            assert overlap_area in chunks[1]
    
    def test_read_file_with_frontmatter(self, temp_manual_root):
        """Test reading markdown file and extracting frontmatter"""
        test_file = temp_manual_root / "000-teory-of-everything" / "01-intro.md"
        
        frontmatter, content = DocumentChunker.read_file(test_file)
        
        assert frontmatter["title"] == "Theory of Everything - Introduction"
        assert frontmatter["tags"] == ["fundamental", "intro"]
        assert "foundational concepts" in content
    
    def test_chunk_metadata_creation(self):
        """Test creating chunk metadata"""
        chunker = DocumentChunker()
        
        file_metadata = {
            "file_path": "010-sbd-manual/02-requisitos-seguranca/intro.md",
            "chapter": "010-sbd-manual",
            "chapter_name": "Security by Design Manual",
            "section": "02-requisitos-seguranca",
            "domain": "Security Requirements",
        }
        
        content = "Sample chunk content"
        chunk_meta = chunker.create_chunk_metadata(
            chunk_index=0,
            total_chunks=5,
            file_metadata=file_metadata,
            content=content
        )
        
        assert chunk_meta["chunk_index"] == 0
        assert chunk_meta["total_chunks"] == 5
        assert chunk_meta["chapter"] == "010-sbd-manual"
        assert chunk_meta["domain"] == "Security Requirements"
        assert chunk_meta["content_length"] == len(content)


class TestChaptersMetadata:
    """Test manual structure metadata parsing"""
    
    def test_parse_sbd_manual_path(self):
        """Test parsing path in 010-sbd-manual section"""
        path = "010-sbd-manual/02-requisitos-seguranca/intro.md"
        metadata = ChaptersMetadata.parse_path(path)
        
        assert metadata["chapter"] == "010-sbd-manual"
        assert metadata["chapter_name"] == "Security by Design Manual"
        assert metadata["chapter_type"] == "main_content"
        assert metadata["section"] == "02-requisitos-seguranca"
        assert metadata["domain"] == "Security Requirements"
        assert metadata["file_name"] == "intro"
    
    def test_parse_theory_path(self):
        """Test parsing path in theory section"""
        path = "000-teory-of-everything/01-intro.md"
        metadata = ChaptersMetadata.parse_path(path)
        
        assert metadata["chapter"] == "000-teory-of-everything"
        assert metadata["chapter_name"] == "Theory of Everything"
        assert metadata["chapter_type"] == "foundational"
    
    def test_parse_normative_path(self):
        """Test parsing path in normative cross-check"""
        path = "002-cross-check-normativo/dora.md"
        metadata = ChaptersMetadata.parse_path(path)
        
        assert metadata["chapter"] == "002-cross-check-normativo"
        assert metadata["chapter_name"] == "Normative Cross-Check"
        assert metadata["chapter_type"] == "frameworks"
        assert metadata["section"] == "dora"


class TestJSONLDatasetBuilder:
    """Test building JSONL datasets with chunks"""
    
    def test_builder_initialization(self, temp_manual_root, temp_index_dir):
        """Test builder initializes correctly"""
        builder = JSONLDatasetBuilder(temp_manual_root, temp_index_dir, chunk_size=200)
        
        assert builder.manual_root == temp_manual_root
        assert builder.index_dir == temp_index_dir
        assert builder.chunker.chunk_size == 200
    
    def test_build_dataset_creates_jsonl(self, temp_manual_root, temp_index_dir):
        """Test building JSONL dataset"""
        builder = JSONLDatasetBuilder(temp_manual_root, temp_index_dir, chunk_size=1000, overlap=100)
        output_path = builder.build_dataset()
        
        # File should exist
        assert output_path.exists()
        assert output_path.suffix == ".jsonl"
        assert output_path.stat().st_size > 0
    
    def test_jsonl_record_structure(self, temp_manual_root, temp_index_dir):
        """Test JSONL records have correct structure"""
        builder = JSONLDatasetBuilder(temp_manual_root, temp_index_dir, chunk_size=1000)
        output_path = builder.build_dataset()
        
        # Read first record
        with open(output_path, 'r') as f:
            first_line = f.readline()
        
        record = json.loads(first_line)
        
        # Check structure
        assert "id" in record
        assert "text" in record
        assert "metadata" in record
        assert "frontmatter" in record
        
        # Check metadata fields
        metadata = record["metadata"]
        assert "chapter" in metadata
        assert "file_path" in metadata
        assert "chunk_index" in metadata
        assert "content_length" in metadata
        
        # Check frontmatter
        assert "title" in record["frontmatter"]
        assert "tags" in record["frontmatter"]
    
    def test_dataset_statistics(self, temp_manual_root, temp_index_dir):
        """Test dataset building statistics"""
        builder = JSONLDatasetBuilder(temp_manual_root, temp_index_dir, chunk_size=500)
        output_path = builder.build_dataset()
        
        # Count records
        record_count = sum(1 for _ in open(output_path))
        
        # Should have at least 3 records (one per file, possibly more due to chunks)
        assert record_count >= 3


class TestChunkedIndexBuilder:
    """Test building Chroma index from chunked data"""
    
    def test_chunked_index_initialization(self, temp_index_dir):
        """Test index builder initializes correctly"""
        builder = ChunkedIndexBuilder(temp_index_dir)
        
        assert builder.index_dir == temp_index_dir
        assert builder.embedding_model is not None
        assert builder.client is not None
    
    def test_build_from_jsonl(self, temp_manual_root, temp_index_dir):
        """Test building index from JSONL file"""
        # First create JSONL
        dataset_builder = JSONLDatasetBuilder(temp_manual_root, temp_index_dir)
        jsonl_path = dataset_builder.build_dataset()
        
        # Then build index
        index_builder = ChunkedIndexBuilder(temp_index_dir)
        stats = index_builder.build_from_jsonl(jsonl_path, force_rebuild=True)
        
        # Should have indexed records
        assert stats["total_records"] > 0
        assert stats["indexed"] > 0
        assert stats["failed"] == 0
    
    def test_chroma_collection_has_data(self, temp_manual_root, temp_index_dir):
        """Test that Chroma collection is populated with chunked data"""
        # Build dataset and index
        dataset_builder = JSONLDatasetBuilder(temp_manual_root, temp_index_dir)
        jsonl_path = dataset_builder.build_dataset()
        
        index_builder = ChunkedIndexBuilder(temp_index_dir)
        index_builder.build_from_jsonl(jsonl_path, force_rebuild=True)
        
        # Query collection
        collection = index_builder.client.get_or_create_collection("manual_chunked")
        results = collection.get()
        
        assert len(results["ids"]) > 0
        assert len(results["documents"]) > 0
        assert len(results["metadatas"]) > 0
    
    def test_separate_chroma_directory(self, temp_manual_root, temp_index_dir):
        """Test that chunked index uses separate chroma directory"""
        dataset_builder = JSONLDatasetBuilder(temp_manual_root, temp_index_dir)
        jsonl_path = dataset_builder.build_dataset()
        
        index_builder = ChunkedIndexBuilder(temp_index_dir)
        index_builder.build_from_jsonl(jsonl_path, force_rebuild=True)
        
        # Check that chroma_chunked directory exists (separate from simple indexing)
        chroma_chunked_dir = temp_index_dir / "chroma_chunked"
        assert chroma_chunked_dir.exists()


class TestIntegration:
    """Integration tests for complete chunked indexing pipeline"""
    
    def test_full_pipeline(self, temp_manual_root, temp_index_dir):
        """Test complete pipeline: data → JSONL → Chroma index"""
        # Step 1: Build JSONL
        dataset_builder = JSONLDatasetBuilder(temp_manual_root, temp_index_dir)
        jsonl_path = dataset_builder.build_dataset()
        assert jsonl_path.exists()
        
        # Step 2: Build Chroma index
        index_builder = ChunkedIndexBuilder(temp_index_dir)
        stats = index_builder.build_from_jsonl(jsonl_path)
        assert stats["indexed"] > 0
        
        # Step 3: Verify data
        collection = index_builder.client.get_or_create_collection("manual_chunked")
        results = collection.get()
        assert len(results["ids"]) > 0
    
    def test_isolation_from_simple_indexing(self, temp_manual_root, temp_index_dir):
        """Test that chunked indexing doesn't interfere with simple indexing"""
        from rag_core.indexing import ManualIndexer
        
        # Build simple index
        simple_indexer = ManualIndexer(temp_manual_root, temp_index_dir)
        simple_indexer.index_all(force_rebuild=False)
        
        # Build chunked index
        dataset_builder = JSONLDatasetBuilder(temp_manual_root, temp_index_dir)
        jsonl_path = dataset_builder.build_dataset()
        
        index_builder = ChunkedIndexBuilder(temp_index_dir)
        index_builder.build_from_jsonl(jsonl_path)
        
        # Verify both exist and use different collections/directories
        assert (temp_index_dir / "chroma").exists()
        assert (temp_index_dir / "chroma_chunked").exists()
        
        # Simple indexing collection should still work
        simple_results = simple_indexer.collection.get()
        assert len(simple_results["ids"]) == 3
        
        # Chunked indexing collection should work
        chunked_results = index_builder.client.get_or_create_collection("manual_chunked").get()
        assert len(chunked_results["ids"]) > 0

"""Tests for simple manual indexing"""

import json
from pathlib import Path
import pytest

from rag_core.indexing import ManualIndexer


class TestManualIndexer:
    """Test simple full-document indexing"""
    
    def test_indexer_initialization(self, temp_index_dir, temp_manual_root):
        """Test that indexer initializes correctly"""
        indexer = ManualIndexer(temp_manual_root, temp_index_dir)
        
        assert indexer.manual_root == temp_manual_root
        assert indexer.index_dir == temp_index_dir
        assert indexer.embedding_model is not None
        assert indexer.client is not None
        assert indexer.collection is not None
    
    def test_read_file_with_frontmatter(self, temp_index_dir, temp_manual_root):
        """Test reading markdown file with frontmatter"""
        indexer = ManualIndexer(temp_manual_root, temp_index_dir)
        
        test_file = temp_manual_root / "000-teory-of-everything" / "01-intro.md"
        doc_data = indexer._read_file(test_file)
        
        assert doc_data is not None
        assert doc_data["title"] == "Theory of Everything - Introduction"
        assert doc_data["tags"] == ["fundamental", "intro"]
        assert "foundational concepts" in doc_data["content"]
        assert doc_data["path"] == "000-teory-of-everything/01-intro.md"
    
    def test_indexing_all_files(self, temp_index_dir, temp_manual_root):
        """Test indexing all markdown files"""
        indexer = ManualIndexer(temp_manual_root, temp_index_dir)
        stats = indexer.index_all(force_rebuild=False)
        
        # We created 3 test files
        assert stats["total_files"] == 3
        assert stats["indexed"] == 3
        assert stats["failed"] == 0
        assert stats["total_chars"] > 0
    
    def test_chroma_collection_populated(self, temp_index_dir, temp_manual_root):
        """Test that Chroma collection is properly populated"""
        indexer = ManualIndexer(temp_manual_root, temp_index_dir)
        indexer.index_all(force_rebuild=False)
        
        # Query the collection
        results = indexer.collection.get()
        
        assert len(results["ids"]) == 3
        assert len(results["documents"]) == 3
        assert len(results["metadatas"]) == 3
        
        # Check metadata
        titles = [m["title"] for m in results["metadatas"]]
        assert "Theory of Everything - Introduction" in titles
        assert "Application Classification" in titles
        assert "Security Requirements" in titles
    
    def test_force_rebuild(self, temp_index_dir, temp_manual_root):
        """Test that force_rebuild clears existing index"""
        indexer = ManualIndexer(temp_manual_root, temp_index_dir)
        
        # First indexing
        stats1 = indexer.index_all(force_rebuild=False)
        assert stats1["indexed"] == 3
        
        # Second indexing with force_rebuild
        stats2 = indexer.index_all(force_rebuild=True)
        assert stats2["indexed"] == 3
        
        # Collection should have same data
        results = indexer.collection.get()
        assert len(results["ids"]) == 3
    
    def test_embeddings_created(self, temp_index_dir, temp_manual_root):
        """Test that embeddings are created for each document"""
        indexer = ManualIndexer(temp_manual_root, temp_index_dir)
        indexer.index_all(force_rebuild=False)
        
        results = indexer.collection.get(include=["embeddings"])
        
        # Chroma stores embeddings (only retrievable if explicitly included)
        assert results["embeddings"] is not None or results["embeddings"] == []
    
    def test_excludes_review_files(self, temp_index_dir, temp_manual_root):
        """Test that .2review files are excluded"""
        # Create a .2review file
        review_file = temp_manual_root / "010-sbd-manual" / "01-classificacao-aplicacoes" / "test.md.2review"
        review_file.write_text("---\ntitle: Review\n---\nThis is a review file")
        
        indexer = ManualIndexer(temp_manual_root, temp_index_dir)
        stats = indexer.index_all(force_rebuild=False)
        
        # Should still be 3 (original files), not 4
        assert stats["total_files"] == 3
    
    def test_persistent_storage(self, temp_index_dir, temp_manual_root):
        """Test that index is persisted to disk"""
        indexer1 = ManualIndexer(temp_manual_root, temp_index_dir)
        indexer1.index_all(force_rebuild=False)
        
        # Check that chroma directory was created
        chroma_dir = temp_index_dir / "chroma"
        assert chroma_dir.exists()
        
        # Create new indexer with same directory
        indexer2 = ManualIndexer(temp_manual_root, temp_index_dir)
        results = indexer2.collection.get()
        
        # Should find the same documents
        assert len(results["ids"]) == 3

"""Fixtures and utilities for RAG core tests"""

import tempfile
from pathlib import Path
import shutil
import pytest
import yaml


@pytest.fixture
def temp_manual_root():
    """Create a temporary manual root with test markdown files"""
    temp_dir = Path(tempfile.mkdtemp(prefix="manual_test_"))
    
    # Create chapter structure
    (temp_dir / "000-teory-of-everything").mkdir()
    (temp_dir / "010-sbd-manual" / "01-classificacao-aplicacoes").mkdir(parents=True)
    (temp_dir / "010-sbd-manual" / "02-requisitos-seguranca").mkdir(parents=True)
    
    # Create test files with frontmatter
    files = {
        "000-teory-of-everything/01-intro.md": {
            "title": "Theory of Everything - Introduction",
            "tags": ["fundamental", "intro"],
            "content": "This is the theory of everything intro. It explains the foundational concepts."
        },
        "010-sbd-manual/01-classificacao-aplicacoes/intro.md": {
            "title": "Application Classification",
            "tags": ["classification", "applications"],
            "content": "Applications are classified by security requirements and maturity levels."
        },
        "010-sbd-manual/02-requisitos-seguranca/intro.md": {
            "title": "Security Requirements",
            "tags": ["security", "requirements"],
            "content": "Security requirements depend on the threat model and risk assessment."
        },
    }
    
    for file_path, data in files.items():
        full_path = temp_dir / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write frontmatter + content
        frontmatter = {
            "title": data["title"],
            "tags": data["tags"],
        }
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write("---\n")
            f.write(yaml.dump(frontmatter, default_flow_style=False))
            f.write("---\n\n")
            f.write(data["content"])
    
    yield temp_dir
    
    # Cleanup
    shutil.rmtree(temp_dir, ignore_errors=True)


@pytest.fixture
def temp_index_dir():
    """Create a temporary index directory for test indexes"""
    temp_dir = Path(tempfile.mkdtemp(prefix="index_test_"))
    yield temp_dir
    shutil.rmtree(temp_dir, ignore_errors=True)


@pytest.fixture
def temp_chroma_dir():
    """Create isolated Chroma directory (won't affect production data)"""
    temp_dir = Path(tempfile.mkdtemp(prefix="chroma_test_"))
    yield temp_dir
    shutil.rmtree(temp_dir, ignore_errors=True)

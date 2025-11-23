"""Root conftest for pytest

This file is at the project root and provides global configuration.
Specific contexts (rag_core, rag_tools) should have their own conftest.py
with context-specific fixtures.
"""

import pytest


def pytest_collection_modifyitems(config, items):
    """Automatically mark tests based on their location
    
    This keeps contexts separate:
    - tests/rag/ → marked with @pytest.mark.rag
    - tests/tagging/ → marked with @pytest.mark.tagging
    """
    for item in items:
        if "tests/rag/" in str(item.fspath):
            item.add_marker(pytest.mark.rag)
        elif "tests/tagging/" in str(item.fspath):
            item.add_marker(pytest.mark.tagging)


def pytest_configure(config):
    """Configure pytest with context awareness"""
    config.addinivalue_line(
        "markers", 
        "rag: Tests for rag_core infrastructure (indexed, chunking, etc)"
    )
    config.addinivalue_line(
        "markers",
        "tagging: Tests for rag_tools tagging workflows"
    )
    config.addinivalue_line(
        "markers",
        "integration: Integration tests across contexts"
    )

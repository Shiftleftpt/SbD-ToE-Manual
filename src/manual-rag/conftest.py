"""Root conftest for pytest

Global pytest configuration and auto-marking.
Tests live in their respective modules:
- rag_core/tests/ → for rag_core infrastructure
- rag_tools/tests/ → for rag_tools workflows
"""

import pytest


def pytest_collection_modifyitems(config, items):
    """Automatically mark tests based on their location"""
    for item in items:
        if "rag_core/tests/" in str(item.fspath):
            item.add_marker(pytest.mark.rag)
        elif "rag_tools/tests/" in str(item.fspath):
            item.add_marker(pytest.mark.tagging)


def pytest_configure(config):
    """Configure pytest markers"""
    config.addinivalue_line(
        "markers", 
        "rag: Tests for rag_core infrastructure"
    )
    config.addinivalue_line(
        "markers",
        "tagging: Tests for rag_tools tagging"
    )
    config.addinivalue_line(
        "markers",
        "integration: Integration tests"
    )

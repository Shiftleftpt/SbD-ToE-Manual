"""Root conftest for pytest

Automatic marking of tests based on their location within modules.
Tests should live in the module they test (not in a root tests/ folder).
"""

import pytest


def pytest_collection_modifyitems(config, items):
    """Automatically mark tests based on their module location
    
    This keeps tests organized within their modules:
    - rag_core/tests/ → marked with @pytest.mark.rag_core
    - rag_tools/tagging/tests/ → marked with @pytest.mark.tagging
    - rag_tools/workflows/tests/ → marked with @pytest.mark.workflows
    - rag_tools/utils/tests/ → marked with @pytest.mark.utils
    """
    for item in items:
        path_str = str(item.fspath)
        
        if "rag_core/tests/" in path_str:
            item.add_marker(pytest.mark.rag_core)
        elif "rag_tools/tagging/tests/" in path_str:
            item.add_marker(pytest.mark.tagging)
        elif "rag_tools/workflows/tests/" in path_str:
            item.add_marker(pytest.mark.workflows)
        elif "rag_tools/utils/tests/" in path_str:
            item.add_marker(pytest.mark.utils)


def pytest_configure(config):
    """Configure pytest with module markers"""
    config.addinivalue_line(
        "markers", 
        "rag_core: RAG core infrastructure tests (indexing, query, metadata)"
    )
    config.addinivalue_line(
        "markers",
        "tagging: RAG tools tagging workflow tests"
    )
    config.addinivalue_line(
        "markers",
        "workflows: RAG tools workflow tests"
    )
    config.addinivalue_line(
        "markers",
        "utils: RAG tools utilities tests"
    )

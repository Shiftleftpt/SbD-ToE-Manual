#!/usr/bin/env python3
"""
Run tests for RAG system with module-based organization.

Tests are now located within their respective modules:
- rag_core/tests/          - RAG infrastructure tests
- rag_tools/tagging/tests/ - Tagging workflow tests
- rag_tools/workflows/tests/ - Workflow orchestration tests
- rag_tools/utils/tests/   - Utility function tests

Usage:
    python run_tests.py                    # Run all tests
    python run_tests.py rag_core           # Run only RAG core tests
    python run_tests.py tagging            # Run only tagging tests
    python run_tests.py workflows          # Run only workflow tests
    python run_tests.py utils              # Run only utils tests
    python run_tests.py -v                 # Run all tests verbose
    python run_tests.py rag_core -v        # Run RAG core tests verbose
"""

import sys
import subprocess
from pathlib import Path


def get_test_path(module: str) -> Path:
    """Get test path for a module."""
    paths = {
        "rag_core": Path("rag_core/tests"),
        "tagging": Path("rag_tools/tagging/tests"),
        "workflows": Path("rag_tools/workflows/tests"),
        "utils": Path("rag_tools/utils/tests"),
    }
    return paths.get(module)


def run_tests(args: list[str]) -> int:
    """Run pytest with given arguments."""
    cmd = ["pytest"] + args
    result = subprocess.run(cmd, cwd=Path(__file__).parent)
    return result.returncode


def main():
    """Main entry point."""
    args = sys.argv[1:]
    
    # No arguments - run all tests
    if not args:
        print("Running all tests...")
        return run_tests([])
    
    # Check if first arg is a module name
    module = args[0]
    test_path = get_test_path(module)
    
    if test_path and test_path.exists():
        # First argument is a valid module
        print(f"Running {module} tests from {test_path}...")
        return run_tests([str(test_path)] + args[1:])
    
    # First argument is not a module, pass all args to pytest
    print("Running pytest with custom arguments...")
    return run_tests(args)


if __name__ == "__main__":
    sys.exit(main())

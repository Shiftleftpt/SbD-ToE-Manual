#!/usr/bin/env python3
"""Helper script to run tests with context awareness

Usage:
    python run_tests.py                    # Run all tests
    python run_tests.py rag                # Run only RAG core tests
    python run_tests.py tagging            # Run only tagging tests
    python run_tests.py rag -v             # Verbose RAG tests
    python run_tests.py rag --coverage     # With coverage
    
Tests are organized by module:
- rag_core/tests/ → Infrastructure tests
- rag_tools/tests/ → Tagging tests
"""

import subprocess
import sys
from pathlib import Path


def main():
    """Run tests with pytest, respecting module organization"""
    try:
        import pytest
    except ImportError:
        print("ERROR: pytest not installed")
        print("Install with: pip install -r requirements.txt")
        return 1
    
    # Default: run all tests
    test_context = None
    pytest_args = []
    
    # Parse arguments
    if len(sys.argv) > 1:
        first_arg = sys.argv[1]
        if first_arg in ["rag", "tagging"]:
            test_context = first_arg
            # Remaining args go to pytest
            pytest_args = sys.argv[2:]
        elif first_arg in ["-h", "--help"]:
            print(__doc__)
            return 0
        else:
            # Treat as pytest argument
            pytest_args = sys.argv[1:]
    
    # Build pytest command
    cmd = ["pytest"]
    
    if test_context == "rag":
        cmd.append("rag_core/tests/")
        print("🧪 Running RAG Core tests")
        print("   Location: rag_core/tests/")
        print("   Module: rag_core\n")
    elif test_context == "tagging":
        cmd.append("rag_tools/tests/")
        print("🏷️  Running Tagging tests")
        print("   Location: rag_tools/tests/")
        print("   Module: rag_tools\n")
    else:
        # Run all
        print("🧪 Running all tests")
        print("   - rag_core/tests/")
        print("   - rag_tools/tests/\n")
    
    # Add pytest arguments
    if "--coverage" in pytest_args:
        pytest_args.remove("--coverage")
        cov_module = "rag_core" if test_context == "rag" else "rag_tools" if test_context == "tagging" else ""
        if cov_module:
            cmd.extend([
                f"--cov={cov_module}",
                "--cov-report=html",
                "--cov-report=term"
            ])
        else:
            # No context specified, measure both
            cmd.extend([
                "--cov=rag_core",
                "--cov=rag_tools",
                "--cov-report=html",
                "--cov-report=term"
            ])
        print("📊 Coverage report will be saved to: htmlcov/index.html\n")
    
    # Add remaining args
    cmd.extend(pytest_args)
    
    print(f"Running: {' '.join(cmd)}\n")
    print("=" * 60)
    
    # Run pytest
    result = subprocess.run(cmd)
    
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())

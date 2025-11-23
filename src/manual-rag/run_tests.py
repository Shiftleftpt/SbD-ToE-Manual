#!/usr/bin/env python3
"""Helper script to run tests with context awareness

Usage:
    python run_tests.py                    # Run all tests
    python run_tests.py rag                # Run only RAG core tests
    python run_tests.py tagging            # Run only tagging tests
    python run_tests.py rag -v             # Verbose RAG tests
    python run_tests.py rag --coverage     # With coverage
    
This maintains separation between RAG and tagging contexts.
Each context runs independently without interference.
"""

import subprocess
import sys
from pathlib import Path


def main():
    """Run tests with pytest, respecting context separation"""
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
        cmd.append("tests/rag/")
        print("🧪 Running RAG Core tests (context isolation)")
        print("   Location: tests/rag/")
        print("   Coverage: rag_core only\n")
    elif test_context == "tagging":
        cmd.append("tests/tagging/")
        print("🏷️  Running Tagging tests (context isolation)")
        print("   Location: tests/tagging/")
        print("   Coverage: rag_tools only\n")
    else:
        # Run all, but separately for clarity
        print("🧪 Running all tests")
        print("   - RAG Core (tests/rag/)")
        print("   - Tagging (tests/tagging/)\n")
    
    # Add pytest arguments
    if "--coverage" in pytest_args:
        pytest_args.remove("--coverage")
        cmd.extend([
            "--cov=rag_core" if not test_context or test_context == "rag" else "--cov=rag_tools",
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

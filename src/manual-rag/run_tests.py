#!/usr/bin/env python3
"""Helper script to run RAG core tests safely

Usage:
    python run_tests.py                    # Run all tests
    python run_tests.py -v                 # Verbose output
    python run_tests.py --coverage         # With coverage report
    python run_tests.py test_indexing.py   # Run specific test file
"""

import subprocess
import sys
from pathlib import Path


def main():
    """Run tests with pytest"""
    # Ensure pytest is available
    try:
        import pytest
    except ImportError:
        print("ERROR: pytest not installed")
        print("Install with: pip install pytest pytest-cov")
        return 1
    
    test_dir = Path(__file__).parent / "tests" / "rag"
    
    # Build pytest command
    cmd = ["pytest", str(test_dir)]
    
    # Add additional arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "--coverage":
            cmd.extend([
                "--cov=rag_core",
                "--cov-report=html",
                "--cov-report=term"
            ])
            print("Running tests with coverage...")
            print("Coverage report will be saved to htmlcov/index.html")
        else:
            cmd.extend(sys.argv[1:])
    
    print(f"Running: {' '.join(cmd)}\n")
    
    # Run pytest
    result = subprocess.run(cmd)
    
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())

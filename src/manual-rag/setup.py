#!/usr/bin/env python3
"""
setup.py - Complete RAG setup and initialization
Run this on any new machine or checkout to get the RAG system ready.

Usage: python3 setup.py
"""

import subprocess
import sys
import os
import shutil
from pathlib import Path

# ANSI color codes
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"


def run_command(cmd, description="", show_output=False):
    """Run a shell command and handle errors."""
    print(f"{YELLOW}→ {description}...{RESET}")
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=not show_output,
            text=True,
            check=True,
        )
        print(f"{GREEN}✅ {description}{RESET}")
        if result.stdout and not show_output:
            return result.stdout.strip()
        return True
    except subprocess.CalledProcessError as e:
        print(f"{RED}❌ {description} failed{RESET}")
        if e.stdout:
            print(e.stdout)
        if e.stderr:
            print(e.stderr)
        sys.exit(1)


def main():
    print(f"\n{GREEN}{'=' * 50}{RESET}")
    print(f"{GREEN}🚀 Manual RAG - Setup & Initialization{RESET}")
    print(f"{GREEN}{'=' * 50}{RESET}\n")

    # Check Python version
    version = sys.version_info
    print(f"{YELLOW}→ Checking Python version...{RESET}")
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"{RED}❌ Python 3.8+ required (found {version.major}.{version.minor}){RESET}")
        sys.exit(1)
    print(f"{GREEN}✅ Python {version.major}.{version.minor}.{version.micro} found{RESET}\n")

    # Step 1: Create virtual environment
    venv_path = Path("rag_env")
    if not venv_path.exists():
        print(f"{YELLOW}→ Creating virtual environment...{RESET}")
        run_command(
            f"{sys.executable} -m venv rag_env",
            "Virtual environment creation",
        )
    else:
        print(f"{YELLOW}→ Virtual environment already exists{RESET}")
        print(f"{GREEN}✅ Virtual environment found{RESET}\n")

    # Step 2: Determine pip command
    if sys.platform == "win32":
        pip_cmd = "rag_env\\Scripts\\pip"
        python_cmd = "rag_env\\Scripts\\python"
    else:
        pip_cmd = "rag_env/bin/pip"
        python_cmd = "rag_env/bin/python3"

    # Step 3: Install dependencies
    print()
    run_command(
        f"{pip_cmd} install --upgrade pip setuptools wheel",
        "Upgrading pip",
    )
    run_command(
        f"{pip_cmd} install -r requirements.txt",
        "Installing dependencies",
        show_output=True,
    )

    # Step 4: Build index
    print()
    print(f"{YELLOW}→ Building RAG index...{RESET}")
    print(f"   (This may take 2-3 minutes)\n")
    run_command(
        f"{python_cmd} -m rag_core.indexing.chunked_build",
        "Index building",
        show_output=True,
    )

    # Step 5: Run tests
    print()
    run_command(
        f"{python_cmd} -m pytest rag_core/tests/ -q",
        "Running tests",
        show_output=True,
    )

    # Summary
    print(f"\n{GREEN}{'=' * 50}{RESET}")
    print(f"{GREEN}✨ Setup Complete! ✨{RESET}")
    print(f"{GREEN}{'=' * 50}{RESET}")

    activation_cmd = (
        "rag_env\\Scripts\\activate" if sys.platform == "win32" else "source rag_env/bin/activate"
    )

    print(f"\n{YELLOW}Next steps:{RESET}")
    print(f"1. Activate environment on future sessions:")
    print(f"   {activation_cmd}")
    print()
    print(f"2. Run auto-tagging workflow:")
    print(f"   {python_cmd} -m rag_tools.workflows.generate_review_report --max-tags 7")
    print()
    print(f"3. Run tests anytime:")
    print(f"   {python_cmd} -m pytest")
    print()
    print(f"{GREEN}📚 See README.md for full documentation{RESET}\n")


if __name__ == "__main__":
    main()

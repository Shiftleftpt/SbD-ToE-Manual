#!/bin/bash
# Setup script for Tag Normalization & Inference Engine
# Creates Python virtual environment and installs dependencies

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VENV_DIR="${SCRIPT_DIR}/.venv"

echo "🔧 Setting up Tag Normalization environment..."
echo "📁 Working directory: $SCRIPT_DIR"

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python version: $PYTHON_VERSION"

# Create virtual environment
if [ ! -d "$VENV_DIR" ]; then
    echo "📦 Creating virtual environment at .venv..."
    python3 -m venv "$VENV_DIR"
    echo "✓ Virtual environment created"
else
    echo "ℹ️  Virtual environment already exists"
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Upgrade pip
echo "⬆️  Upgrading pip, setuptools, wheel..."
pip install --upgrade pip setuptools wheel > /dev/null 2>&1
echo "✓ pip upgraded"

# Install requirements
if [ -f "${SCRIPT_DIR}/requirements.txt" ]; then
    echo "📥 Installing dependencies from requirements.txt..."
    pip install -r "${SCRIPT_DIR}/requirements.txt"
    echo "✓ Dependencies installed"
else
    echo "⚠️  requirements.txt not found, skipping dependency installation"
fi

# Show summary
echo ""
echo "✅ Setup complete!"
echo ""
echo "To use this environment:"
echo "  source $VENV_DIR/bin/activate"
echo ""
echo "To deactivate:"
echo "  deactivate"
echo ""
echo "To run inference:"
echo "  python3 infer/infer_tags.py infer"

#!/bin/bash
# Quick setup and test script for Manual RAG

set -e

echo "📚 Manual RAG System - Setup"
echo "=================================="
echo ""

# Check Python version
PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo "✓ Python $PYTHON_VERSION"

# Create venv
echo ""
echo "Setting up virtual environment..."
if [ ! -d "rag_env" ]; then
    python3 -m venv rag_env
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

# Activate venv
source rag_env/bin/activate
echo "✓ Virtual environment activated"

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install -q -r requirements.txt
echo "✓ Dependencies installed"

# Check Ollama
echo ""
echo "Checking Ollama setup..."
if ! command -v ollama &> /dev/null; then
    echo "⚠ Ollama not found. Install with:"
    echo "  brew install ollama"
else
    echo "✓ Ollama installed"
    
    # Check if running
    if curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
        echo "✓ Ollama is running"
        
        # Check for mistral model
        if curl -s http://localhost:11434/api/tags | grep -q "mistral"; then
            echo "✓ Mistral model available"
        else
            echo "⚠ Mistral model not found. Pull it with:"
            echo "  ollama pull mistral"
        fi
    else
        echo "⚠ Ollama not running. Start with:"
        echo "  ollama serve"
    fi
fi

# Test imports
echo ""
echo "Testing imports..."
python3 -c "from manual_rag.config import *; from manual_rag.local_llm import *; from manual_rag.indexing import *; from manual_rag.query import *" && echo "✓ All imports successful"

# Summary
echo ""
echo "=================================="
echo "✓ Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Start Ollama: ollama serve"
echo "  2. Build index: python3 build_index.py"
echo "  3. Try a query: python3 -m manual_rag search 'authentication'"
echo ""

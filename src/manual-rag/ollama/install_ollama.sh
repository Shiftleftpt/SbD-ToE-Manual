#!/bin/bash
# Install Ollama + Mistral model
# Usage: bash install_ollama.sh

set -e

echo "🚀 Ollama + Mistral Installation Script"
echo "========================================"
echo ""

# Check if already installed
if command -v ollama &> /dev/null; then
    echo "✅ Ollama already installed at: $(which ollama)"
    ollama --version
else
    echo "📥 Installing Ollama..."
    
    # Check OS
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        echo "   Detected: macOS"
        echo "   Downloading Ollama installer..."
        
        # Download and install
        curl -fsSL https://ollama.ai/install.sh | sh 2>&1 | grep -E "(Installing|installed|Error)" || true
        
        # Wait for it to be available
        sleep 2
        
        if command -v ollama &> /dev/null; then
            echo "✅ Ollama installed successfully"
        else
            echo "⚠️  Ollama may not be in PATH. Trying /usr/local/bin/ollama..."
            if [ -f "/usr/local/bin/ollama" ]; then
                echo "✅ Found at /usr/local/bin/ollama"
                export PATH="/usr/local/bin:$PATH"
            else
                echo "❌ Failed to install Ollama"
                echo "   Try manual installation from: https://ollama.ai"
                exit 1
            fi
        fi
    else
        echo "❌ This script only supports macOS"
        echo "   Visit https://ollama.ai for other OS"
        exit 1
    fi
fi

echo ""
echo "📦 Downloading Mistral model..."
echo "   (This will download ~4GB, may take 5-10 minutes)"
echo ""

# Pull model
ollama pull mistral

echo ""
echo "✅ Mistral model ready!"
echo ""
echo "📋 To use Tagging Tools:"
echo ""
echo "   1. In Terminal 1 - Start Ollama server:"
echo "      ollama serve"
echo ""
echo "   2. In Terminal 2 - Run tagging:"
echo "      cd /Volumes/G-DRIVE/Shared/Manual-SbD-ToE/SbD-ToE-Manual/src/manual-rag"
echo "      source rag_env/bin/activate"
echo "      python3 rag_tools/tagging_tools/suggest_tags.py \"002-cross-check\" --top-n 15"
echo ""
echo "✨ Done!"

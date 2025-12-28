#!/bin/bash
# Quick start script for Tagging Tools
# Usage: bash run_tagging.sh [chapter] [--top-n N] [--max-docs N]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/../../rag_env"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}🏷️  Tagging Tools - Quick Start${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Check venv
if [ ! -d "$VENV_DIR" ]; then
    echo -e "${RED}❌ Virtual environment not found at: $VENV_DIR${NC}"
    echo "   Create it first: python3 -m venv rag_env"
    exit 1
fi

# Activate venv
echo -e "${YELLOW}📦 Activating virtual environment...${NC}"
source "$VENV_DIR/bin/activate"

# Check if Ollama is running
echo -e "${YELLOW}🔍 Checking Ollama server...${NC}"
if curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Ollama is running${NC}"
else
    echo -e "${YELLOW}⚠️  Ollama not running${NC}"
    echo "   To use Ollama, start it in another terminal:"
    echo "   ${BLUE}ollama serve${NC}"
    echo ""
    echo -e "${YELLOW}📌 Using local keyword extraction fallback${NC}"
fi

echo ""

# Run script
cd "$SCRIPT_DIR" || exit 1
python3 suggest_tags.py "$@"

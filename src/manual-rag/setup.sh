#!/bin/bash

# setup.sh - Complete RAG setup and initialization script
# Run this on any new machine or checkout to get the RAG system ready
# Usage: bash setup.sh

set -e  # Exit on error

echo "🚀 Manual RAG - Setup & Initialization"
echo "======================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 not found. Please install Python 3.8+${NC}"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo -e "${GREEN}✅ Python ${PYTHON_VERSION} found${NC}"

# Step 1: Create virtual environment if it doesn't exist
if [ ! -d "rag_env" ]; then
    echo -e "\n${YELLOW}📦 Creating virtual environment...${NC}"
    python3 -m venv rag_env
    echo -e "${GREEN}✅ Virtual environment created${NC}"
else
    echo -e "\n${YELLOW}📦 Virtual environment already exists${NC}"
fi

# Step 2: Activate virtual environment
echo -e "\n${YELLOW}🔌 Activating virtual environment...${NC}"
source rag_env/bin/activate
echo -e "${GREEN}✅ Virtual environment activated${NC}"

# Step 3: Upgrade pip and install requirements
echo -e "\n${YELLOW}📚 Installing dependencies...${NC}"
pip install --upgrade pip setuptools wheel > /dev/null 2>&1
pip install -r requirements.txt
echo -e "${GREEN}✅ Dependencies installed${NC}"

# Step 4: Build the index
echo -e "\n${YELLOW}🔨 Building RAG index...${NC}"
echo "   (This may take 2-3 minutes)"
python3 -m rag_core.indexing.chunked_build
echo -e "${GREEN}✅ RAG index built successfully${NC}"

# Step 5: Run tests to verify everything works
echo -e "\n${YELLOW}🧪 Running tests to verify setup...${NC}"
python3 -m pytest rag_core/tests/ -q
echo -e "${GREEN}✅ All tests passed${NC}"

# Summary
echo -e "\n${GREEN}════════════════════════════════════════${NC}"
echo -e "${GREEN}✨ Setup Complete! ✨${NC}"
echo -e "${GREEN}════════════════════════════════════════${NC}"

echo -e "\n${YELLOW}Next steps:${NC}"
echo "1. Activate environment on future sessions:"
echo "   source rag_env/bin/activate"
echo ""
echo "2. Run auto-tagging workflow:"
echo "   python3 -m rag_tools.workflows.generate_review_report --max-tags 7"
echo ""
echo "3. Run tests anytime:"
echo "   python3 -m pytest"
echo ""
echo -e "${GREEN}📚 See README.md for full documentation${NC}"

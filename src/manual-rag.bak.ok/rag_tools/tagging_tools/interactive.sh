#!/bin/bash
# Interactive Tagging Tool
# Easy-to-use wrapper for tag suggestions

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/../../rag_env"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}════════════════════════════════════════════${NC}"
echo -e "${BLUE}🏷️  Tagging Tools - Interactive${NC}"
echo -e "${BLUE}════════════════════════════════════════════${NC}"
echo ""

# Check venv
if [ ! -d "$VENV_DIR" ]; then
    echo "❌ Virtual environment not found"
    exit 1
fi

source "$VENV_DIR/bin/activate"

# Menu
echo "Capítulos Disponíveis:"
echo "  1) 002-cross-check-normativo (522 docs)"
echo "  2) 010-sbd-manual (4522 docs)"
echo "  3) tldr (22 docs)"
echo ""
read -p "Escolha um capítulo (1-3): " chapter_choice

case $chapter_choice in
    1) CHAPTER="002-cross-check" ;;
    2) CHAPTER="010-sbd-manual" ;;
    3) CHAPTER="tldr" ;;
    *) echo "Opção inválida"; exit 1 ;;
esac

echo ""
read -p "Número de tags por documento [15]: " tags_count
tags_count=${tags_count:-15}

echo ""
read -p "Máximo de documentos a analisar (deixe em branco para todos): " max_docs

echo ""
echo -e "${YELLOW}🔍 Verificando Ollama...${NC}"
if curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Ollama disponível - usando LLM para melhores sugestões${NC}"
else
    echo -e "${YELLOW}⚠️  Ollama não rodando - usando análise local${NC}"
fi

echo ""
echo -e "${BLUE}Iniciando análise...${NC}"
echo ""

cd "$SCRIPT_DIR" || exit 1

if [ -z "$max_docs" ]; then
    python3 suggest_tags.py "$CHAPTER" --top-n "$tags_count"
else
    python3 suggest_tags.py "$CHAPTER" --top-n "$tags_count" --max-docs "$max_docs"
fi

echo ""
echo -e "${GREEN}✅ Análise concluída!${NC}"
echo ""
echo -e "Relatório salvo em: ${BLUE}reports/${NC}"

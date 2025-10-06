#!/bin/bash
echo "🔍 Verificação de ambiente para exportação do manual SbD-ToE"

check() {
  if command -v "$1" >/dev/null 2>&1; then
    echo "✅ $1 encontrado"
  else
    echo "❌ $1 NÃO encontrado"
  fi
}

echo "📦 Ferramentas necessárias:"
check python3
check pandoc
check xelatex
check fc-list

echo ""
echo "📦 Bibliotecas necessárias (verificação parcial):"
python3 -c "import yaml" && echo "✅ PyYAML instalado" || echo "❌ PyYAML NÃO instalado"

echo ""
echo "🗂️ Diretórios esperados:"
[ -d "../doc_manual_src/docs/sbd-toe" ] && echo "✅ DOCS_SRC encontrado" || echo "❌ DOCS_SRC NÃO encontrado"
[ -f "book.yml" ] && echo "✅ book.yml encontrado" || echo "❌ book.yml NÃO encontrado"
[ -f "template.tex" ] && echo "✅ template.tex encontrado" || echo "❌ template.tex NÃO encontrado"
[ -f "parse_book_yaml.py" ] && echo "✅ parse_book_yaml.py encontrado" || echo "❌ parse_book_yaml.py NÃO encontrado"

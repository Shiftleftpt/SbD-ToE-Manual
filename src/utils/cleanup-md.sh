#!/bin/bash
# Corrige formatação Markdown: adiciona linha em branco após headers e blocos especiais

find . -name "*.md" | while read -r file; do
  echo "A corrigir $file"
  # 1. Adiciona linha em branco após headers se não existir
  sed -i '' -E '/^#{1,6}[^#]/ {
    N
    /[^#]\n[^[:space:]]/s/\n/\n\n/
  }' "$file"

  # 2. Adiciona linha em branco após blocos de listas (ex: ** item)
  sed -i '' -E '/^\*\*[^*]+/ {
    N
    /[^\*]\n[^[:space:]]/s/\n/\n\n/
  }' "$file"
done

#!/bin/bash

DIR="07-cicd-seguro/addon"

echo "🔁 A renomear ficheiros no diretório '$DIR'..."

# Lista de renomeações: "nome_antigo::nome_novo"
RENOMEACOES=$(cat <<EOF
01-catalogo-requisitos.md::01-catalogo-requisitos.md
02-matriz-aplicacao-requisitos.md::02-matriz-aplicacao-requisitos.md
04-politicas-nivel.md::03-politicas-nivel.md
12-controle-ambientes.md::04-controle-ambientes.md
02-runners-execucao.md::05-runners-execucao.md
10-gestao-segredos.md::06-gestao-segredos.md
03-integridade-pipeline.md::07-integridade-pipeline.md
07-validacao-artefactos.md::08-validacao-artefactos.md
08-rastreabilidade-assinaturas.md::09-rastreabilidade-assinaturas.md
06-release-controle.md::10-release-controle.md
05-exemplos-praticos.md::11-exemplos-praticos.md
EOF
)

echo "$RENOMEACOES" | while IFS="::" read OLD NEW; do
  if [ -f "$DIR/$OLD" ]; then
    mv "$DIR/$OLD" "$DIR/$NEW"
    echo "✅ $OLD → $NEW"
  else
    echo "⚠️  Ficheiro não encontrado: $OLD"
  fi
done

echo "✔️ Renumeração concluída."

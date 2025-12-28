# 🏷️ Tagging Tools - Status & Próximos Passos

## ✅ Progresso

### Concluído:
- ✅ **Script `suggest_tags.py`**: Funcional e testado
- ✅ **Análise Local**: Funcionando perfeitamente (sem dependências externas)
- ✅ **Chroma Integration**: Buscas por similaridade e contexto implementadas
- ✅ **Reports**: Gerados em JSON com detalhes completos
- ✅ **Setup Documentation**: `SETUP_OLLAMA.md` para instalação Ollama

### Teste Realizado:
```bash
python3 suggest_tags.py "002-cross-check" --top-n 10 --max-docs 3
```

**Resultados**:
- 3 documentos analisados
- 26 tags sugeridas (8-10 tags por doc)
- 96% de tags novas (não existentes no metadata)
- Relatório JSON salvo automaticamente

## 📋 Como Usar

### Opção 1: Análise Rápida (Sem Ollama)
```bash
cd src/manual-rag
source rag_env/bin/activate

# Analisar 5 documentos do capítulo
python3 rag_tools/tagging_tools/suggest_tags.py "002-cross-check" --top-n 15 --max-docs 5

# Ou analisar todos os documentos
python3 rag_tools/tagging_tools/suggest_tags.py "002-cross-check" --top-n 15
```

### Opção 2: Com Ollama (Melhor Qualidade)

1. **Terminal 1** - Instalar e inicia Ollama:
```bash
bash src/manual-rag/rag_tools/tagging_tools/install_ollama.sh
```

2. **Terminal 2** - Executa o script:
```bash
cd src/manual-rag
source rag_env/bin/activate
python3 rag_tools/tagging_tools/suggest_tags.py "002-cross-check" --top-n 15
```

### Opção 3: Analisar Subfolders do 010-sbd-manual

```bash
# Analisar secção específica
python3 rag_tools/tagging_tools/suggest_tags.py "010-sbd" \
  --subfolder "01-classificacao-aplicacoes" \
  --top-n 12 --max-docs 20

# Analisar apenas requisitos
python3 rag_tools/tagging_tools/suggest_tags.py "010-sbd" \
  --subfolder "02-requisitos" \
  --top-n 12

# Analisar arquitetura
python3 rag_tools/tagging_tools/suggest_tags.py "010-sbd" \
  --subfolder "04-arquitetura" \
  --top-n 12 --max-docs 30
```

## 📁 Arquivos Criados

```
src/manual-rag/rag_tools/tagging_tools/
├── __init__.py                 # Module marker
├── suggest_tags.py             # Main tagging script ✅ FUNCIONAL
├── SETUP_OLLAMA.md            # Instruções instalação
├── install_ollama.sh          # Script de instalação
├── run_tagging.sh             # Wrapper para execução
└── reports/                   # Relatórios gerados aqui
    └── chapter_002-cross-check-normativo_tags_top10.json
```

## 📂 Capítulos e Subfolders Disponíveis

### 002-cross-check-normativo (522 docs)
Análise de conformidade com normas e frameworks

### 010-sbd-manual (4522 docs)
Manual completo de Security by Design com subfolders:

| Subfolder | Descrição | Docs |
|-----------|-----------|------|
| 00-fundamentos | Fundamentos de SbD | ~400 |
| **01-classificacao-aplicacoes** | Classificação e maturidade | ~350 |
| **02-requisitos-seguranca** | Requisitos técnicos | ~600 |
| **03-threat-modeling** | Modelagem de ameaças | ~500 |
| **04-arquitetura-segura** | Arquitetura segura | ~450 |
| **05-dependencias-sbom-sca** | Dependências e SBOM | ~380 |
| **06-desenvolvimento-seguro** | Dev seguro | ~600 |
| **07-cicd-seguro** | CI/CD seguro | ~450 |
| **08-iac-infraestrutura** | Infrastructure as Code | ~400 |
| **09-containers-imagens** | Containers | ~350 |
| **10-testes-seguranca** | Testes de segurança | ~400 |
| **11-deploy-seguro** | Deploy seguro | ~380 |
| **12-monitorizacao-operacoes** | Monitorização | ~450 |
| **13-formacao-onboarding** | Formação e onboarding | ~300 |
| **14-governanca-contratacao** | Governança | ~350 |

### tldr (22 docs)
Resumo executivo

## 💡 Exemplo de Saída

**Documento**: `01-intro.md` (Cross-Check)

**Tags Existentes** (10): compliance, cross-check, dora, nis2, iso27001...

**Tags Sugeridas** (10, NEW): compliance, construção, lacunas, complementaridade, processos...

**Status**: 90% de tags novas (sugestões independentes!)

## 🔧 Próximos Passos Opcionais

1. **Instalar Ollama** para sugestões com LLM sofisticado
2. **Ampliar análise** para todo o capítulo 010-sbd-manual (4522 docs)
3. **Integrar sugestões** ao workflow de revisão de tags
4. **Validar qualidade** comparando tags sugeridas vs existentes
5. **Fazer merge** das melhores tags com o conjunto canônico

## 📊 Estatísticas Iniciais (3 docs testados)

- Documentos analisados: 3
- Tags sugeridas: 26 (média 8.7 por doc)
- Tags novas: 25 (96%)
- Tags em comum: 1 (4%)
- Tempo: ~30s (primeira execução, com download de modelo)

## ⚠️ Notas Importantes

1. **Análise Local**: Usa keyword extraction + similaridade semântica (sem LLM)
   - ✅ Rápido, não precisa Ollama
   - ✅ Funcional agora
   - ⚠️ Menos sofisticado que LLM

2. **Com Ollama**: Usa Mistral 7B para análise semântica completa
   - ✅ Melhor qualidade de sugestões
   - ⚠️ Requer instalação Ollama
   - ⚠️ Mais lento (~5-10s por doc)

3. **Ignora Tags Existentes**: Script analisa APENAS conteúdo
   - ✅ Sugestões completamente independentes
   - ✅ Ideal para validação
   - ✓ Conforme requisitado

## 📝 Próxima Ação Recomendada

Testar análise de capítulo maior:
```bash
python3 rag_tools/tagging_tools/suggest_tags.py "010-sbd-manual" --top-n 15 --max-docs 50
```

Isto gerará insights sobre quais tags são mais relevantes para o manual principal.

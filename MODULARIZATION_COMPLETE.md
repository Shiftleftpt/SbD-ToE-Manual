# 📦 Manual RAG - Modularização Completa

## ✅ Estrutura Modular Implementada

```
manual-rag/
│
├── 📁 rag_core/              ← RAG INFRASTRUCTURE (Construção do índice)
│   ├── indexing/             
│   │   └── ManualIndexer     (Constrói índice com chunks + metadata)
│   ├── query/                
│   │   └── SemanticSearch    (Query com reranking por chapter)
│   └── local_llm/            
│       └── OllamaClient       (Interface com Ollama LLM)
│
├── 📁 rag_tools/             ← RAG TOOLS (Operações baseadas em RAG)
│   │
│   ├── 📁 tagging/           (Tag Management - Sugestões + Normalização)
│   │   ├── _tags.py          ← CanonicalTags (carrega tags.yml, normaliza)
│   │   ├── _auto_tagger.py   ← AutoTagger (RAG + patterns), TagSuggestion
│   │   ├── _file_updater.py  ← FileTagUpdater (lê/escreve frontmatter)
│   │   └── __init__.py       (Exports públicos)
│   │
│   ├── 📁 workflows/         (High-level CLIs)
│   │   ├── build_chunked_index.py     (Constrói índice)
│   │   ├── generate_review_report.py  (Analisa ficheiros, gera CSV)
│   │   ├── apply_review_decisions.py  (Aplica tags aprovadas)
│   │   └── __init__.py
│   │
│   ├── 📁 utils/             (Utilidades)
│   │   ├── batch.py          (Batch processing)
│   │   ├── smart_tag_selection.py (Selecciona top N tags)
│   │   └── __init__.py
│   │
│   └── __init__.py           (Package root)
│
├── 📁 tests/                 ← TESTES
│   ├── rag/                  (Testes para RAG core)
│   │   ├── test_chapter_aware.py
│   │   ├── test_improved_search.py
│   │   ├── test_strategies.py
│   │   └── audit_tags_comprehensive.py
│   ├── tagging/              (Testes para tagging)
│   │   └── __init__.py
│   └── __init__.py
│
├── 📁 results/               ← OUTPUTS (git-ignored)
│   ├── .gitignore            (Exclui *.csv, *.json, *.db, chroma/)
│   └── *.csv, *.json         (Relatórios temporários)
│
├── 📁 manual_rag/            ← CONFIGURAÇÃO
│   ├── config.py             (Paths centralizados)
│   └── __init__.py
│
├── 📁 .archive/              ← LEGACY (histórico)
│   └── legacy_scripts/       (Scripts antigos, não usados)
│
├── canonical-tags.yml        ← TAG VOCABULARY (ESSENCIAL)
├── requirements.txt
├── README.md
└── MODULAR_STRUCTURE.md      ← Documentação completa
```

---

## 🎯 Separação de Responsabilidades

### **Camada 1: RAG CORE** (Construção)
```python
from rag_core import ManualIndexer, SemanticSearch, OllamaClient

# Constrói o índice (one-time)
indexer = ManualIndexer()
indexer.index_all(force_rebuild=True)
# Output: index/chroma/ com 5000+ chunks
```

**Responsabilidade**: Criar e manter índice vectorial

---

### **Camada 2-4: RAG TOOLS** (Operações)

#### **Camada 2: Tag Management** (`rag_tools/tagging/`)

```python
from rag_tools.tagging import CanonicalTags, AutoTagger, FileTagUpdater

# 1. Normalização (CanonicalTags)
canonical = CanonicalTags()
normalized = canonical.normalize("auth")  # → "autenticacao"
is_valid = canonical.is_valid("autenticacao")  # → True

# 2. Sugestões (AutoTagger - usa RAG + Patterns)
tagger = AutoTagger()  # Cria SemanticSearch internamente
suggestions = tagger.suggest_tags(
    file_path="010-sbd-manual/02-requisitos-seguranca/file.md",
    content="...",
    title="Authentication",
    existing_tags=["seguranca"]
)
# Output: List[TagSuggestion] com confidence + reasoning

# 3. Merge com threshold
final_tags, new_tags = tagger.merge_tags(
    existing_tags, 
    suggestions, 
    strategy='balanced'  # 0.6 threshold
)

# 4. Escrita (FileTagUpdater)
FileTagUpdater.update_tags(Path("docs/file.md"), final_tags)
```

**Separação de responsabilidades**:
- `_tags.py`: Dados (loading, validation)
- `_auto_tagger.py`: Lógica (sugestões com RAG + patterns)
- `_file_updater.py`: I/O (lê/escreve YAML)

---

#### **Camada 3: Workflows** (`rag_tools/workflows/`)

```bash
# Fase 1: Build index
python rag_tools/workflows/build_chunked_index.py

# Fase 2: Generate review report
python rag_tools/workflows/generate_review_report.py > results/review_report.csv

# Fase 3: Apply approved tags
python rag_tools/workflows/apply_review_decisions.py results/review_report.csv
```

**Scripts de produção** - CLI entry points

---

#### **Camada 4: Utilities** (`rag_tools/utils/`)

```python
from rag_tools.utils.smart_tag_selection import select_tags_for_display

# Selecciona top 7 tags para legibilidade
readable_tags = select_tags_for_display(all_tags, max_count=7)
```

**Funções auxiliares** - Reutilizáveis

---

## 📊 Fluxo de Dados

```
┌──────────────────────────────────────────────────────┐
│ FASE 1: BUILD INDEX (one-time)                       │
├──────────────────────────────────────────────────────┤
│ build_chunked_index.py                               │
│   └─ ManualIndexer                                   │
│       ├─ read docs/                                  │
│       ├─ extract metadata (chapter, domain)          │
│       ├─ generate embeddings                         │
│       └─ store in Chroma                             │
│                                                      │
│ Output: index/chroma/ (5000+ chunks)                │
└──────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────┐
│ FASE 2: GENERATE REVIEW (per-file)                  │
├──────────────────────────────────────────────────────┤
│ generate_review_report.py                            │
│   └─ for each file:                                  │
│       ├─ FileTagUpdater.read_frontmatter()          │
│       ├─ AutoTagger.suggest_tags()                  │
│       │   ├─ SemanticSearch.search() [RAG]         │
│       │   ├─ extract_patterns() [Regex]            │
│       │   └─ CanonicalTags.normalize()             │
│       └─ Merge with strategy='balanced'             │
│                                                      │
│ Output: results/review_report.csv                   │
└──────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────┐
│ FASE 3: APPLY DECISIONS (batch)                     │
├──────────────────────────────────────────────────────┤
│ apply_review_decisions.py < review_report.csv       │
│   └─ for each OK row:                                │
│       └─ FileTagUpdater.update_tags()               │
│           └─ write YAML frontmatter                  │
│                                                      │
│ Output: 250+ files attualizados                     │
└──────────────────────────────────────────────────────┘
```

---

## 🔄 Imports Após Modularização

### Antes (monolítico)
```python
from manual_rag.tagging import AutoTagger, CanonicalTags, FileTagUpdater
from manual_rag.query import SemanticSearch
from manual_rag.indexing import ManualIndexer
```

### Depois (modular) ✅
```python
# RAG infrastructure (Layer 1)
from rag_core import ManualIndexer, SemanticSearch, OllamaClient

# RAG tools (Layers 2-4)
from rag_tools.tagging import AutoTagger, CanonicalTags, FileTagUpdater, TagSuggestion
from rag_tools.utils.smart_tag_selection import select_tags_for_display

# Configuration
from manual_rag.config import MANUAL_ROOT, TAGS_FILE
```

---

## 🧪 Testes

```
tests/
├── rag/                    ← Testes para RAG core
│   ├── test_chapter_aware.py
│   ├── test_improved_search.py
│   └── test_strategies.py
└── tagging/                ← Testes para tagging (a adicionar)
```

**Run**:
```bash
pytest tests/                # Todos
pytest tests/rag/            # Apenas RAG
pytest tests/tagging/        # Apenas tagging
```

---

## 📋 Results (Git-Ignored)

```
results/
├── .gitignore              ← Exclui saídas temporárias
├── review_report.csv       ← Generated by workflow
├── comparison_*.json       ← Generated by tests
└── chroma/                 ← (se movido aqui)
```

**Por quê git-ignore?**
- Outputs gerados (não são fonte)
- Grandes ficheiros binários
- Mudam frequentemente
- Não são reutilizáveis

---

## 🎁 Benefícios da Modularização

✅ **Single Responsibility**: Cada módulo tem um propósito claro  
✅ **Testability**: Testar cada camada independentemente  
✅ **Reusability**: Importar tagging logic em outros projectos  
✅ **Extensibility**: Adicionar novos workflows sem mexer em core  
✅ **Maintainability**: Ficheiros pequenos e focados  
✅ **Documentation**: Cada módulo autodocumentado com docstrings  

---

## 🚀 Exemplos de Uso

### Usar RAG Core sozinho
```python
from rag_core import ManualIndexer, SemanticSearch

# Build index
indexer = ManualIndexer()
indexer.index_all()

# Query
searcher = SemanticSearch()
results = searcher.search("authentication", top_k=5)
```

### Usar Tagging sozinho
```python
from rag_tools.tagging import CanonicalTags, FileTagUpdater

# Validate tags
canonical = CanonicalTags()
for tag in old_tags:
    normalized = canonical.normalize(tag)

# Update file
FileTagUpdater.update_tags(Path("file.md"), new_tags)
```

### Usar Workflows completos
```bash
# Análise completa
python rag_tools/workflows/build_chunked_index.py
python rag_tools/workflows/generate_review_report.py
# ... review results/review_report.csv ...
python rag_tools/workflows/apply_review_decisions.py results/review_report.csv
```

---

## 📈 Pronto para Crescimento

Estrutura preparada para:

1. **Novos workflows**:
   - `batch_auto_tagger.py` - Processar muitos ficheiros
   - `tag_validator.py` - Validar tags
   - `gap_analysis.py` - Encontrar lacunas

2. **Novas ferramentas RAG**:
   - `semantic_search/` - UI de pesquisa
   - `duplicate_detection/` - Encontrar duplicados
   - `cross_reference/` - Referências cruzadas

3. **Mais testes**:
   - Unit tests para cada classe
   - Integration tests para workflows
   - Performance tests

---

## ✨ Resumo

| Aspecto | Antes | Depois |
|--------|-------|--------|
| Ficheiros | 1 monolítico | 4 camadas bem separadas |
| Imports | Complicados | Claros e organizados |
| Testability | Difícil | Fácil (cada módulo) |
| Extensibility | Acoplado | Desacoplado |
| Documentação | Genérica | Específica por módulo |
| Reutilização | Difícil | Fácil |

**Status**: ✅ **PRODUCTION READY**

Estrutura modular implementada, documentada e commitada!

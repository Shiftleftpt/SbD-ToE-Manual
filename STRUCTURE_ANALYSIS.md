# Manual RAG - Estrutura e Separação de Concerns

## 1. ESTADO ATUAL

```
manual-rag/
├── manual_rag/              # CORE LIBRARY
│   ├── __init__.py          # Exports: SemanticSearch, OllamaClient
│   ├── config.py            # Configuração centralizada
│   ├── indexing/
│   │   └── __init__.py      # ManualIndexer (constrói índice)
│   ├── query/
│   │   └── __init__.py      # SemanticSearch (query/search no índice)
│   ├── tagging/
│   │   └── __init__.py      # AutoTagger (sugestões de tags com RAG)
│   └── local_llm/
│       └── __init__.py      # OllamaClient (chamadas LLM)
│
├── tools/                    # PRODUCTION WORKFLOWS
│   ├── build_chunked_index.py   # CLI: Constrói índice com chunks
│   ├── generate_review_report.py # CLI: Gera relatório de review
│   └── apply_review_decisions.py # CLI: Aplica decisões aprovadas
│
├── scripts/
│   ├── legacy/              # CÓDIGO LEGADO (descontinuado)
│   │   └── *.py            # Scripts antigos que usavam tag_system/
│   └── testing/             # SCRIPTS DE TESTE
│       └── *.py            # Testes e validações
│
├── canonical-tags.yml       # DATA: Tags canónicas (ESSENCIAL)
├── config.py               # CONFIGURAÇÃO
└── __main__.py             # ENTRY POINT
```

---

## 2. ANÁLISE DE RESPONSABILIDADES

### **LAYER 1: RAG INFRASTRUCTURE (Construção)**
**Responsável por: Criar e manter o índice**

```
manual_rag/indexing/ManualIndexer
    ↓
    └─→ Carrega documentos MD
        └─→ Lê frontmatter (YAML)
        └─→ Extrai metadata (chapter, tags, title)
        └─→ Gera embeddings (SentenceTransformer)
        └─→ Armazena em Chroma (persistent index)

Saída: INDEX_DIR/chroma/ (base de dados vetorial)
```

**Usadores:**
- `tools/build_chunked_index.py` → Builds the chunked JSONL index
- `tools/build_chunked_index.py` → Builds the Chroma persistent DB

---

### **LAYER 2: RAG QUERY (Utilização)**
**Responsável por: Consultar o índice para encontrar documentos similares**

```
manual_rag/query/SemanticSearch
    ↓
    ├─→ search()            # Query semântica com reranking por capítulo
    ├─→ suggest_tags()      # Sugere tags baseado em docs similares
    ├─→ cross_reference()   # Encontra referências cruzadas
    ├─→ analyze_gaps()      # Análise de conteúdo em falta (com LLM)
    └─→ _extract_chapter()  # Helper: extrai capítulo de caminho

Entrada: Query string
Saída: Lista de documentos similares com scores
```

**Usadores:**
- `manual_rag/tagging/AutoTagger.suggest_from_rag()` → Gets tags from similar docs
- `tools/generate_review_report.py` → Para análise de ficheiros
- Scripts de teste

---

### **LAYER 3: TAG MANAGEMENT (Normalização)**
**Responsável por: Gerir tags canónicas, validação, normalização**

```
manual_rag/tagging/CanonicalTags
    ↓
    ├─→ Load tags from YAML (canonical-tags.yml)
    ├─→ is_valid()          # Valida se tag é canónica ou alias
    ├─→ normalize()         # Converte alias → tag canónica
    └─→ get_description()   # Devolve descrição

Entrada: canonical-tags.yml
Saída: Tag mappings (name → canonical_name)
```

**Usadores:**
- `manual_rag/tagging/AutoTagger` → Para validar e normalizar tags sugeridas
- `manual_rag/tagging/FileTagUpdater` → Para escrever tags validadas

---

### **LAYER 4: AUTO-TAGGING (Sugestões)** 
**Responsável por: Combinar RAG + Padrões + Tags Existentes**

```
manual_rag/tagging/AutoTagger
    ↓
    ├─→ extract_patterns()        # Regex patterns (cicd, auth, etc)
    ├─→ suggest_from_rag()        # RAG: similar docs (usa SemanticSearch)
    ├─→ suggest_tags()            # COMBINA: RAG + Patterns + Existing
    │   └─→ Confidence scoring
    └─→ merge_tags()              # Aplica threshold (conservative/balanced/aggressive)

Entrada: File content, path, existing tags
Saída: TagSuggestion[] com confidence + reasoning
```

**Usadores:**
- `tools/generate_review_report.py` → Para gerar relatório
- `tools/apply_review_decisions.py` → Para aplicar decisões

---

### **LAYER 5: FILE OPERATIONS (Escrita)**
**Responsável por: Ler/escrever frontmatter YAML de ficheiros**

```
manual_rag/tagging/FileTagUpdater
    ↓
    ├─→ read_frontmatter()   # Extrai YAML frontmatter
    ├─→ write_frontmatter()  # Escreve YAML frontmatter
    └─→ update_tags()        # Aplica novas tags ao ficheiro

Entrada: Caminho ficheiro + novas tags
Saída: Ficheiro actualizado
```

**Usadores:**
- `tools/apply_review_decisions.py` → Escreve tags nos ficheiros

---

## 3. FLUXO DE DADOS

```
┌─────────────────────────────────────────────────────────────┐
│  FASE 1: CONSTRUÇÃO (One-time)                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  tools/build_chunked_index.py                               │
│    ↓                                                         │
│    └─→ ManualIndexer.index_all()                           │
│        ├─→ Lê docs/*.md                                     │
│        ├─→ Extrai metadata (path → chapter/domain/tags)    │
│        ├─→ Gera embeddings                                  │
│        └─→ Chroma.add() → INDEX_DIR/chroma/                │
│                                                              │
│    Saída: 5066 chunks em Chroma com metadata               │
│                                                              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  FASE 2: AUTO-TAGGING (Per-file analysis)                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  tools/generate_review_report.py                            │
│    ↓                                                         │
│    for cada ficheiro:                                       │
│        ├─→ FileTagUpdater.read_frontmatter()              │
│        ├─→ AutoTagger.suggest_tags():                      │
│        │   ├─→ SemanticSearch.search() [RAG]              │
│        │   ├─→ AutoTagger.extract_patterns() [Regex]      │
│        │   ├─→ CanonicalTags.normalize() [Validation]     │
│        │   └─→ Merge com estratégia (balanced = 0.6)      │
│        └─→ CSV Report (file | old_tags | new_tags | OK?) │
│                                                              │
│    Saída: review_report.csv                                │
│                                                              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  FASE 3: APLICAÇÃO (Batch update)                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  tools/apply_review_decisions.py < review_report.csv       │
│    ↓                                                         │
│    for cada row com APPROVAL_STATUS = OK:                  │
│        ├─→ FileTagUpdater.update_tags()                    │
│        │   ├─→ read_frontmatter()                          │
│        │   ├─→ update tags field                           │
│        │   └─→ write_frontmatter()                         │
│        └─→ docs/*/file.md [ACTUALIZADO]                    │
│                                                              │
│    Saída: 251 ficheiros com tags actualizadas              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 4. PROPOSTAS DE SEPARAÇÃO

### **Opção A: Manter Estrutura (RECOMENDADO)**
✅ Já bem separado. Apenas reorganizar:

```
manual-rag/
├── manual_rag/              
│   ├── core/               # NEW: RAG infrastructure (build)
│   │   ├── indexing/       # Moved from indexing/
│   │   └── query/          # Moved from query/
│   ├── tagging/            # KEEP: Tag management + auto-tagging
│   └── config.py           # Shared config
├── tools/                   # KEEP: Production workflows
└── scripts/
    ├── legacy/             # KEEP: Legacy (pode remover depois)
    └── testing/            # KEEP: Tests
```

**Vantagem:** Deixa claro: `core/` = RAG construction, `tagging/` = tag workflows

---

### **Opção B: Separação Mais Radical**
Esta seria a estrutura mais "enterprise":

```
manual-rag/
├── core/                    # RAG infrastructure
│   ├── indexing/           # Index building only
│   ├── query/              # Query interface only
│   └── embeddings/         # Model management
├── tagging/                 # Tag management workflows
│   ├── management/         # CanonicalTags, validation
│   ├── auto_tagger/        # AutoTagger logic
│   └── file_ops/           # FileTagUpdater
├── tools/                   # CLI entry points (não contêm lógica)
└── scripts/
```

**Vantagem:** Total separação entre "construir RAG" e "usar RAG para tags"
**Desvantagem:** Muitos imports circulares, mais verboso

---

## 5. RECOMENDAÇÃO FINAL

### **Manter Option A (Simple + Clean)**

A estrutura actual é boa porque:

1. **`manual_rag/indexing`** = "Como construir o índice"
2. **`manual_rag/query`** = "Como consultar o índice"  
3. **`manual_rag/tagging`** = "Como usar o índice para sugerir tags"
4. **`manual_rag/local_llm`** = "Interface com LLM"

O ponto de separação natural é:
- **RAG Construction**: `build_chunked_index.py` → `ManualIndexer`
- **RAG Query**: `generate_review_report.py` → `SemanticSearch` → `AutoTagger`
- **File Updates**: `apply_review_decisions.py` → `FileTagUpdater`

**Não precisa alterar código**, apenas **documentar a responsabilidade de cada módulo**.

### **O que PODIA melhorar:**

1. **`manual_rag/tagging/`** tem 3 classes bem distintas:
   - `CanonicalTags` = Data management (canonização)
   - `AutoTagger` = Business logic (sugestões)
   - `FileTagUpdater` = I/O (escrita em disco)
   
   Podiam ir para sub-módulos, mas é overengineering nesta escala.

2. **Documentação**: Cada classe deveria ter docstring explicando:
   - O quê faz
   - Quem a usa
   - Que dados entra/sai

3. **`scripts/legacy/`**: Pode ficar ou remover - não afecta a arquitectura

---

## 6. EXEMPLO DE COMO CADA CAMADA É USADA

```python
# ===== LAYER 1: Build Index (one-time) =====
from manual_rag.indexing import ManualIndexer

indexer = ManualIndexer()
indexer.index_all(force_rebuild=True)
# Resultado: INDEX_DIR/chroma/ com 5066 chunks

# ===== LAYER 2: Query Index =====
from manual_rag.query import SemanticSearch

searcher = SemanticSearch()
results = searcher.search("authentication", context_file="010-sbd-manual/file.md")
# Resultado: List[Dict] com docs similares do mesmo chapter

# ===== LAYER 3+4: Auto-tag com RAG =====
from manual_rag.tagging import AutoTagger, CanonicalTags

tagger = AutoTagger()  # Internamente cria SemanticSearch()
suggestions = tagger.suggest_tags("docs/file.md", content, title, existing_tags)
# Resultado: List[TagSuggestion] com confidence + reasoning

final_tags, new_tags = tagger.merge_tags(existing, suggestions, strategy='balanced')
# Resultado: tags filtradas por threshold (0.6 para balanced)

# ===== LAYER 5: Write tags back =====
from manual_rag.tagging import FileTagUpdater

FileTagUpdater.update_tags(Path("docs/file.md"), final_tags, dry_run=False)
# Resultado: ficheiro actualizado com novo frontmatter
```

---

## 7. CONCLUSÃO

A estrutura já está **bem separada por responsabilidades**:
- ✅ Indexing (build)
- ✅ Query (search)
- ✅ Tagging (suggestions)
- ✅ File I/O (write)

**Próximos passos para melhorar:**
1. Adicionar docstrings em cada classe explicando responsabilidade
2. Adicionar type hints completos
3. Considerar mover `scripts/legacy/` para pasta `.archive/`
4. Considerar `scripts/testing/` → `tests/` (pytest structure)

Quer que eu faça alguma destas melhorias? 🚀

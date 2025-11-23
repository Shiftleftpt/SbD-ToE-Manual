# Auto-Tagging System

Intelligent tag suggestion system combining semantic search, pattern matching, and LLM analysis.

## 🎯 How It Works

### Three-Stage Pipeline

1. **Semantic Search** (100% precision)
   - Find similar content using vector embeddings
   - Chapter-aware prioritization
   - Returns relevant documents

2. **Pattern Matching**
   - Analyze content for keywords
   - Extract domain indicators
   - Combine with existing tags

3. **LLM Suggestion** (Optional)
   - Use Ollama for context-aware suggestions
   - Fallback to pattern matching if LLM unavailable
   - Confidence scoring

### Components

#### `_tags.py` - Tag Management
```python
from rag_tools.tagging import CanonicalTags

# Load tags from data/canonical-tags.yml
tags = CanonicalTags.from_file("rag_tools/tagging/data/canonical-tags.yml")

# Access tag hierarchies
print(tags.domains)      # List of domains
print(tags.frameworks)   # List of frameworks
print(tags.patterns)     # Regex patterns for tag detection
```

#### `_auto_tagger.py` - Tag Suggestion
```python
from rag_tools.tagging import AutoTagger, CanonicalTags

tags = CanonicalTags.from_file("rag_tools/tagging/data/canonical-tags.yml")
tagger = AutoTagger(tags=tags)

# Get suggestions for a file
suggestions = tagger.suggest_tags(
    file_path="docs/chapter/file.md",
    max_tags=7
)

# Returns: {
#   "current_tags": ["existing", "tags"],
#   "suggested_tags": ["new", "tags"],
#   "confidence": 0.85,
#   "source": "semantic_search"
# }
```

#### `_file_updater.py` - Apply Changes
```python
from rag_tools.tagging import FileTagUpdater

updater = FileTagUpdater()

# Update a file's frontmatter tags
updater.update_file_tags(
    file_path="docs/chapter/file.md",
    new_tags=["tag1", "tag2", "tag3"]
)

# Creates backup and updates frontmatter
```

## 📁 Data

### canonical-tags.yml
Master reference for all valid tags:

```yaml
domains:
  - Security
  - DevOps
  - Architecture

frameworks:
  - Spring Boot
  - Kubernetes
  - Docker

patterns:
  security: ['encryption', 'certificate', 'TLS']
  devops: ['CI/CD', 'pipeline', 'deployment']
```

**Location:** `rag_tools/tagging/data/canonical-tags.yml`

## 🚀 Usage

### From Workflow
```bash
# Generate review report with suggestions
python3 -m rag_tools.workflows.generate_review_report --max-tags 7

# Apply approved changes
python3 -m rag_tools.workflows.apply_review_decisions review_report.csv
```

### From Code
```python
from rag_tools.tagging import AutoTagger, CanonicalTags, FileTagUpdater

# 1. Load tags
tags = CanonicalTags.from_file("rag_tools/tagging/data/canonical-tags.yml")

# 2. Create tagger
tagger = AutoTagger(tags=tags)

# 3. Get suggestions
for file in markdown_files:
    suggestions = tagger.suggest_tags(file, max_tags=7)
    print(f"{file}: {suggestions['suggested_tags']}")

# 4. Update files
updater = FileTagUpdater()
updater.update_file_tags(file, suggestions['suggested_tags'])
```

## 🧪 Testing

```bash
# Run tagging tests
python3 -m pytest rag_tools/tagging/tests/ -v

# Specific test
python3 -m pytest rag_tools/tagging/tests/test_auto_tagger.py -v

# With coverage
python3 -m pytest rag_tools/tagging/tests/ --cov=rag_tools.tagging
```

### Test Structure
```
tagging/tests/
├── conftest.py
├── test_tags.py         # CanonicalTags tests
├── test_auto_tagger.py  # AutoTagger tests
└── test_file_updater.py # FileTagUpdater tests
```

## ⚙️ Configuration

Edit suggestions behavior in code:

```python
# Confidence threshold
MIN_CONFIDENCE = 0.7

# Max tags per file
MAX_TAGS = 7

# Semantic search parameters
SEARCH_RESULTS = 5      # Similar documents to analyze
RELEVANCE_THRESHOLD = 0.6
```

## 📊 Typical Results

From analyzing 276 files:
- **252 files** with suggestions (91.3%)
- **~7 tags per file** on average
- **100%** chapter accuracy
- **0.75** average confidence score

## 🔗 Dependencies

- `rag_core` - Semantic search
- `sentence-transformers` - Embeddings
- `pyyaml` - YAML parsing
- `ollama` - Optional LLM (client only)
- `pytest` - Testing

## 🔗 See Also

- [rag_tools README](../README.md) - Tools overview
- [rag_core README](../rag_core/README.md) - Search infrastructure
- [data/canonical-tags.yml](data/canonical-tags.yml) - Tag reference

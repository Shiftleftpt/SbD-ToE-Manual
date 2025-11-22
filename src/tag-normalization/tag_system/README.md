# 📋 Tag System - Architecture & Organization

## Project Structure

```
tag_system/
├── core/                     # Core components
│   ├── __init__.py
│   └── canonical_tags.py    # CanonicalTagsManager - single source of truth
│
├── validators/              # Tag validation
│   ├── __init__.py
│   └── validation_engine.py # ValidationEngine - analyzes existing tags
│
├── recommenders/            # Tag recommendations
│   ├── __init__.py
│   └── recommendation_engine.py # RecommendationEngine - suggests tags
│
├── services/                # Utility services (TBD)
│   └── __init__.py
│
├── cli/                     # Command-line interface
│   ├── __init__.py
│   └── main_cli.py         # Unified CLI
│
├── reports/                 # Report generation (TBD)
│   └── __init__.py
│
├── tests/                   # Unit tests
│   └── __init__.py
│
├── Makefile                 # Build automation
├── README.md               # This file
└── __init__.py             # Package root
```

## Components

### 1. Core - CanonicalTagsManager

**Purpose**: Single source of truth for all tags.

**Key methods:**
- `load()` - Load from YAML
- `get_tag(name)` - Get tag info
- `find_by_alias(alias)` - Find canonical tag by alias
- `get_related_tags(tag)` - Get semantically related tags

### 2. Validators - ValidationEngine

**Purpose**: Analyze existing tags and identify issues.

**Detects:**
- ✓ Unknown tags (not in canonical)
- ✓ Aliases (should be normalized)
- ✓ Case mismatches
- ✓ Duplicate tags
- ✓ Formatting errors

**Output**: List of `ValidationIssue` with severity (ERROR/WARNING/INFO)

### 3. Recommenders - RecommendationEngine

**Purpose**: Suggest tags based on content and context.

**Factors:**
1. **Keyword match** - Keywords in title/description/content
2. **Semantic relations** - Tags related to existing tags
3. **Context boost** - Tags from parent chapter
4. **Related tags** - Tags marked as related in canonical

**Output**: List of `Recommendation` with confidence scores

### 4. CLI - Unified Interface

**Commands:**
- `validate` - Validate all tags
- `recommend` - Recommend missing tags
- `audit` - Full validation + recommendations

## Usage

### Via Makefile

```bash
cd tag_system

# Validate
make validate BASE_PATH=../../../manuals_src/docs/sbd-toe

# Recommend (with limit)
make recommend BASE_PATH=../../../manuals_src/docs/sbd-toe LIMIT=10

# Full audit
make audit BASE_PATH=../../../manuals_src/docs/sbd-toe
```

### Programmatic

```python
from tag_system.core import CanonicalTagsManager
from tag_system.validators import ValidationEngine
from tag_system.recommenders import RecommendationEngine

# Initialize
canonical = CanonicalTagsManager("canonical-tags.yml")
validator = ValidationEngine(canonical)
recommender = RecommendationEngine(canonical)

# Validate file
result = validator.validate_file("docs/chapter/file.md")
print(f"Errors: {result.error_count}")
for issue in result.issues:
    print(f"  - {issue.message}")

# Get recommendations
recommendations = recommender.recommend_tags("docs/chapter/file.md")
for rec in recommendations:
    print(f"  - {rec.tag} ({rec.confidence:.0%}): {rec.reason}")
```

## Design Principles

1. **Modular**: Each component has a single responsibility
2. **Extensible**: Easy to add new validators/recommenders
3. **Type-safe**: Uses dataclasses and type hints
4. **Well-documented**: Clear docstrings and examples
5. **Testable**: Components can be tested independently

## Next Steps

- [ ] Implement report generation (JSON, HTML)
- [ ] Add tag unification service (normalize aliases)
- [ ] Add tests for each component
- [ ] Add configuration system
- [ ] Add batch recommendation with approval workflow

# 📋 Tag System - Validation & Recommendation Engine

Professional-grade system for validating, auditing, and recommending tags in markdown documentation.

## 🚀 Quick Start

### 1. Setup (First Time Only)

```bash
cd src/tag-normalization
./setup-env.sh
```

### 2. Validate Tags

```bash
cd tag_system
make validate BASE_PATH=../../../manuals_src/docs/sbd-toe
```

Shows all tag issues: unknown tags, aliases, case mismatches, duplicates.

### 3. Get Recommendations

```bash
make recommend BASE_PATH=../../../manuals_src/docs/sbd-toe
```

Suggests missing tags based on content, context, and semantic relations.

### 4. Full Audit

```bash
make audit BASE_PATH=../../../manuals_src/docs/sbd-toe
```

Runs both validation and recommendations in one go.

## 📁 Structure

```
tag_system/
├── core/              # Canonical tags manager
├── validators/        # Tag validation engine
├── recommenders/      # Tag recommendation engine
├── cli/              # Command-line interface
├── services/         # Utility services (TBD)
├── reports/          # Report generation (TBD)
├── tests/            # Unit tests (TBD)
├── Makefile          # Build automation
└── README.md         # Architecture docs
```

## ✨ Features

✓ **Validation**: Detect unknown tags, aliases, case mismatches, duplicates  
✓ **Recommendations**: Suggest tags based on:
  - Content keywords
  - Semantic relations (e.g., sbom ↔ sca ↔ supply-chain)
  - Parent chapter context
  - Related tags already present  
✓ **Modular Design**: Easy to extend with new validators/recommenders  
✓ **Type-Safe**: Full type hints and dataclasses  
✓ **Well-Documented**: Clear docstrings and inline docs

## 🧠 How It Works

### Validation Engine

Analyzes existing tags in files and identifies issues:

```
File: docs/chapter/file.md
  ❌ Unknown tag: 'foo' → Add to canonical or use alias
  ⚠️  Case mismatch: 'Testing' → Use 'testing'
  ⚠️  Alias found: 'SBOM' → Use canonical 'sbom'
```

### Recommendation Engine

Suggests missing tags based on smart analysis:

```
File: docs/05-sbom/addon/inventory.md
  💡 sbom (0.95) - keyword match
  💡 sca (0.80) - semantic: related to sbom
  💡 supply-chain (0.75) - context: parent chapter
```

## 📖 Documentation

- **Architecture**: `tag_system/README.md`
- **Legacy Code**: `legacy/` (old normalization scripts)

## 🔧 Programmatic Usage

```python
from tag_system.core import CanonicalTagsManager
from tag_system.validators import ValidationEngine
from tag_system.recommenders import RecommendationEngine

# Initialize
canonical = CanonicalTagsManager("canonical-tags.yml")
validator = ValidationEngine(canonical)
recommender = RecommendationEngine(canonical)

# Validate
result = validator.validate_file("docs/file.md")
for issue in result.issues:
    print(f"- {issue.message}")

# Recommend
recommendations = recommender.recommend_tags("docs/file.md")
for rec in recommendations:
    print(f"- {rec.tag}: {rec.reason}")
```

## 📊 Canonical Tags

All available tags are defined in `canonical-tags.yml` (489 tags across multiple categories).

Each tag includes:
- **Category**: Classification (security, testing, governance, etc.)
- **Description**: Clear definition
- **Aliases**: Alternative names
- **Related**: Semantically related tags

## 🎯 Next Steps

- [ ] Report generation (JSON, HTML)
- [ ] Tag unification service
- [ ] Unit tests
- [ ] Configuration system
- [ ] Web dashboard

---

**Status**: Production Ready ✓


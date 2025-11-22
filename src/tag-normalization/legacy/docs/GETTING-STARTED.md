# 🚀 Getting Started - Tag System

## One-Time Setup

### Step 1: Create Virtual Environment

```bash
cd src/tag-normalization
./setup-env.sh
```

This creates `.venv/` and installs dependencies (scikit-learn, numpy, pytest, pyyaml).

### Step 2: Verify Setup

```bash
source .venv/bin/activate
python3 -c "from tag_system.core import CanonicalTagsManager; print('✓ Ready!')"
```

## Daily Usage

### Check Existing Tags for Issues

```bash
cd src/tag-normalization/tag_system
make validate BASE_PATH=../../../manuals_src/docs/sbd-toe
```

Output shows:
- ❌ Unknown tags (not in canonical)
- ⚠️  Aliases (should be normalized)
- ⚠️  Case mismatches
- ⚠️  Duplicates

### Get Tag Recommendations

```bash
make recommend BASE_PATH=../../../manuals_src/docs/sbd-toe
```

Output shows:
- 💡 Suggested tags with confidence scores
- 🔍 Why each tag is recommended (keyword, semantic, context)
- 📊 Recommendation reason breakdown

### Full Audit (Both)

```bash
make audit BASE_PATH=../../../manuals_src/docs/sbd-toe
```

Combines validation + recommendations for complete analysis.

## Python Usage

### Validate a Single File

```python
from tag_system.core import CanonicalTagsManager
from tag_system.validators import ValidationEngine

canonical = CanonicalTagsManager("../canonical-tags.yml")
validator = ValidationEngine(canonical)

result = validator.validate_file("../../../manuals_src/docs/sbd-toe/chapter/file.md")

print(f"Valid tags: {result.valid_tags}")
for issue in result.issues:
    print(f"  - {issue.issue_type.value}: {issue.message}")
    if issue.suggestion:
        print(f"    → {issue.suggestion}")
```

### Get Recommendations for a File

```python
from tag_system.core import CanonicalTagsManager
from tag_system.recommenders import RecommendationEngine

canonical = CanonicalTagsManager("../canonical-tags.yml")
recommender = RecommendationEngine(canonical)

recommendations = recommender.recommend_tags(
    filepath="../../../manuals_src/docs/sbd-toe/chapter/file.md",
    max_recommendations=5,
    min_confidence=0.65
)

for rec in recommendations:
    print(f"{rec.tag:<25} ({rec.confidence:.0%}) - {rec.reason}")
```

## Understanding Recommendations

### Confidence Factors

1. **Keyword Match** (0.0-0.4)
   - Tag name/description appears in content

2. **Semantic Relations** (+0.25)
   - Related to tags already in file
   - Example: If file has `sbom`, suggest `sca`, `supply-chain`

3. **Context Boost** (+0.2)
   - Tag exists in parent chapter
   - Example: File in `10-testes-seguranca/` inherits `testing`

4. **Related Tags** (+0.15)
   - Semantic siblings present in file

### Example

```
File: docs/05-sbom/addon/software-bill.md
Parent tags: [sbom, supply-chain]
Existing tags: [sbom]

Calculation for 'sca':
  - Keyword match: 0.3 (description found)
  - Semantic relation to 'sbom': +0.25
  - Result: 0.55 confidence ✓

Recommendation: sca (0.55) - keyword match; related to sbom
```

## Canonical Tags

All available tags are in `canonical-tags.yml` (489 tags).

Structure:

```yaml
tags:
  sbom:
    category: supply-chain
    description: Software Bill of Materials - component inventory
    aliases:
      - bill-of-materials
      - component-list
    related:
      - sca
      - supply-chain
      - dependencias
```

Add new tags by editing this file.

## Troubleshooting

### "ModuleNotFoundError: No module named 'tag_system'"

Make sure you're in the right directory:
```bash
cd src/tag-normalization/tag_system
```

Or activate virtual environment:
```bash
source ../.venv/bin/activate
```

### "Canonical tags file not found"

Check path is correct:
```bash
ls ../canonical-tags.yml
```

### No recommendations shown

This usually means:
- File already has complete tags
- Content has no keyword matches
- Confidence below threshold (default 0.65)

Try lowering threshold in code:
```python
recommendations = recommender.recommend_tags(
    filepath="...",
    min_confidence=0.5  # Lower threshold
)
```

## Next Steps

- [ ] Learn about semantic relations in `tag_system/README.md`
- [ ] Check tag categories in `canonical-tags.yml`
- [ ] Run full audit on your documentation
- [ ] Review and apply recommendations

---

**Need help?** See `tag_system/README.md` for architecture details.

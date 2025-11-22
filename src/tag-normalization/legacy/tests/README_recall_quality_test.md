# Multi-File Recall Quality Test

## Overview

This test suite analyzes tag recommendation accuracy across 4 diverse markdown files. It compares:

1. **Existing Tags** - What tags are currently in the file
2. **Robot Re-detection** - Can the system find these tags from content analysis?
3. **New Suggestions** - What high-confidence tags does the system recommend?

## Running the Tests

```bash
cd src/tag-normalization
source .venv/bin/activate
python3 tests/recall_quality_test_multifile.py
```

## Output

The script generates two files in `tests/results/`:

- `multifile_recall_analysis_TIMESTAMP.json` - Structured data for analysis
- `multifile_recall_analysis_TIMESTAMP.txt` - Human-readable report

## Test Files (Latest Run)

The test automatically selects 4 markdown files with existing tags:

| File | Existing Tags | Re-detected | Recall |
|------|---------------|-------------|--------|
| 002-cross-check-normativo/01-intro.md | 10 | 0 | 0.0% |
| 002-cross-check-normativo/cra/01-intro.md | 6 | 0 | 0.0% |
| 002-cross-check-normativo/cra/02-playbook.md | 5 | 0 | 0.0% |
| 002-cross-check-normativo/dora/01-intro.md | 6 | 0 | 0.0% |

**Summary:**
- Files analyzed: 4
- Total existing tags: 27
- Successfully re-detected: 0 (0.0% average recall)
- New high-confidence suggestions: 20

## Key Findings

### Current State
- The recommendation engine suggests 5 new tags per file at 70%+ confidence
- However, it currently fails to re-detect EXISTING tags from content
- This indicates tags are largely **structural/semantic** rather than content-based

### Classification of Tags
Based on earlier analysis:
- **50.1%** of tags are content-based (appear in document text)
- **49.9%** of tags are structural (administrative/organizational only)

Top structural tags (often not in content):
- `seguranca` (65 files)
- `validacao` (48 files)
- `cicd` (23 files)
- `compliance`, `cross-check`, `normativos` (regulatory tags)

### Implications
This 0% recall rate on certain tag types is **expected behavior**, indicating:
1. Many tags are intentionally assigned for organizational/indexing purposes
2. The recommendation engine finds content-based tags but misses structural ones
3. A hybrid approach is needed: keyword-based + structural inference

## Next Steps

1. **Classify tags** - Identify which are content-based vs structural
2. **Implement structural inference** - Recognize context clues (file path, parent chapter)
3. **Tune thresholds** - Different thresholds for different tag types
4. **Validate results** - Compare with human manual tagging

## Files

- `recall_quality_test_multifile.py` - Main test script
- `results/` - Generated reports and data
- `README_recall_quality_test.md` - This file

## Previous Versions

Earlier analysis with the toolchain example showed better results (83% recall), 
suggesting the system performs better on content-rich files with explicit technical terms.

## References

- `CASE_STUDY_TOOLCHAIN.py` - Single-file detailed analysis example
- `test_recall_quality.py` - Original single-file recall test
- `analyze_structural_tags.py` - Tag classification system

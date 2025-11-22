# Legacy Archive

This directory contains archived development artifacts from earlier phases of tag normalization system development. These files are preserved for reference but are no longer part of the active pipeline.

## Directory Structure

```
legacy/
├── analysis/          # Analysis scripts and reports from earlier research
├── demos/             # Demo implementations and test cases
├── docs/              # Historical documentation and getting started guides
├── reports/           # Analysis reports and tools
├── tests/             # Quality test suites and diagnostic tools
└── README.md          # This file
```

## Contents by Folder

### `/analysis`
Early-stage analysis comparing RAG vs pattern-based approaches:
- `ANALYSIS_RAG_vs_Patterns.txt` - Detailed comparison of tagging strategies
- `RAG_COMPLETE_SYSTEM_ANALYSIS.txt` - Comprehensive system analysis
- `RAG_EMBEDDINGS_ANALYSIS.py` - Embedding analysis script
- Various supporting scripts for strategy evaluation

**Status**: ✅ Analysis completed, insights integrated into current RAG system

### `/demos`
Demo implementations showing system functionality:
- `DEMO-README.md` - Demo documentation
- `DEMO-SAMPLE.md` - Sample tagged content
- `demo.py` - Demo script
- `SISTEMA-FUNCIONANDO.txt` - System operational notes

**Status**: ✅ Reference material, functionality now in Makefile

### `/docs`
Historical documentation:
- `GETTING-STARTED.md` - Original getting started guide
- `QUICK-START.md` - Quick reference (superseded by Makefile)
- `DEMO-NO-TAGS-SAMPLE.md` - Sample without tags
- `DEMO-READY.txt` - Preparation notes
- `ESTRUTURA-FINAL.txt` - Final structure notes

**Status**: ✅ Archived for reference, current docs in parent README.md

### `/reports`
Analysis and reporting tools:
- `analyze_recommendations.py` - Recommendation analysis
- `analyze_structural_tags.py` - Tag structure analysis
- `scan_chapters.py` - Chapter scanning tool
- `show_gaps.py` - Gap identification
- `tag-analysis-report.json` - Archived analysis results
- `view_report.py` - Report viewer

**Status**: ✅ Tools archived, gap analysis now in Makefile (`make gaps F=...`)

### `/tests`
Quality and recall testing suite:
- `test_recall_quality.py` - Recall quality tests
- `test_recommendation_quality.py` - Recommendation quality
- `diagnostic_recall.py` - Diagnostic tools
- `recall_quality_test_multifile.py` - Multi-file testing
- Supporting test infrastructure and results

**Status**: ✅ Testing framework archived, core validation automated in indexing

## Why These Files Are Archived

**Phase A (Complete)**: Cleanup & Organization
- Separated legacy development artifacts from active pipeline
- Preserved historical analysis for reference
- Organized by function (analysis, demos, docs, reports, tests)

**Phase B (Current)**: RAG Integration & Auto-tagging
- Focus on semantic search integration with existing tag system
- Auto-tagging of all 291 content files
- Measurement of recall/precision improvements

**Phase C (Planning)**: Production Deployment
- Full automation of tagging pipeline
- Performance optimization
- Documentation updates

## How to Access If Needed

If you need to reference historical analysis or run legacy tools:

```bash
# Access specific analysis
cat legacy/analysis/ANALYSIS_RAG_vs_Patterns.txt

# Run legacy tests
python legacy/tests/test_recall_quality.py

# Review demo implementations
python legacy/demos/demo.py

# Generate legacy report
python legacy/reports/show_gaps.py
```

## Migration to Current System

**Old Approach** (archived):
- Manual pattern-based tagging
- External analysis tools
- Separate test suites

**New Approach** (active):
- Semantic RAG system (see parent README.md)
- Unified Makefile command interface
- Integrated testing via `make health`
- 291 files indexed, <100ms search latency

## Timeline

| Phase | Status | Date | Artifacts |
|-------|--------|------|-----------|
| Phase A | ✅ Complete | 2024-11-22 | Organized legacy/, cleanup complete |
| Phase B | 🔄 In Progress | Current | RAG integration, auto-tagging |
| Phase C | ⏳ Planning | Next | Production deployment |

## See Also

- Parent `README.md` - Current active system documentation
- `Makefile` - Command automation for RAG operations
- `canonical-tags.yml` - Active tag taxonomy
- `tag_system/` - Core tagging system code

---

**Note**: These archived files are preserved for historical reference and can be safely ignored during normal RAG operations. They do not affect the current tagging pipeline.

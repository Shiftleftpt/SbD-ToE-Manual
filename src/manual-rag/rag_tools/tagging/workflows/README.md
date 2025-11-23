# 🏷️ Tagging Workflows - Complete Guide

## Overview

**3-step process for safe, reviewable tag management:**

1. **ANALYZE** - Deep exploration of all proposed changes
2. **REVIEW** - Human-in-the-loop CSV approval
3. **APPLY** - Apply only approved changes

---

## 🔄 Complete Workflow

### Step 1: ANALYZE - Detailed Exploration

**Purpose:** Understand what changes will happen and why.

```bash
cd rag_tools/tagging/workflows
python3 analyze_tag_changes.py [OPTIONS]
```

**Output:** `tag_analysis_TIMESTAMP.json`

**Contains for each file:**
- Current tags (with breakdown by type)
- Proposed tags (with confidence levels)
- Detailed additions (why each will be added)
- Detailed removals (why each will be removed)
- All suggestions considered (with reasoning)
- Recommendation (✅ APPROVE, ⚠️ REVIEW, 🤔 INVESTIGATE)

**Options:**
- `--sample N` - Analyze only N files (0 = all)
- `--chapter NAME` - Filter by chapter name
- `--max-tags 7` - Target number of tags per document

**Example:**
```bash
# Analyze first 5 files
python3 analyze_tag_changes.py --sample 5 --output my_analysis.json

# Look for "INVESTIGATE" recommendations
grep "INVESTIGATE" my_analysis.json
```

**JSON Structure:**
```json
{
  "metadata": {...},
  "global_stats": {
    "total_files": 100,
    "files_with_additions": 23,
    "files_with_removals": 0,
    "total_tags_to_add": 45,
    "by_confidence_level": {
      "high": 34,
      "medium": 8,
      "low": 3
    }
  },
  "files": [
    {
      "file": "sbd-toe/chapter/intro.md",
      "current": {
        "tags": ["tag1", "tag2"],
        "count": 2,
        "breakdown": {...}
      },
      "proposed": {
        "tags": ["tag1", "tag2", "tag3"],
        "count": 3
      },
      "changes": {
        "added": {
          "count": 1,
          "tags": {
            "tag3": {
              "confidence": "75%",
              "reasoning": "..."
            }
          }
        },
        "removed": {...},
        "net_change": 1
      },
      "recommendation": "✅ APPROVE"
    }
  ]
}
```

---

### Step 2: REVIEW - Generate CSV for Approval

**Purpose:** Create human-editable review interface.

```bash
python3 generate_review_report.py [OPTIONS]
```

**Output:** 
- `review_report_TIMESTAMP.csv` - For review and editing
- `review_report_TIMESTAMP.json` - For programmatic processing

**CSV Format:**

| Column | Purpose |
|--------|---------|
| CHAPTER | Chapter name (for context) |
| FILE | File path |
| SUMMARY | First 100 chars of content |
| CURRENT_TAGS | Tags before (pipe-separated) |
| PROPOSED_TAGS | Tags after (pipe-separated) |
| TAGS_ADDED | New tags being added |
| TAGS_REMOVED | Old tags being removed |
| RATIONALE_ADDED | Why each tag was added (confidence, source, reason) |
| APPROVAL_STATUS | **PENDING** (default) or **OK** (to approve) |

**Options:**
- `--sample N` - Process only N files
- `--chapter NAME` - Filter by chapter
- `--max-tags 7` - Max tags per document

**Example CSV Row:**
```csv
sbd-toe/010-sbd-manual,intro.md,"Security basics",iso27001|gdpr,iso27001|gdpr|devsecops,devsecops,,"devsecops(75%,rag:matches security context)",PENDING
```

**How to Use:**

1. **Open the CSV** in Excel, Google Sheets, or your editor
2. **Review each row:**
   - Check PROPOSED_TAGS makes sense
   - Look at RATIONALE_ADDED for confidence scores
   - Read SUMMARY to understand the content
3. **Approve changes:**
   - Change `PENDING` → `OK` for rows to apply
   - Leave `PENDING` to skip
4. **Edit if needed:**
   - Modify PROPOSED_TAGS (pipe-separated) if you disagree
   - Remove tags or add new ones

**Example Editing:**
```
BEFORE:
PROPOSED_TAGS: iso27001|gdpr|devsecops|cicd|kubernetes
APPROVAL_STATUS: PENDING

AFTER (you edited it):
PROPOSED_TAGS: iso27001|gdpr|devsecops
APPROVAL_STATUS: OK
(You removed cicd and kubernetes - they'll be skipped)
```

---

### Step 3: APPLY - Apply Approved Changes

**Purpose:** Update files with approved tags.

```bash
python3 apply_review_decisions.py REVIEW_CSV_FILE
```

**Behavior:**
- ✅ **Processes only rows with `APPROVAL_STATUS=OK`**
- Reads PROPOSED_TAGS from your edited CSV
- Updates file frontmatter
- Shows summary of changes

**Example:**
```bash
# Apply the CSV you edited
python3 apply_review_decisions.py review_report_2025-11-23T16-17-06.csv
```

**Output:**
```
🔄 APPLYING TAG CHANGES FROM REVIEW REPORT
════════════════════════════════════════════
Loaded 100 review decisions

✅ file1.md
   + devsecops|cicd
   - old_tag

✅ file2.md
   + iso27001
   
⊘ file3.md (no changes)

📊 APPLICATION SUMMARY
Files processed: 100
Changes applied: 23
Changes skipped: 77 (PENDING status)
Errors: 0

✅ SUCCESS: 23 files updated
```

---

## Quality Safeguards

### Confidence Levels

Tags are only suggested if they meet quality thresholds:

- **High (≥70%)** - High confidence, safe to add
- **Medium (50-70%)** - Medium confidence, review carefully
- **Low (<50%)** - Low confidence, probably should skip

**Default behavior:**
- `analyze_tag_changes.py` shows ALL suggestions (for exploration)
- `generate_review_report.py` uses smart selection (≥60% minimum)
- `regen_intro_tags.py` only accepts high-confidence (≥60%)

### Mandatory Tags

Certain tags are always preserved:
- `tipo:*` (e.g., `tipo:seguranca`)
- `tema:*` (e.g., `tema:compliance`)
- Existing tags (user intent)

### Tag Organization

**What goes in TAGS:**
- `tipo:*`, `tema:*` (mandatory framework)
- Frameworks: `iso27001`, `gdpr`, `dora`, `nis2`, `nist`
- Technical: `cicd`, `containers`, `sast`, `dast`, `sbom`, `sca`
- Practice: `playbook`, `exemplo`, `checklist`

**What goes in FRONTMATTER fields (not tags):**
- `categoria:` - Document category
- `group:` - Document group

---

## Common Scenarios

### Scenario 1: Review All Changes

```bash
# Analyze to understand
python3 analyze_tag_changes.py

# Generate for review
python3 generate_review_report.py

# Edit CSV, mark all OK
# Then apply
python3 apply_review_decisions.py review_report_*.csv
```

### Scenario 2: Review High-Risk Changes Only

```bash
# Analyze with focus on big changes
python3 analyze_tag_changes.py --output analysis.json

# Search for high-impact files (jq or grep)
grep -l "large" analysis.json

# Generate report
python3 generate_review_report.py

# Edit CSV: approve low-risk, review high-risk
# Run apply
python3 apply_review_decisions.py review_report_*.csv
```

### Scenario 3: Regenerate Specific Chapter

```bash
# Analyze just one chapter
python3 analyze_tag_changes.py --chapter "010-sbd-manual"

# Review
python3 generate_review_report.py --chapter "010-sbd-manual"

# Edit and apply
python3 apply_review_decisions.py review_report_*.csv
```

---

## Troubleshooting

### "No files found"
- Check that files have existing tags: `tags: [...]`
- Check path filters match your files

### "High confidence distribution is low"
- This is normal! The tagger is conservative
- Increase `min_confidence` to see more suggestions (lower quality)
- Or manually edit CSV to add suggestions you trust

### "Changes don't apply"
- Check CSV APPROVAL_STATUS is `OK` (not `PENDING`)
- Verify file path is correct (use `|` not `,` for tag separator)
- Check for syntax errors in PROPOSED_TAGS

---

## Performance

- **analyze_tag_changes.py**: ~200ms per file
- **generate_review_report.py**: ~150ms per file  
- **apply_review_decisions.py**: ~10ms per file

For large corpus:
- Use `--sample N` to test first
- Or use `--chapter` to focus on specific areas

---

## Next Steps

1. **Try it:** `bash test_tagging_workflow.sh`
2. **Review:** Open generated JSON and CSV
3. **Understand:** Read the recommendations
4. **Customize:** Adjust CSV as needed
5. **Apply:** Run apply script

---

## FAQ

**Q: What if I disagree with a suggestion?**
A: Edit the CSV and change PROPOSED_TAGS to what you want. Or mark PENDING to skip entirely.

**Q: Can I manually add tags not in suggestions?**
A: Yes! Edit PROPOSED_TAGS in the CSV to include them.

**Q: How many tags should each file have?**
A: Target: 5-7 tags. The system enforces a max of 7 to keep UI clean.

**Q: What's the difference between analyze and review?**
A: Analyze shows ALL considerations. Review creates the CSV for human approval.

**Q: Can I run this on all files at once?**
A: Yes, omit `--sample` parameter. But start with a sample first to understand the changes.

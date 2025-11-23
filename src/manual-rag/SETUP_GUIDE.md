# 🚀 Getting Started - New Machine Setup

Complete guide to set up the RAG system on a new machine or fresh checkout.

## Quick Start (Automated)

### Option 1: Bash Script (macOS/Linux)
```bash
cd src/manual-rag
bash setup.sh
```

### Option 2: Python Script (All Platforms - Recommended)
```bash
cd src/manual-rag
python3 setup.py
```

**That's it!** The script will:
1. ✅ Create virtual environment
2. ✅ Install all dependencies
3. ✅ Build the RAG index (2-3 minutes)
4. ✅ Run tests to verify everything works

---

## Manual Setup (Step by Step)

If you prefer to do it yourself or the scripts don't work:

### Step 1: Create Virtual Environment
```bash
cd src/manual-rag
python3 -m venv rag_env
```

### Step 2: Activate Virtual Environment
```bash
# macOS/Linux
source rag_env/bin/activate

# Windows
rag_env\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

### Step 4: Build the Index
```bash
python3 -m rag_core.indexing.chunked_build
```

**⏱️ This takes 2-3 minutes**

Output should show:
```
📊 Document Statistics:
  Total files: 276
  Total chunks: 5066
  Average chunk size: 450 tokens
✅ Index built successfully
```

### Step 5: Verify Setup
```bash
python3 -m pytest rag_core/tests/ -v
```

**Should show: `26 passed` ✅**

---

## After Setup

### On Future Sessions (Same Machine)

Just activate the environment:
```bash
cd src/manual-rag
source rag_env/bin/activate
```

Everything else is cached/persisted:
- ✅ Virtual environment with all packages
- ✅ Chroma vector index (stored in `index/`)
- ✅ JSONL dataset (stored in `datasets/`)

### Running Tagging Workflow

Once setup is complete:

```bash
# Generate suggestions (1-2 minutes)
python3 -m rag_tools.workflows.generate_review_report --max-tags 7

# Review the CSV, then apply
python3 -m rag_tools.workflows.apply_review_decisions review_report_*.csv
```

### Running Tests

```bash
# All tests
python3 -m pytest

# Specific module
python3 -m pytest rag_core/tests/ -v
python3 -m pytest rag_tools/tagging/tests/ -v

# With coverage
pytest --cov=rag_core --cov=rag_tools --cov-report=html
```

---

## Troubleshooting

### "Python 3 not found"
Install Python 3.8+:
- **macOS:** `brew install python@3.11`
- **Windows:** Download from [python.org](https://www.python.org/downloads/)
- **Linux:** `sudo apt install python3.11`

### "venv already exists, want to recreate?"
If something went wrong with dependencies:
```bash
rm -rf rag_env
python3 setup.py  # or bash setup.sh
```

### "Module not found" errors
Make sure venv is activated:
```bash
# Check if venv is active (should see "rag_env" in prompt)
source rag_env/bin/activate

# Reinstall if needed
pip install -r requirements.txt
```

### "Ollama not running" (non-fatal warning)
The system will still work, just uses pattern matching instead of LLM:
```bash
# Optional: Start Ollama for LLM suggestions
ollama pull mistral
ollama serve &
```

### Tests are failing
Try a clean setup:
```bash
rm -rf rag_env
python3 setup.py
```

---

## Different Checkouts/Branches

Each checkout can have its own setup:

```bash
# Checkout branch/commit
git checkout feature-branch

# Setup that specific checkout
cd src/manual-rag
python3 setup.py

# Now that checkout is ready to use
```

Each has independent:
- Virtual environment
- Installed packages
- Built indexes
- Test results

---

## What Gets Created?

After setup, you'll have:

```
manual-rag/
├── rag_env/              # Virtual environment (git-ignored)
│   ├── bin/              # Python executables
│   └── lib/              # Installed packages
│
├── index/                # Chroma vector index (git-ignored)
│   └── chroma-data/
│
├── datasets/             # JSONL datasets (git-ignored)
│   └── chunked_index.jsonl
│
├── .pytest_cache/        # Test cache (git-ignored)
└── [rest of source code]
```

**Git-ignored files** (in `.gitignore`):
- `rag_env/` - Virtual environment
- `index/` - Vector index
- `datasets/` - JSONL data
- `.pytest_cache/` - Test cache
- `*.csv` - Review reports

---

## File Sizes & Time Estimates

| Operation | Time | Size |
|-----------|------|------|
| Create venv | 30s | ~300MB |
| Install dependencies | 2-3 min | +200MB |
| Build index | 2-3 min | ~50MB (Chroma) |
| Generate tags | 1-2 min | - |
| Run tests | ~45s | - |
| **Total setup** | **~8-10 minutes** | **~550MB** |

---

## 📚 Next Steps

1. **Read the workflow docs:** [EXECUTION_GUIDE.md](EXECUTION_GUIDE.md)
2. **Understand the architecture:** [README.md](README.md)
3. **Review infrastructure:** [rag_core/README.md](rag_core/README.md)
4. **Learn about tools:** [rag_tools/README.md](rag_tools/README.md)
5. **Start tagging:** `python3 -m rag_tools.workflows.generate_review_report --max-tags 7`

---

## Quick Reference

```bash
# Setup (one time)
python3 setup.py

# Activate (every session)
source rag_env/bin/activate

# Build index (after file changes)
python3 -m rag_core.indexing.chunked_build

# Generate tags
python3 -m rag_tools.workflows.generate_review_report --max-tags 7

# Apply tags
python3 -m rag_tools.workflows.apply_review_decisions review_report_*.csv

# Run tests
python3 -m pytest
```

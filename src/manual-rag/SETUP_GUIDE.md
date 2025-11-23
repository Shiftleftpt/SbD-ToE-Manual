# 🚀 Getting Started - Setup with Make

Complete guide to set up the RAG system on a new machine or fresh checkout.

## Quick Start (One Command)

```bash
cd src/manual-rag
make setup
```

**That's it!** Make will:
1. ✅ Create virtual environment
2. ✅ Install all dependencies
3. ✅ Build the RAG index (2-3 minutes)
4. ✅ Run tests to verify everything works

---

## Manual Setup (Step by Step)

If you prefer to do it yourself:

### Step 1: Create Virtual Environment
```bash
cd src/manual-rag
make install  # This also creates venv if needed
```

### Step 2: Build the Index
```bash
make build
```

**⏱️ This takes 2-3 minutes**

Output should show:
```
Building RAG index (advanced chunked)...
This may take 2-3 minutes...
✓ Index built successfully
```

### Step 3: Verify Setup
```bash
make test
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
make generate-tags

# Review the CSV, then apply
make apply-tags CSV=review_report_*.csv
```

### Running Tests

```bash
# All tests
make test

# Specific module
make test-core

# With coverage
make test-cov
```

### Other Make Commands

```bash
# Build index
make build              # Advanced (recommended)
make build-simple       # Simple indexing

# Show all commands
make help
```

---

## Troubleshooting

### "make: command not found"
Install make:
- **macOS:** `brew install make`
- **Windows:** Use WSL or `make` from MinGW
- **Linux:** `sudo apt install make`

### "venv already exists, want to recreate?"
If something went wrong with dependencies:
```bash
make clean
make setup
```

### "Module not found" errors
Make sure venv is activated:
```bash
source rag_env/bin/activate
make install
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
make clean
make setup
```

---

## Different Checkouts/Branches

Each checkout can have its own setup:

```bash
# Checkout branch/commit
git checkout feature-branch

# Setup that specific checkout
cd src/manual-rag
make setup

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
5. **Start tagging:** `make generate-tags`

---

## Quick Reference

```bash
# Setup (one time)
make setup

# Activate (every session)
source rag_env/bin/activate

# Build index (after file changes)
make build

# Generate tags
make generate-tags

# Apply tags
make apply-tags CSV=review_report_*.csv

# Run tests
make test

# See all commands
make help
```

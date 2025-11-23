# 🤔 Setup: Which Tool to Use?

You have **3 ways** to set up the RAG system. They all do the same thing - pick whichever you prefer!

## 📊 Comparison

| Method | Best For | Command | Platform |
|--------|----------|---------|----------|
| **setup.py** | Any OS, recommended | `python3 setup.py` | ✅ All (Linux, macOS, Windows) |
| **setup.sh** | Quick on macOS/Linux | `bash setup.sh` | ⚠️ macOS/Linux only |
| **Makefile** | Developers, make users | `make setup` | ⚠️ Requires make, macOS/Linux |

---

## 🎯 What Each One Does

All three do the same thing in this order:
1. Create virtual environment (`rag_env/`)
2. Install dependencies (`pip install -r requirements.txt`)
3. Build RAG index (2-3 minutes)
4. Run tests to verify (26 tests ✅)

---

## ✅ Quick Decision Guide

### "I just want it to work"
```bash
python3 setup.py  ← Easiest, cross-platform
```

### "I'm on macOS/Linux and want to keep it simple"
```bash
bash setup.sh     ← Direct and simple
```

### "I'm a developer familiar with make"
```bash
make setup        ← Familiar tool, more options
```

---

## 🔍 Detailed Comparison

### `setup.py` (Cross-Platform)
**Pros:**
- ✅ Works on Windows, macOS, Linux
- ✅ Self-contained, no dependencies
- ✅ Colorized output
- ✅ Clear error messages
- ✅ Best for CI/CD

**Cons:**
- None really

**Use when:**
- You want maximum compatibility
- You're setting up on any OS
- You want to automate setup

---

### `setup.sh` (Bash Script)
**Pros:**
- ✅ Direct shell script
- ✅ Minimal overhead
- ✅ Easy to read and modify
- ✅ Good for shell-savvy users

**Cons:**
- ❌ Only works on macOS/Linux
- ❌ Won't work on Windows (unless WSL)

**Use when:**
- You're on macOS or Linux
- You want simplicity
- You prefer bash scripting

---

### `Makefile`
**Pros:**
- ✅ Familiar to developers
- ✅ More commands than just setup (build, test, clean)
- ✅ Tab completion support
- ✅ Easy to add custom targets

**Cons:**
- ❌ Only on macOS/Linux (requires `make`)
- ❌ Setup is one of many commands (less focused)

**Use when:**
- You're a developer who uses make
- You need multiple operations (build, test, etc)
- You want `make test`, `make clean`, etc

---

## 🚀 All Three Methods in Action

### Method 1: Python Script
```bash
$ python3 setup.py

🚀 Manual RAG - Setup & Initialization
══════════════════════════════════════
→ Checking Python version...
✅ Python 3.10.1 found
...
✨ Setup Complete! ✨
```

### Method 2: Bash Script
```bash
$ bash setup.sh

🚀 Manual RAG - Setup & Initialization
══════════════════════════════════════
✅ Python 3.10.1 found
...
✨ Setup Complete! ✨
```

### Method 3: Makefile
```bash
$ make setup

Manual RAG System - Make Commands

→ Creating virtual environment...
✓ Virtual environment created
...
✨ Setup Complete! ✨
```

---

## 💡 My Recommendation

**For 90% of users:** Use `python3 setup.py`
- Works everywhere
- Simple one-liner
- No dependencies
- Clear output

**For developers:** Use `make setup`
- Get access to `make build`, `make test`, etc
- Familiar tool
- More control

**For shell enthusiasts:** Use `bash setup.sh`
- Direct approach
- Easy to understand
- No abstractions

---

## 📝 After Setup (All Methods)

After any of the three setup methods complete, you use the same commands:

```bash
# Activate environment (every session)
source rag_env/bin/activate

# Generate tags
python3 -m rag_tools.workflows.generate_review_report --max-tags 7

# Apply tags
python3 -m rag_tools.workflows.apply_review_decisions review_report_*.csv

# Run tests
python3 -m pytest
```

Or with make:
```bash
make generate-tags
make apply-tags CSV=review_report_*.csv
make test
```

---

## 🔄 Other Make Commands

If you choose Makefile, here are the additional commands available:

```bash
make build              # Build index
make build-simple       # Simple index
make rebuild            # Clean + build
make test               # Run all tests
make test-core          # Core tests only
make test-cov           # Tests with coverage
make generate-tags      # Generate suggestions
make apply-tags CSV=... # Apply changes
make clean              # Remove venv
make activate           # Show activation command
```

---

## ❓ FAQ

**Q: Can I use setup.py on Windows?**
A: Yes! It's the only one that works on Windows.

**Q: Can I use Makefile on Windows?**
A: Only if you have `make` installed (via MinGW, WSL, etc). Use `setup.py` instead.

**Q: Which is fastest?**
A: All three are equally fast - they run the same commands.

**Q: Can I switch between methods?**
A: Yes, but you need to delete `rag_env/` first to start fresh.

**Q: What if setup fails?**
A: Read [SETUP_GUIDE.md](SETUP_GUIDE.md) troubleshooting section.

---

## 📚 See Also

- [SETUP_GUIDE.md](SETUP_GUIDE.md) - Detailed setup instructions
- [README.md](README.md) - Project overview
- [EXECUTION_GUIDE.md](EXECUTION_GUIDE.md) - How to run tagging

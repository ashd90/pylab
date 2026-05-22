# 🐍 PyLab — Python Mastery, the Right Way

> A structured, project-based curriculum built for beginners — blending deep theory
> with hands-on code. Based on [roadmap.sh/python](https://roadmap.sh/python)
> Tracked on GitHub · Practiced on CachyOS Linux.

---

## 📌 About This Repository

`pylab` is my personal Python learning lab. Every concept is studied in depth,
practiced through **3–4 focused exercises**, and validated through a **real-world
mini-project** before moving on. No rushing. No skipping.

| Property | Detail |
|---|---|
| **Skill Level** | Absolute Beginner → Advanced |
| **OS** | CachyOS Linux (Arch-based) |
| **IDE** | VS Code / Neovim |
| **Python Version** | 3.12+ (managed via `pyenv`) |
| **Reference** | [roadmap.sh/python](https://roadmap.sh/python) |
| **Methodology** | Theory → Exercises (×3–4) → Project → Validate → Advance |

---

## 🗺️ Learning Roadmap
---

## 📁 Repository Structure
---

## 📚 Section README Layout

Every phase folder contains a `README.md` with this consistent structure:
---

## 💻 IDE Setup — CachyOS Linux

### ⭐ Option 1: VS Code (Recommended for beginners)

```bash
# Install via AUR
yay -S vscodium-bin        # open-source build (recommended)
# or
yay -S visual-studio-code-bin   # official Microsoft build

# Essential extensions
# Python        → ms-python.python
# Pylance       → ms-python.pylance
# Black         → ms-python.black-formatter
# Error Lens    → usernamehw.errorlens
# GitLens       → eamodio.gitlens
```

### Option 2: PyCharm Community Edition (Free)

```bash
yay -S pycharm-community-edition
```

### Option 3: Neovim + LazyVim (Terminal native, blazing fast)

```bash
yay -S neovim
# Follow https://lazyvim.org → add pyright + ruff via Mason
```

---

## ⚙️ First-Time Setup (Quick Start)

```bash
# 1. Install pyenv (Python version manager)
curl https://pyenv.run | bash

# 2. Add to ~/.bashrc (or ~/.zshrc)
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# 3. Reload shell and install Python 3.12
source ~/.bashrc
pyenv install 3.12.0
pyenv global 3.12.0

# 4. Clone this repo
git clone https://github.com/YOUR_USERNAME/pylab.git ~/repoHive/pylab
cd ~/repoHive/pylab

# 5. Create a virtual environment per phase
python -m venv .venv
source .venv/bin/activate
```

---

## 🔧 Git Workflow

```bash
# Start a new exercise or phase
git checkout -b phase-01/ex02-variables

# After finishing
git add .
git commit -m "feat(01-basics): ex02 variables and type casting complete"
git push origin phase-01/ex02-variables
```

### Commit Message Convention
---

## 🧠 Learning Principles

1. **Theory before code** — understand visually before writing a single line
2. **3–4 exercises per concept** — repetition builds genuine muscle memory
3. **No copy-paste** — type every exercise by hand to train fingers and brain together
4. **Project to validate** — only start the section project when exercises feel natural
5. **Git everything** — every exercise, even incomplete ones, gets committed
6. **Checkpoint before advancing** — answer the checkpoint questions before the next phase

---

## 📈 Progress Tracker

| Phase | Topic | Status | Project |
|---|---|---|---|
| 00 | Setup & Environment | ⬜ Not Started | — |
| 01 | Python Basics | ⬜ Not Started | Tip Calculator |
| 02 | Control Flow | ⬜ Not Started | Number Guessing Game |
| 03 | Functions | ⬜ Not Started | Unit Converter |
| 04 | Data Structures | ⬜ Not Started | Student Grade Manager |
| 05 | OOP | ⬜ Not Started | Bank Account System |
| 06 | Modules & Packages | ⬜ Not Started | File Organizer |
| 07 | Advanced Python | ⬜ Not Started | Async Data Pipeline |
| 08 | Testing & Exceptions | ⬜ Not Started | Tested Calculator |
| 09 | Web & Data Capstone | ⬜ Not Started | Personal Finance Tracker |

> Update ⬜ → 🟡 (In Progress) → ✅ (Complete) as you advance.

---

## 📖 Resources

| Resource | URL |
|---|---|
| Official Python Docs | https://docs.python.org/3/ |
| roadmap.sh/python | https://roadmap.sh/python |
| Real Python | https://realpython.com |
| Python Cheatsheet | https://www.pythoncheatsheet.org |
| Exercism Python Track | https://exercism.org/tracks/python |
| PEP Index | https://peps.python.org |

---

## 📝 License

This repository is for personal learning. All code is original unless attributed.

---

*Started: 2026 · Maintained by Ashish · CachyOS Linux*

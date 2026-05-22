# 🐍 PyLab — Python Mastery, the Right Way

> A structured, project-based curriculum built for beginners — blending deep theory
> with hands-on code. Based on [roadmap.sh/python](https://roadmap.sh/python)
> Tracked on GitHub · Practiced on CachyOS Linux.

---

## 📌 About This Repository

`pylab` is my personal Python learning lab. Every concept is studied in depth,
practiced through **3–4 focused exercises**, and validated through a **real-world
mini-project** before moving on. No rushing. No skipping.

| Property       | Detail                                         |
|----------------|------------------------------------------------|
| **Skill Level**    | Absolute Beginner → Advanced               |
| **OS**             | CachyOS Linux (Arch-based)                 |
| **IDE**            | VS Code / Neovim                           |
| **Python Version** | 3.12+ (managed via `pyenv`)               |
| **Reference**      | [roadmap.sh/python](https://roadmap.sh/python) |
| **Methodology**    | Theory → Exercises (×3–4) → Project → Validate → Advance |

---

## 🗺️ Learning Roadmap

    Phase 00 → Setup & Environment
    Phase 01 → Python Basics
    Phase 02 → Control Flow
    Phase 03 → Functions
    Phase 04 → Data Structures
    Phase 05 → Object-Oriented Programming (OOP)
    Phase 06 → Modules & Packages
    Phase 07 → Advanced Python
    Phase 08 → File I/O, Exceptions & Testing
    Phase 09 → Web, Data Science & Capstone Projects

---

## 📁 Repository Structure

    ~/repoHive/pylab/
    │
    ├── README.md                        ← You are here — curriculum homepage
    │
    ├── 00-setup/
    │   ├── README.md                    ← Setup theory, steps, troubleshooting
    │   └── notes.md
    │
    ├── 01-basics/
    │   ├── README.md                    ← Theory + FAQ + Production Q&A
    │   ├── ex01_hello_world.py
    │   ├── ex02_variables.py
    │   ├── ex03_data_types.py
    │   ├── ex04_type_casting.py
    │   └── project/
    │       └── tip_calculator.py
    │
    ├── 02-control-flow/
    │   ├── README.md
    │   ├── ex01_if_else.py
    │   ├── ex02_for_loops.py
    │   ├── ex03_while_loops.py
    │   ├── ex04_match_case.py
    │   └── project/
    │       └── number_guessing_game.py
    │
    ├── 03-functions/
    │   ├── README.md
    │   ├── ex01_basic_functions.py
    │   ├── ex02_args_kwargs.py
    │   ├── ex03_recursion.py
    │   ├── ex04_lambda_scope.py
    │   └── project/
    │       └── unit_converter.py
    │
    ├── 04-data-structures/
    │   ├── README.md
    │   ├── ex01_lists.py
    │   ├── ex02_tuples_sets.py
    │   ├── ex03_dictionaries.py
    │   ├── ex04_comprehensions.py
    │   └── project/
    │       └── student_grade_manager.py
    │
    ├── 05-oop/
    │   ├── README.md
    │   ├── ex01_classes_objects.py
    │   ├── ex02_inheritance.py
    │   ├── ex03_dunder_methods.py
    │   ├── ex04_polymorphism.py
    │   └── project/
    │       └── bank_account_system.py
    │
    ├── 06-modules-packages/
    │   ├── README.md
    │   ├── ex01_stdlib_os_path.py
    │   ├── ex02_stdlib_datetime.py
    │   ├── ex03_third_party_requests.py
    │   ├── ex04_custom_package/
    │   └── project/
    │       └── file_organizer.py
    │
    ├── 07-advanced-python/
    │   ├── README.md
    │   ├── ex01_decorators.py
    │   ├── ex02_generators.py
    │   ├── ex03_context_managers.py
    │   ├── ex04_async_await.py
    │   └── project/
    │       └── data_pipeline.py
    │
    ├── 08-testing-exceptions/
    │   ├── README.md
    │   ├── ex01_try_except.py
    │   ├── ex02_custom_exceptions.py
    │   ├── ex03_pytest_basics.py
    │   ├── ex04_tdd_example.py
    │   └── project/
    │       └── tested_calculator/
    │
    └── 09-web-data-capstone/
        ├── README.md
        ├── fastapi-todo-api/
        ├── pandas-data-analysis/
        ├── django-blog/
        └── capstone-project/

---

## 📚 Section README Layout

Every phase folder contains a `README.md` with this consistent structure:

    1. Brief Theory          → concept explained plainly, text-based
    2. Key Syntax            → code patterns to memorize
    3. Exercises             → 3–4 practice scripts with learning goals
    4. Project               → real-world mini-project to apply knowledge
    5. FAQ                   → common beginner confusions answered
    6. Real-World Q&A        → production-level questions and answers
    7. Troubleshooting       → common errors and their fixes
    8. Checkpoint            → questions to validate mastery before advancing

---

## 💻 IDE Setup — CachyOS Linux

**Option 1 — VS Code (Recommended for beginners)**

Install via AUR:

    yay -S vscodium-bin              # open-source build (recommended)
    yay -S visual-studio-code-bin    # official Microsoft build

Essential extensions to install (`Ctrl+Shift+X`):

- `ms-python.python` — Python language support
- `ms-python.pylance` — Type checking and IntelliSense
- `ms-python.black-formatter` — Auto-formatting on save
- `usernamehw.errorlens` — Inline error display
- `eamodio.gitlens` — Git history and blame

**Option 2 — PyCharm Community Edition (Free)**

    yay -S pycharm-community-edition

**Option 3 — Neovim + LazyVim (Terminal native, blazing fast)**

    yay -S neovim
    # Follow https://lazyvim.org then add pyright + ruff via Mason

---

## ⚙️ First-Time Setup

    # 1. Install pyenv
    curl https://pyenv.run | bash

    # 2. Add to ~/.bashrc or ~/.zshrc
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

---

## 🔧 Git Workflow

    # Start a new exercise
    git checkout -b phase-01/ex02-variables

    # After finishing
    git add .
    git commit -m "feat(01-basics): ex02 variables and type casting complete"
    git push origin phase-01/ex02-variables

**Commit message convention:**

    feat(phase)      → new exercise or project added
    fix(phase)       → bug or logic correction
    docs(phase)      → README or notes updated
    refactor(phase)  → cleaner rewrite of existing code
    test(phase)      → test files added or updated

---

## 🧠 Learning Principles

1. **Theory before code** — understand the concept fully before writing a single line
2. **3–4 exercises per concept** — repetition builds genuine muscle memory
3. **No copy-paste** — type every exercise by hand to train fingers and brain together
4. **Project to validate** — only start the section project when exercises feel natural
5. **Git everything** — every exercise, even incomplete ones, gets committed
6. **Checkpoint before advancing** — answer checkpoint questions before the next phase

---

## 📈 Progress Tracker

| Phase | Topic                   | Status         | Project                  |
|-------|-------------------------|----------------|--------------------------|
| 00    | Setup & Environment     | ⬜ Not Started | —                        |
| 01    | Python Basics           | ⬜ Not Started | Tip Calculator           |
| 02    | Control Flow            | ⬜ Not Started | Number Guessing Game     |
| 03    | Functions               | ⬜ Not Started | Unit Converter           |
| 04    | Data Structures         | ⬜ Not Started | Student Grade Manager    |
| 05    | OOP                     | ⬜ Not Started | Bank Account System      |
| 06    | Modules & Packages      | ⬜ Not Started | File Organizer           |
| 07    | Advanced Python         | ⬜ Not Started | Async Data Pipeline      |
| 08    | Testing & Exceptions    | ⬜ Not Started | Tested Calculator        |
| 09    | Web & Data Capstone     | ⬜ Not Started | Personal Finance Tracker |

> Update ⬜ → 🟡 (In Progress) → ✅ (Complete) as you advance.

---

## 📖 Resources

| Resource               | URL                                      |
|------------------------|------------------------------------------|
| Official Python Docs   | https://docs.python.org/3/               |
| roadmap.sh/python      | https://roadmap.sh/python                |
| Real Python            | https://realpython.com                   |
| Python Cheatsheet      | https://www.pythoncheatsheet.org         |
| Exercism Python Track  | https://exercism.org/tracks/python       |
| PEP Index              | https://peps.python.org                  |

---

## 📝 License

This repository is for personal learning. All code is original unless attributed.

---

*Started: 2026 · Maintained by Ashish · CachyOS Linux*

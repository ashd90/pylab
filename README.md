# 🐍 PyLab — Python Mastery, the Right Way

> A structured, project-based curriculum built for beginners — blending deep theory
> with hands-on code. Based on roadmap.sh/python
> Tracked on GitHub · Practiced on CachyOS Linux.

---

## 📌 About This Repository

pylab is my personal Python learning lab. Every concept is studied in depth,
practiced through 8–10 focused exercises, and validated through a real-world
mini-project before moving on. No rushing. No skipping.

| Property       | Detail                                                        |
|----------------|---------------------------------------------------------------|
| Skill Level    | Absolute Beginner → Advanced                                  |
| OS             | CachyOS Linux (Arch-based)                                    |
| IDE            | VS Code / Neovim                                              |
| Python Version | 3.12+ (managed via pyenv)                                     |
| Reference      | roadmap.sh/python                                             |
| Methodology    | Theory → Exercises (8–10) → Project → Validate → Advance     |

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
    ├── README.md
    ├── .gitignore
    │
    ├── 00-setup/
    │   └── README.md
    │
    ├── 01-basics/
    │   ├── README.md                  ← phase index
    │   ├── c1-variables-data-types/
    │   │   ├── README.md              ← concept theory + exercises + checkpoint
    │   │   ├── ex01_variables.py
    │   │   ├── ex02_dynamic_typing.py
    │   │   ├── ex03_none_vs_zero.py
    │   │   └── ex04_big_numbers.py
    │   ├── c2-type-system-casting/
    │   │   ├── README.md
    │   │   ├── ex05_type_function.py
    │   │   ├── ex06_isinstance.py
    │   │   ├── ex07_implicit_conversion.py
    │   │   ├── ex08_explicit_casting.py
    │   │   ├── ex09_truthy_falsy.py
    │   │   ├── ex10_identity_equality.py
    │   │   ├── ex11_casting_input.py
    │   │   ├── ex12_type_in_fstrings.py
    │   │   └── ex13_type_system_mixed.py
    │   ├── c3-strings/
    │   ├── c4-operators/
    │   ├── c5-input-output/
    │   ├── c6-builtin-functions/
    │   └── project/
    │       └── tip_calculator.py
    │
    ├── 02-control-flow/            ← same concept subfolder pattern
    ├── 03-functions/
    ├── 04-data-structures/
    ├── 05-oop/
    ├── 06-modules-packages/
    ├── 07-advanced-python/
    ├── 08-testing-exceptions/
    └── 09-web-data-capstone/

---

## 📚 Section README Layout

Each phase has a top-level README (phase index) and one README per concept:

    Phase README      → concept list, status tracker, folder structure, project
    Concept README    → theory, language compare, key syntax, exercises,
                        FAQ, troubleshooting, checkpoint

---

## 💻 IDE Setup — CachyOS Linux

Option 1 — VS Code (Recommended)

    yay -S vscodium-bin

Extensions: ms-python.python, ms-python.pylance, ms-python.black-formatter,
            usernamehw.errorlens, eamodio.gitlens

Option 2 — PyCharm Community

    yay -S pycharm-community-edition

Option 3 — Neovim + LazyVim

    yay -S neovim

---

## ⚙️ First-Time Setup

    curl https://pyenv.run | bash

    export PYENV_ROOT="$HOME/.pyenv"
    [[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"

    source ~/.bashrc
    pyenv install 3.12.0
    pyenv global 3.12.0

    cd 01-basics
    python -m venv .venv
    source .venv/bin/activate

---

## 🔧 Git Workflow

    git checkout -b phase-01/c2-type-system-casting
    git add .
    git commit -m "feat(01-basics/c2): type system and casting — 9 exercises complete"
    git push origin phase-01/c2-type-system-casting

Commit conventions:
    feat   → new exercise or project
    fix    → bug correction
    docs   → README update
    refactor → cleaner rewrite

---

## 🧠 Learning Methodology

    1. Theory first        — real-world analogy + language comparison
    2. 8–10 exercises      — typed by hand, never copy-pasted
    3. Review after push   — consolidate before moving forward
    4. Validate            — checkpoint answered before next concept
    5. Project             — one real project per phase
    6. Git everything      — every exercise committed

---

## 📈 Progress Tracker

| Phase | Topic                | Status         | Project                  |
|-------|----------------------|----------------|--------------------------|
| 00    | Setup & Environment  | ✅ Complete    | —                        |
| 01    | Python Basics        | 🟡 In Progress | Tip Calculator           |
| 02    | Control Flow         | ⬜ Not Started | Number Guessing Game     |
| 03    | Functions            | ⬜ Not Started | Unit Converter           |
| 04    | Data Structures      | ⬜ Not Started | Student Grade Manager    |
| 05    | OOP                  | ⬜ Not Started | Bank Account System      |
| 06    | Modules & Packages   | ⬜ Not Started | File Organizer           |
| 07    | Advanced Python      | ⬜ Not Started | Async Data Pipeline      |
| 08    | Testing & Exceptions | ⬜ Not Started | Tested Calculator        |
| 09    | Web & Data Capstone  | ⬜ Not Started | Personal Finance Tracker |

---

## 📖 Resources

| Resource              | URL                                |
|-----------------------|------------------------------------|
| Official Python Docs  | https://docs.python.org/3/         |
| roadmap.sh/python     | https://roadmap.sh/python          |
| Real Python           | https://realpython.com             |
| Python Cheatsheet     | https://www.pythoncheatsheet.org   |
| Exercism Python Track | https://exercism.org/tracks/python |
| PEP Index             | https://peps.python.org            |

---

*Started: 2026 · Maintained by Ashish · CachyOS Linux*

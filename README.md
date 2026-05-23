# 🐍 PyLab — Python Mastery, the Right Way

> A structured, project-based curriculum built for beginners — blending deep theory
> with hands-on code. Based on [roadmap.sh/python](https://roadmap.sh/python)
> Tracked on GitHub · Practiced on CachyOS Linux.

---

## 📌 About This Repository

`pylab` is my personal Python learning lab. Every concept is studied in depth,
practiced through **8–10 focused exercises**, and validated through a **real-world
mini-project** before moving on. No rushing. No skipping.

| Property       | Detail                                                        |
|----------------|---------------------------------------------------------------|
| **Skill Level**    | Absolute Beginner → Advanced                              |
| **OS**             | CachyOS Linux (Arch-based)                                |
| **IDE**            | VS Code / Neovim                                          |
| **Python Version** | 3.12+ (managed via pyenv)                                |
| **Reference**      | roadmap.sh/python                                         |
| **Methodology**    | Theory → Exercises (8–10) → Project → Validate → Advance |

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
    ├── .gitignore                       ← covers all .venv, __pycache__, logs
    │
    ├── 00-setup/
    │   ├── README.md                    ← Setup theory, steps, troubleshooting
    │   └── notes.md
    │
    ├── 01-basics/
    │   ├── README.md                    ← Theory + FAQ + Production Q&A
    │   ├── .venv/                       ← gitignored, created locally
    │   ├── ex01_variables.py
    │   ├── ex02_dynamic_typing.py
    │   ├── ex03_none_vs_zero.py
    │   ├── ex04_big_numbers.py
    │   ├── ex05_type_casting.py
    │   ├── ex06_strings.py
    │   ├── ex07_operators.py
    │   ├── ex08_input_output.py
    │   ├── ex09_builtins.py
    │   ├── ex10_mixed_practice.py
    │   └── project/
    │       └── tip_calculator.py
    │
    ├── 02-control-flow/
    │   ├── README.md
    │   ├── .venv/
    │   ├── ex01_if_else.py
    │   ├── ex02_nested_conditions.py
    │   ├── ex03_match_case.py
    │   ├── ex04_for_loops.py
    │   ├── ex05_while_loops.py
    │   ├── ex06_break_continue.py
    │   ├── ex07_loop_else.py
    │   ├── ex08_nested_loops.py
    │   ├── ex09_ternary.py
    │   ├── ex10_mixed_practice.py
    │   └── project/
    │       └── number_guessing_game.py
    │
    ├── 03-functions/
    │   ├── README.md
    │   ├── .venv/
    │   ├── ex01_basic_functions.py
    │   ├── ex02_return_values.py
    │   ├── ex03_default_args.py
    │   ├── ex04_args_kwargs.py
    │   ├── ex05_scope_legb.py
    │   ├── ex06_lambda.py
    │   ├── ex07_closures.py
    │   ├── ex08_recursion.py
    │   ├── ex09_higher_order.py
    │   ├── ex10_mixed_practice.py
    │   └── project/
    │       └── unit_converter.py
    │
    ├── 04-data-structures/
    │   ├── README.md
    │   ├── .venv/
    │   ├── ex01_lists_basics.py
    │   ├── ex02_lists_methods.py
    │   ├── ex03_tuples.py
    │   ├── ex04_sets.py
    │   ├── ex05_dicts_basics.py
    │   ├── ex06_dicts_methods.py
    │   ├── ex07_list_comprehensions.py
    │   ├── ex08_dict_set_comprehensions.py
    │   ├── ex09_nested_structures.py
    │   ├── ex10_mixed_practice.py
    │   └── project/
    │       └── student_grade_manager.py
    │
    ├── 05-oop/
    │   ├── README.md
    │   ├── .venv/
    │   ├── ex01_classes_objects.py
    │   ├── ex02_instance_class_vars.py
    │   ├── ex03_methods.py
    │   ├── ex04_inheritance.py
    │   ├── ex05_super.py
    │   ├── ex06_dunder_methods.py
    │   ├── ex07_property.py
    │   ├── ex08_polymorphism.py
    │   ├── ex09_abstract_classes.py
    │   ├── ex10_mixed_practice.py
    │   └── project/
    │       └── bank_account_system.py
    │
    ├── 06-modules-packages/
    │   ├── README.md
    │   ├── .venv/
    │   ├── ex01_stdlib_os_path.py
    │   ├── ex02_stdlib_datetime.py
    │   ├── ex03_stdlib_math_random.py
    │   ├── ex04_json_csv.py
    │   ├── ex05_regex_intro.py
    │   ├── ex06_collections_module.py
    │   ├── ex07_functools_module.py
    │   ├── ex08_third_party_requests.py
    │   ├── ex09_custom_package/
    │   ├── ex10_mixed_practice.py
    │   └── project/
    │       └── file_organizer.py
    │
    ├── 07-advanced-python/
    │   ├── README.md
    │   ├── .venv/
    │   ├── ex01_decorators_basic.py
    │   ├── ex02_decorators_advanced.py
    │   ├── ex03_generators_basic.py
    │   ├── ex04_generators_advanced.py
    │   ├── ex05_context_managers.py
    │   ├── ex06_functional_programming.py
    │   ├── ex07_type_hints.py
    │   ├── ex08_dataclasses.py
    │   ├── ex09_async_await.py
    │   ├── ex10_mixed_practice.py
    │   └── project/
    │       └── data_pipeline.py
    │
    ├── 08-testing-exceptions/
    │   ├── README.md
    │   ├── .venv/
    │   ├── ex01_try_except.py
    │   ├── ex02_exception_hierarchy.py
    │   ├── ex03_custom_exceptions.py
    │   ├── ex04_exception_chaining.py
    │   ├── ex05_logging_basics.py
    │   ├── ex06_logging_advanced.py
    │   ├── ex07_pytest_basics.py
    │   ├── ex08_pytest_fixtures.py
    │   ├── ex09_pytest_mocking.py
    │   ├── ex10_tdd_practice.py
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

Every phase folder contains a README.md with this consistent structure:

    1. Brief Theory       → concept explained plainly with real-world analogies
    2. Language Compare   → how Python differs from C, Java, JavaScript on this topic
    3. Key Syntax         → patterns to memorize with inline comments
    4. Exercises          → 8–10 practice scripts, one concept at a time
    5. Project            → real-world mini-project applying everything in the phase
    6. FAQ                → common beginner confusions answered directly
    7. Real-World Q&A     → production-level scenarios and answers
    8. Troubleshooting    → common errors, causes, and fixes
    9. Checkpoint         → questions to validate mastery before advancing

---

## 💻 IDE Setup — CachyOS Linux

**Option 1 — VS Code (Recommended for beginners)**

Install via AUR:

    yay -S vscodium-bin              # open-source build (recommended)
    yay -S visual-studio-code-bin    # official Microsoft build

Essential extensions (Ctrl+Shift+X):

- ms-python.python        — Python language support
- ms-python.pylance       — type checking and IntelliSense
- ms-python.black-formatter — auto-format on save
- usernamehw.errorlens    — inline error display
- eamodio.gitlens         — git history and blame

**Option 2 — PyCharm Community Edition (Free)**

    yay -S pycharm-community-edition

**Option 3 — Neovim + LazyVim (terminal native)**

    yay -S neovim
    # Follow lazyvim.org then add pyright + ruff via Mason

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

    # 5. Create a virtual environment per phase (example for Phase 01)
    cd 01-basics
    python -m venv .venv
    source .venv/bin/activate

---

## 🔧 Git Workflow

    # Start a new exercise
    git checkout -b phase-01/concept-1-variables

    # After finishing all exercises in a concept
    git add .
    git commit -m "feat(01-basics): concept 1 — variables and data types (8 exercises)"
    git push origin phase-01/concept-1-variables

**Commit message convention:**

    feat(phase)      → new exercise or project added
    fix(phase)       → bug or logic correction
    docs(phase)      → README or notes updated
    refactor(phase)  → cleaner rewrite of existing code
    test(phase)      → test files added or updated

---

## 🧠 Learning Methodology

1. Theory first         — real-world analogy + language comparison before any code
2. 8–10 exercises       — one per concept variation, typed by hand, never copy-pasted
3. Review after push    — brief consolidation of what was learned before moving on
4. Validate before next — checkpoint questions answered correctly before advancing
5. Project at the end   — one real-world project per phase applying all concepts
6. Git everything       — every exercise committed, progress fully tracked on GitHub

---

## 📈 Progress Tracker

| Phase | Topic                | Exercises | Status         | Project                  |
|-------|----------------------|-----------|----------------|--------------------------|
| 00    | Setup & Environment  | —         | ✅ Complete    | —                        |
| 01    | Python Basics        | 8–10      | 🟡 In Progress | Tip Calculator           |
| 02    | Control Flow         | 8–10      | ⬜ Not Started | Number Guessing Game     |
| 03    | Functions            | 8–10      | ⬜ Not Started | Unit Converter           |
| 04    | Data Structures      | 8–10      | ⬜ Not Started | Student Grade Manager    |
| 05    | OOP                  | 8–10      | ⬜ Not Started | Bank Account System      |
| 06    | Modules & Packages   | 8–10      | ⬜ Not Started | File Organizer           |
| 07    | Advanced Python      | 8–10      | ⬜ Not Started | Async Data Pipeline      |
| 08    | Testing & Exceptions | 8–10      | ⬜ Not Started | Tested Calculator        |
| 09    | Web & Data Capstone  | 8–10      | ⬜ Not Started | Personal Finance Tracker |

> Update ⬜ → 🟡 (In Progress) → ✅ (Complete) as you advance.

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

## 📝 License

This repository is for personal learning. All code is original unless attributed.

---

*Started: 2026 · Maintained by Ashish · CachyOS Linux*

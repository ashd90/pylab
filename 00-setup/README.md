# Phase 00 — Environment Setup

## What This Phase Covers

Getting a clean, professional Python development environment running on CachyOS
Linux before writing a single line of real code.

---

## 1. Brief Theory

### How Python Runs Your Code

When you run `python hello.py`, three stages happen in sequence.

Stage 1 — CPython reads your .py file and compiles it into bytecode.
Stage 2 — That bytecode is saved into __pycache__/ so it does not need recompiling next time.
Stage 3 — The Python Virtual Machine (PVM) reads the bytecode and executes it.

Real-world analogy: your .py file is a recipe written in English. CPython is the
head chef who converts it into shorthand kitchen notes (bytecode). The PVM is the
kitchen assistant who follows those notes to produce the final dish (output).

### Why pyenv

Your CachyOS system ships with a Python installation that powers OS-level tools.
Think of it as the building's shared electricity supply. You never plug your own
appliances into it. pyenv installs a private power outlet in your room — your own
Python version that you fully control, with zero risk to the system.

pyenv manages Python VERSIONS (3.10, 3.11, 3.12 ...).

### Why venv

Even with pyenv giving you the right Python version, all your projects would still
share one global pool of packages. That causes version conflicts across projects.

venv creates an isolated box of packages per project. Project A gets its own
flask==2.0. Project B gets its own flask==3.0. They never meet.

venv manages PACKAGES for a single project.

### pyenv vs venv — the one-line distinction

    pyenv  →  which Python version am I using?
    venv   →  which packages does this project have?

### Why Git + GitHub

Git is version history for your code — every commit is a named snapshot you can
return to. GitHub is the cloud storage for those snapshots. Together they mean
you never lose work and your progress is visible and shareable.

---

## 2. Setup Steps

### Install pyenv dependencies

    sudo pacman -S --needed base-devel openssl zlib xz tk

### Install pyenv

    curl https://pyenv.run | bash

### Wire pyenv into your shell — add to ~/.bashrc

    export PYENV_ROOT="$HOME/.pyenv"
    [[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"

    source ~/.bashrc

### Install Python 3.12 and set as global default

    pyenv install 3.12.0
    pyenv global 3.12.0

### Verify

    python --version        # Python 3.12.0
    which python            # ~/.pyenv/shims/python  (NOT /usr/bin/python)

### Configure Git

    git config --global user.name "Your Name"
    git config --global user.email "your@email.com"
    git config --global init.defaultBranch main
    git config --global core.editor "code --wait"

### SSH key for GitHub

    ssh-keygen -t ed25519 -C "your@email.com"
    cat ~/.ssh/id_ed25519.pub   # copy → GitHub Settings → SSH Keys

    ssh -T git@github.com       # verify: Hi username! You've successfully authenticated.

### Create venv for Phase 01

    cd ~/repoHive/pylab/01-basics
    python -m venv .venv
    source .venv/bin/activate
    python --version            # confirms 3.12.0 inside venv

---

## 3. FAQ

Q: Should I use python or python3 in commands?
A: With pyenv configured, just use python. It always points to your pyenv version.

Q: My prompt does not show (.venv) after activation. What is wrong?
A: Run source .venv/bin/activate explicitly. Fish shell users use activate.fish instead.

Q: Can I use one venv for the whole pylab repo?
A: Yes, but one venv per phase mirrors real-world practice where each project has
   its own dependency set. That habit pays off later.

Q: What is __all__ in a Python file?
A: It controls which names are exported when someone does `from module import *`.
   You do not need it yet — it comes up in Phase 06 Modules.

---

## 4. Real-World Production Q&A

Q: Do production teams use venv directly?
A: Yes, or tools built on top of it — poetry (modern dependency management),
   uv (extremely fast, written in Rust by Astral). The isolation concept is identical.

Q: How are Python versions managed on production servers?
A: Docker images (FROM python:3.12-slim) handle the Python version on servers.
   pyenv is for developer machines. Both solve the same problem at different layers.

Q: What is requirements.txt and when do I use it?
A: It lists every package your project needs with exact versions.
   Generate it with: pip freeze > requirements.txt
   Recreate the environment anywhere with: pip install -r requirements.txt

---

## 5. Troubleshooting

    pyenv: command not found
    → pyenv lines not in ~/.bashrc. Add them and run: source ~/.bashrc

    python --version shows system Python
    → Run: pyenv rehash   then check: which python

    Permission denied pushing to GitHub
    → SSH key not added. Run: cat ~/.ssh/id_ed25519.pub and add to GitHub

    VS Code not finding Python interpreter
    → Ctrl+Shift+P → Python: Select Interpreter → choose .venv path

---

## 6. Checkpoint — Passed

    [x] CPython compiles .py to bytecode — PVM executes bytecode
    [x] __pycache__ is auto-generated cache — never commit it
    [x] pyenv manages Python versions
    [x] venv manages isolated package environments per project
    [x] Terminal confirms: Python 3.12.0 running from inside .venv

Phase 00 complete → Phase 01: Python Basics

# Phase 01 — Python Basics

> Covers the absolute building blocks of Python. Each concept lives in its own
> subfolder with dedicated theory, exercises, and a checkpoint.

---

## Concepts

    c1-variables-data-types/    Variables, 5 core types, dynamic typing
    c2-type-system-casting/     type(), isinstance(), casting, truthy/falsy, is vs ==
    c3-strings/                 Indexing, slicing, methods, f-strings, immutability
    c4-operators/               Arithmetic, comparison, logical, bitwise, precedence
    c5-input-output/            print(), input(), formatting, sys.argv intro
    c6-builtin-functions/       len(), range(), abs(), round(), sorted(), enumerate()

---

## Status

    c1-variables-data-types    ✅ Complete   4 exercises
    c2-type-system-casting     ✅ Complete   9 exercises
    c3-strings                 ⬜ Upcoming
    c4-operators               ⬜ Upcoming
    c5-input-output            ⬜ Upcoming
    c6-builtin-functions       ⬜ Upcoming

---

## Project — Tip Calculator & Bill Splitter

File: project/tip_calculator.py

Takes bill amount, tip percentage, and number of people via input(). Calculates
tip amount, total bill, and per-person share. Displays a formatted breakdown.

Concepts applied: input(), float(), round(), f-strings, arithmetic operators,
print() alignment.

---

## Folder Structure

    01-basics/
    ├── README.md                     ← this file
    ├── .venv/                        ← gitignored
    ├── c1-variables-data-types/
    │   ├── README.md
    │   ├── ex01_variables.py
    │   ├── ex02_dynamic_typing.py
    │   ├── ex03_none_vs_zero.py
    │   └── ex04_big_numbers.py
    ├── c2-type-system-casting/
    │   ├── README.md
    │   ├── ex05_type_function.py
    │   ├── ex06_isinstance.py
    │   ├── ex07_implicit_conversion.py
    │   ├── ex08_explicit_casting.py
    │   ├── ex09_truthy_falsy.py
    │   ├── ex10_identity_equality.py
    │   ├── ex11_casting_input.py
    │   ├── ex12_type_in_fstrings.py
    │   └── ex13_type_system_mixed.py
    ├── c3-strings/
    │   └── README.md
    ├── c4-operators/
    │   └── README.md
    ├── c5-input-output/
    │   └── README.md
    ├── c6-builtin-functions/
    │   └── README.md
    └── project/
        └── tip_calculator.py

---

## Checkpoint Summary

Before moving to Phase 02 all checkpoints in c1 through c6 must be answered
and all project exercises must be complete and committed.

Phase 01 complete → Phase 02: Control Flow

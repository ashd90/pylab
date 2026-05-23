# Phase 01 — Python Basics

> Building blocks of Python — data types, type system, strings, operators,
> input/output, and built-in functions. 8–10 exercises per concept.

---

## Concepts Covered

    Concept 1 — Variables & Data Types
    Concept 2 — Type System & Casting
    Concept 3 — Strings          (upcoming)
    Concept 4 — Operators        (upcoming)
    Concept 5 — Input & Output   (upcoming)
    Concept 6 — Built-in Functions (upcoming)

---

## 1. Variables & Data Types

A variable is a named label pointing to a value in memory. Python tracks the
type internally — you never declare it. The label can be reassigned to any
type at any time (dynamic typing).

**Five core types:**

    int    → whole numbers, unlimited size, no overflow (unlike C/Java)
    float  → decimal numbers, IEEE 754 double precision
    str    → immutable sequence of unicode characters, no separate char type
    bool   → exactly True or False (capital letters required)
    None   → deliberate absence of a value — not 0, not False, not ""

**Dynamic typing:** type is determined at assignment, checked at runtime.
Trade-off: fast prototyping, but type errors only surface when code runs.

**Language comparison:**

    C/Java integers overflow at 2^31 - 1. Python integers never overflow.
    JavaScript has null AND undefined. Python has only None.
    Java/JS booleans are lowercase (true/false). Python capitalises (True/False).
    C has no string type — just char arrays. Python str is a first-class object.

**Exercises:**

    ex01_variables.py        → declare all 5 types, print value + type()
    ex02_dynamic_typing.py   → reassign one variable through all types
    ex03_none_vs_zero.py     → prove None != 0 != False != ""
    ex04_big_numbers.py      → unlimited int, underscore notation, 10**100

---

## 2. Type System & Casting

**type()** returns the exact type object of a value. Used for exact matching.

**isinstance()** checks if a value belongs to a type or any of its parent types.
Preferred in production because it respects inheritance.

    type(True) == int        → False  (exact check — True is bool, not int)
    isinstance(True, int)    → True   (bool is a subclass of int)

**Implicit conversion:** Python silently promotes int → float when needed.
Never loses data — always promotes to the more precise type.

    10 + 3.5  → 13.5 (float)   Python promoted int to float automatically.

**Explicit casting — valid conversions:**

    int("42")              → 42
    int(float("3.14"))     → 3      two-step: str→float→int
    float("3.14")          → 3.14
    str(100)               → "100"
    bool(0)                → False
    bool(" ")              → True   space is NOT empty — only "" is falsy

**Falsy values — the complete list at this stage:**

    0, 0.0, "", None

**Everything else is truthy** — including " " (space), "0", -1, 0.1.

**== vs is:**

    ==   checks value equality   — do both sides hold the same value?
    is   checks object identity  — do both sides point to the same object in memory?

Use is only for None checks. Use == for everything else.

    result is None      ✅ correct
    result == None      ⚠️  works but PEP 8 violation

**int() truncates, does not round:**

    int(9.9)  → 9     (decimal dropped, not rounded)
    int(9.1)  → 9

**Language comparison:**

    JavaScript  "5" + 3 → "53"   silent coercion, surprising result
    Python      "5" + 3 → TypeError, forces you to be explicit
    Java cast syntax: (int) 3.14   Python cast syntax: int(3.14)

**Exercises:**

    ex05_type_function.py       → type() on every data type, direct comparison
    ex06_isinstance.py          → isinstance() vs type(), bool/int gotcha
    ex07_implicit_conversion.py → int+float promotion, bool arithmetic
    ex08_explicit_casting.py    → all valid casts, int() truncation behaviour
    ex09_truthy_falsy.py        → map every falsy value, space vs empty string
    ex10_identity_equality.py   → is vs ==, id(), CPython integer caching
    ex11_casting_input.py       → cast live user input, use in calculation
    ex12_type_in_fstrings.py    → format int/float/bool/None in f-strings
    ex13_type_system_mixed.py   → combined practice, all concept 2 topics

---

## 3. Strings (upcoming)

---

## 4. Operators (upcoming)

---

## 5. Input & Output (upcoming)

---

## 6. Built-in Functions (upcoming)

---

## Project — Tip Calculator & Bill Splitter

**File:** project/tip_calculator.py

Takes bill amount, tip %, and number of people via input(). Calculates tip,
total, and per-person share. Formatted output using f-strings.

Concepts applied: input(), float(), round(), f-strings, arithmetic operators.

---

## FAQ

**Q: Why does 0.1 + 0.2 not equal 0.3?**
Floats are stored in binary. 0.1 has no exact binary representation — a tiny
rounding error accumulates. Use round() for display. Use the decimal module
for financial calculations that require exact precision.

**Q: bool(" ") — True or False?**
True. Only "" (zero characters) is falsy. A space has one character — truthy.

**Q: int() vs round() — what is the difference?**
int(9.9) → 9 (truncates, drops decimal). round(9.9) → 10 (rounds to nearest).

**Q: When to use is vs ==?**
Use is only for None: if x is None. Use == for all value comparisons.

**Q: isinstance() vs type() — which to prefer?**
isinstance() in almost all cases. It respects inheritance. type() is for the
rare case you need an exact type match with no subclasses accepted.

---

## Real-World Notes

- Arbitrary precision int is used in cryptography (RSA key generation).
- None is returned by database queries when no record is found.
- f-strings are fastest at runtime — prefer over .format() and % formatting.
- Type hints + mypy (Phase 07) give Python static-typing benefits optionally.

---

## Troubleshooting

    ValueError: invalid literal for int()
    → Passed a non-numeric string. Go via float() first if it has a decimal.

    TypeError: can only concatenate str (not "int") to str
    → Use f-string or wrap the number in str().

    NameError: name 'x' is not defined
    → Variable used before assignment. Check spelling and order.

---

## Checkpoint Questions

    Concept 1:
    [ ] What are the 5 core types and one key trait of each?
    [ ] Why does Python never have integer overflow?
    [ ] What is dynamic typing and what is the trade-off?

    Concept 2:
    [ ] isinstance() vs type() — difference and which to prefer?
    [ ] What are all the falsy values covered so far?
    [ ] int(9.9) → ? Does it round or truncate?
    [ ] == checks ___ equality. is checks ___ equality.
    [ ] Why does int("3.14") fail but int(float("3.14")) work?

Phase 01 complete → Phase 02: Control Flow

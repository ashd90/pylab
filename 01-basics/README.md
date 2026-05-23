# Phase 01 — Python Basics

> Covers the absolute building blocks of Python — how data is stored, named,
> typed, manipulated, and displayed. Every concept is practiced through 8–10
> exercises before moving to the project.

---

## 1. Brief Theory

### Variables

A variable is a named label pointing to a value stored in memory. Python does
not require you to declare a type — you simply assign a value and Python tracks
the type internally. The label can be reassigned to any type at any time.

Real-world analogy: RAM is a warehouse with millions of shelves. A variable is
a sticky label you attach to one shelf. The label has a name, the shelf holds
the value. You can peel the label off and stick it on a different shelf any time.

### Core Data Types

**int** — whole numbers of unlimited size. No overflow unlike C or Java.
**float** — decimal numbers using IEEE 754 double precision (64-bit).
**str** — immutable sequence of unicode characters. No char type in Python.
**bool** — exactly two values: True or False (capital letters mandatory).
**None** — represents the deliberate absence of a value. Not zero, not False.

### Dynamic Typing

Python determines the type of a variable from the value assigned, not from a
declaration. Types are checked at runtime, not at compile time. This is called
dynamic typing. The upside is fast prototyping. The downside is that type errors
only surface when code actually runs — which is why we add type hints in Phase 07.

### Type Casting

Converting a value from one type to another explicitly using built-in functions:
int(), float(), str(), bool(). Some conversions are safe (int to float), others
can raise exceptions if the value is incompatible ("hello" cannot become an int).

### Strings

Strings are immutable sequences of unicode characters. Immutable means once
created, the string object cannot be changed — operations like .upper() return
a new string, they do not modify the original. Python 3 is unicode by default,
meaning it handles every human language out of the box.

### Operators

Python operators follow standard mathematical precedence (PEMDAS). The // operator
does floor division (discards decimal). The ** operator is exponentiation. The %
operator returns the remainder (modulo). Comparison operators return bool values.
Logical operators (and, or, not) use short-circuit evaluation.

### Input and Output

print() sends output to stdout. It accepts multiple arguments separated by commas,
a sep parameter to control what goes between them, and an end parameter to control
the line ending. input() reads from stdin and always returns a string — you must
cast it explicitly if you need a number.

### Built-in Functions

Python ships with ~70 built-in functions available without any import. The most
commonly used ones in this phase: len(), type(), range(), abs(), round(), min(),
max(), sum(), sorted(), enumerate(), zip().

---

## 2. Language Comparison

### Integers

    Language   | Integer limit           | Overflow
    -----------|-------------------------|------------------
    C (int)    | -2^31 to 2^31 - 1      | Yes, wraps silently
    Java (int) | -2^31 to 2^31 - 1      | Yes, wraps silently
    JavaScript | -(2^53-1) to 2^53-1    | Loses precision
    Python int | Unlimited               | Never

### Strings

    Language    | String type     | Unicode default | Mutable
    ------------|-----------------|-----------------|--------
    C           | char[] array    | No              | Yes
    Java        | String class    | Yes             | No
    JavaScript  | string          | Yes             | No
    Python 3    | str class       | Yes             | No

### Typing System

    Language     | Typing   | Type errors caught
    -------------|----------|----------------------
    C / Java     | Static   | At compile time
    JavaScript   | Dynamic  | At runtime
    Python       | Dynamic  | At runtime
    Python+mypy  | Optional | Before runtime via tooling

### Boolean

    Language    | Bool values       | Case
    ------------|-------------------|------------
    C           | No bool, uses 0/1 | —
    Java        | true / false      | lowercase
    JavaScript  | true / false      | lowercase
    Python      | True / False      | Capitalized

### Null / None

    Language    | Null value  | Common error
    ------------|-------------|----------------------------------
    Java        | null        | NullPointerException
    JavaScript  | null / undefined (two different things)
    C#          | null        | NullReferenceException
    Python      | None        | AttributeError (clear message)

---

## 3. Key Syntax

    # Variable assignment
    name = "Ashish"
    age = 28
    height = 5.9
    is_active = True
    result = None

    # Checking type
    type(name)           # <class 'str'>
    isinstance(age, int) # True

    # Type casting
    int("42")            # 42
    float("3.14")        # 3.14
    str(100)             # "100"
    bool(0)              # False
    bool("hello")        # True

    # String formatting (f-string — preferred)
    print(f"Hello, {name}. You are {age} years old.")

    # Operators
    10 // 3              # 3  (floor division)
    10 % 3               # 1  (remainder)
    2 ** 8               # 256 (exponentiation)

    # Input (always returns str)
    age = int(input("Enter your age: "))

    # Useful builtins
    len("hello")         # 5
    abs(-42)             # 42
    round(3.7)           # 4
    max(1, 5, 3)         # 5

---

## 4. Exercises

    ex01_variables.py        → declare all 5 types, print value + type
    ex02_dynamic_typing.py   → reassign one variable through all types
    ex03_none_vs_zero.py     → prove None != 0 != False != ""
    ex04_big_numbers.py      → unlimited int size, underscore notation
    ex05_type_casting.py     → safe and unsafe casting, handle ValueError
    ex06_strings_basics.py   → indexing, slicing, immutability proof
    ex07_string_methods.py   → upper, lower, strip, split, join, replace, find
    ex08_fstrings.py         → f-string formatting, alignment, precision
    ex09_operators.py        → all operator types, precedence, short-circuit
    ex10_input_output.py     → input(), cast to int/float, formatted output

---

## 5. Project — Tip Calculator & Bill Splitter

**File:** project/tip_calculator.py

**What it does:**
A CLI app that takes the bill amount, tip percentage, and number of people
via input(). It calculates the tip amount, total bill, and per-person share.
Displays a clean formatted breakdown. Handles invalid input gracefully.

**Concepts applied:**
input(), int(), float(), round(), f-strings, arithmetic operators, print()
formatting with sep and alignment.

**Sample run:**

    Enter bill amount (₹): 1200
    Enter tip percentage: 18
    Enter number of people: 4

    ----------------------------------------
    Bill Amount   :  ₹ 1200.00
    Tip (18%)     :  ₹  216.00
    Total Bill    :  ₹ 1416.00
    Per Person    :  ₹  354.00
    ----------------------------------------

---

## 6. FAQ

Q: Why does 0.1 + 0.2 not equal 0.3 in Python?
A: Floats are stored in binary (base-2). Just like 1/3 cannot be written exactly
   in decimal (0.333...), 0.1 cannot be written exactly in binary. The result is
   a tiny rounding error. Use round() for display, or the decimal module when
   exact precision matters (e.g. financial calculations).

Q: Should I use single quotes or double quotes for strings?
A: Python accepts both and they are identical. Pick one and be consistent.
   The community convention (PEP 8) has no preference. Double quotes are common
   because they allow apostrophes inside without escaping: "it's fine".

Q: Is True equal to 1 and False equal to 0?
A: Yes. bool is a subclass of int in Python. True == 1 and False == 0 evaluate
   to True. This means True + True == 2. It is rarely useful but good to know.

Q: What happens if I call int() on a float string like "3.14"?
A: It raises ValueError. You must go through float first: int(float("3.14")) → 3.

Q: Why does input() always return a string?
A: Because Python cannot know in advance whether the user will type a number,
   a name, or a sentence. It plays it safe and gives you the raw text. You decide
   what to do with it.

---

## 7. Real-World Production Q&A

Q: Are Python's unlimited integers actually used in production?
A: Yes. Cryptography libraries (like Python's cryptography package) use them
   constantly. RSA encryption involves modular exponentiation with numbers that
   are hundreds of digits long. This is impossible in C without special libraries.

Q: When would a production codebase use None?
A: Constantly. Functions that query a database return the result or None if not
   found. Optional function parameters default to None. Config values that have
   not been set yet are None. Checking `if result is None` is standard Python.

Q: Why use f-strings over .format() or % formatting?
A: f-strings (introduced in Python 3.6) are the fastest at runtime, the most
   readable, and the least error-prone. .format() is used when the template is
   stored separately from the values. % formatting is legacy — avoid it in new code.

Q: Why does Python use duck typing instead of strict type enforcement?
A: Python's philosophy (PEP 20) values practicality. If an object behaves like
   a duck (has the methods you need), it is a duck — you do not need to verify
   its class. This makes code more flexible and reusable. Type hints + mypy give
   you safety when you need it, without making the language rigid by default.

---

## 8. Troubleshooting

    ValueError: invalid literal for int() with base 10: 'hello'
    → You passed a non-numeric string to int(). Wrap in try/except or validate first.

    NameError: name 'x' is not defined
    → You used a variable before assigning it. Check spelling and assignment order.

    TypeError: can only concatenate str (not "int") to str
    → You tried to join a string and a number with +. Use f-strings or str(number).

    SyntaxError: invalid syntax on a print line
    → Often a missing closing parenthesis or mismatched quotes from a line above.

    IndentationError: unexpected indent
    → Python uses indentation as syntax. Do not indent lines that are not inside
      a block. Use 4 spaces consistently — never mix tabs and spaces.

---

## 9. Checkpoint

Answer these before moving to Phase 02.

    [ ] What are the 3 stages Python goes through to run a .py file?
    [ ] What is the difference between int and float? When would you use each?
    [ ] Why is None not the same as 0 or False?
    [ ] What does dynamic typing mean? What is the trade-off vs static typing?
    [ ] A user types "25" into input(). How do you use it as a number?
    [ ] What does 17 // 5 return? What does 17 % 5 return?
    [ ] Why are strings immutable? What does .upper() actually return?
    [ ] What is short-circuit evaluation in and / or?

Phase 01 complete → Phase 02: Control Flow

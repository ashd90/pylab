# Concept 1 — Variables & Data Types

---

## Theory

A variable is a named label pointing to a value stored in memory. Python
determines the type from the assigned value — you never declare it explicitly.
The same label can be reassigned to a completely different type at any time.
This is called dynamic typing.

Real-world analogy: RAM is a warehouse with millions of shelves. A variable is
a sticky label on one shelf. The label holds the name, the shelf holds the value.
Peel the label off and stick it elsewhere — Python handles cleanup automatically.

### The Five Core Types

int — whole numbers with no size limit. No overflow ever, unlike C or Java.
      Underscores allowed for readability: 1_000_000 is the same as 1000000.

float — decimal numbers stored in IEEE 754 double precision (64 bits).
        Capable of representing very large and very small decimals, but with
        minor rounding limitations in binary representation.

str — an immutable, ordered sequence of unicode characters. Python 3 handles
      every human language out of the box. There is no separate char type —
      a single character is just a str of length 1.

bool — exactly two values: True or False. Capital letters are mandatory.
       bool is a subclass of int — True equals 1 and False equals 0 numerically.

None — the deliberate absence of a value. Not zero, not False, not empty string.
       It is a real object of type NoneType. There is exactly one None object
       in all of Python — every variable assigned None points to the same object.

### Dynamic Typing

Python checks types at runtime, not at compile time. The benefit is rapid
prototyping — no declarations, no ceremony. The trade-off is that type errors
only surface when the specific line of code actually executes. Type hints
(Phase 07) restore safety without sacrificing flexibility.

---

## Language Comparison

    Feature            Python              C/Java              JavaScript
    -------------------|--------------------|--------------------|--------------------
    Integer limit      | Unlimited          | -2^31 to 2^31-1    | -(2^53-1) to 2^53-1
    Integer overflow   | Never              | Wraps silently      | Loses precision
    String type        | str (first-class)  | char[] / String     | string
    Unicode default    | Yes (Python 3)     | Java yes, C no      | Yes
    Bool values        | True / False       | true / false        | true / false
    Null value         | None               | null                | null and undefined
    Typing             | Dynamic            | Static              | Dynamic

---

## Key Syntax

    # Assignment
    name     = "Ashish"      # str
    age      = 28            # int
    height   = 5.9           # float
    active   = True          # bool
    manager  = None          # NoneType

    # Check type
    type(age)                # <class 'int'>
    type(age) == int         # True

    # Underscores in large numbers
    population = 1_400_000_000

    # Exponentiation
    googol = 10 ** 100       # works perfectly — no overflow

    # Print value and type together
    print(name, type(name))

---

## Exercises

    ex01_variables.py       Declare all 5 types, print each value and type()
    ex02_dynamic_typing.py  Reassign one variable through all 5 types, observe
    ex03_none_vs_zero.py    Prove None != 0 != False != "" with comparisons
    ex04_big_numbers.py     Unlimited int size, underscore notation, 10**100

---

## FAQ

Q: Can I name a variable anything?
A: Almost. Names must start with a letter or underscore, not a digit. They are
   case-sensitive (age and Age are different). Avoid Python keywords like if,
   for, class, None, True, False — they are reserved.

Q: Is True equal to 1?
A: Numerically yes — True == 1 and False == 0 evaluate to True. bool is a
   subclass of int. This means True + True returns 2. Rarely useful, but good
   to know.

Q: Why is Python's int unlimited but float is not?
A: int is stored as a variable-length object in memory — it grows as needed.
   float uses a fixed 64-bit IEEE 754 representation, which gives a maximum
   value of about 1.8 × 10^308 but with limited decimal precision.

---

## Troubleshooting

    NameError: name 'x' is not defined
    Variable used before assignment, or spelling mismatch. Check case.

    SyntaxError near a variable name
    You likely used a Python keyword as a variable name (e.g. None = 5).

---

## Checkpoint

    [ ] Name all 5 core types and one key characteristic of each.
    [ ] What is dynamic typing? What is the trade-off vs static typing?
    [ ] Why does Python never have integer overflow?
    [ ] What is None? How is it different from 0, False, and ""?
    [ ] What does type(True) return? What does type(True) == int return and why?

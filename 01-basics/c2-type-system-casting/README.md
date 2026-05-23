# Concept 2 — Type System & Casting

---

## Theory

### type() vs isinstance()

type() returns the exact type object of a value. isinstance() checks whether
a value belongs to a type or any of its parent types in the inheritance chain.

isinstance() is preferred in production because it respects class inheritance.
bool is a subclass of int, so isinstance(True, int) returns True — which is
correct because True genuinely is an integer internally.

    type(True) == int        False  — exact check only, True is bool not int
    type(True) == bool       True
    isinstance(True, int)    True   — bool inherits from int
    isinstance(True, bool)   True

### Implicit Conversion

Python silently promotes types when combining them in operations, but only
when the conversion is safe and lossless. It always promotes toward the
more precise type — int becomes float, never the other way around.

    10 + 3.5    →   13.5   (float)   int promoted to float automatically
    True + 1    →   2      (int)     bool promoted to int automatically

Python never implicitly converts in a way that loses data or surprises you.

### Explicit Casting

You manually convert using built-in functions. The conversion must make sense
or Python raises an exception.

    int("42")            →  42         str to int, works
    int("3.14")          →  ValueError  decimal in string, int() refuses
    int(float("3.14"))   →  3          two-step: str→float→int, works
    float("3.14")        →  3.14
    str(100)             →  "100"
    bool(0)              →  False
    bool(" ")            →  True       space is not empty — one character exists

int() always truncates toward zero. It does not round.
    int(9.9)  →  9      int(9.1)  →  9      int(-9.9)  →  -9

### Truthy and Falsy Values

Every Python value has an implicit boolean meaning used in conditions (Phase 02).

Falsy — evaluates to False when converted to bool:
    0       0.0      ""      None

Truthy — everything else:
    Any non-zero number, any non-empty string (including " "), any object.

The rule for strings: only "" (zero characters) is falsy. One character minimum
makes it truthy — even a space, even "0", even "False" as a string.

### == vs is (Value vs Identity)

== checks value equality — do both sides hold the same value?
is checks object identity — do both sides point to the exact same object
in memory (same id())?

Two variables can hold equal values but be separate objects:
    a = 1000
    b = 1000
    a == b     True   — same value
    a is b     False  — two separate objects in memory

None is special — there is exactly one None object in Python. Every variable
assigned None points to the same object:
    x is None  always correct — use is for None checks, never ==

CPython caches small integers (-5 to 256) and short strings as an optimization.
This means is may return True for small integers even when you expect False.
Never rely on is for value comparisons — use it only for None.

---

## Language Comparison

    Feature                 Python              Java            JavaScript
    ------------------------|--------------------|---------       ---------------------
    Type check              | isinstance()       | instanceof     | typeof / instanceof
    Cast syntax             | int(x)             | (int) x        | Number(x), parseInt()
    Implicit str+int        | TypeError          | Compile error  | "53" — silent coercion
    Null check              | x is None          | x == null      | x === null
    Truthy/falsy            | Defined clearly    | Only bool      | Many surprises ([] is truthy, "" is falsy)

JavaScript implicit coercion is a famous source of bugs. Python forces you to
be explicit — the same operation that silently gives "53" in JS raises a clear
TypeError in Python.

---

## Key Syntax

    # Type checking
    type(x)                      # exact type object
    type(x) == int               # exact type match
    isinstance(x, int)           # type or subclass match — preferred

    # Casting
    int("42")                    # 42
    int(float("3.14"))           # 3  — two-step for decimal strings
    float("3.14")                # 3.14
    str(100)                     # "100"
    bool(0)                      # False
    bool("")                     # False
    bool(" ")                    # True

    # Truthy/falsy
    bool(0)      bool(0.0)       bool("")     bool(None)    # all False
    bool(1)      bool(3.14)      bool(" ")    bool("hi")    # all True

    # None check
    result is None               # correct
    result is not None           # correct negation

    # Identity vs equality
    a == b                       # value comparison
    a is b                       # identity comparison — same object?
    id(a)                        # memory address of object a

---

## Exercises

    ex05_type_function.py        type() on every data type, direct comparison
    ex06_isinstance.py           isinstance() vs type(), bool/int inheritance
    ex07_implicit_conversion.py  int+float promotion, bool arithmetic
    ex08_explicit_casting.py     all valid casts, int() truncation behaviour
    ex09_truthy_falsy.py         all falsy values, space vs empty string
    ex10_identity_equality.py    is vs ==, id(), CPython integer caching
    ex11_casting_input.py        cast live user input, use in calculation
    ex12_type_in_fstrings.py     format types in f-strings with precision
    ex13_type_system_mixed.py    combined practice across all concept 2 topics

---

## FAQ

Q: Why does int("3.14") fail but int(float("3.14")) work?
A: int() expects a clean integer string with no decimal point. "3.14" has one,
   so it refuses. Going via float() first converts the string to a float object
   3.14, and int() can truncate a float cleanly to 3.

Q: bool(" ") — True or False?
A: True. A space is a character. Only "" (zero characters) is falsy.

Q: Should I ever use type() instead of isinstance()?
A: Rarely. Only when you explicitly want to reject subclasses — for example,
   rejecting bool when you only want a pure int. In most cases isinstance() is
   the right tool.

Q: Why does is return True for small integers?
A: CPython caches integers from -5 to 256 as a memory optimization — only one
   object is ever created for each of those values. So x = 5; y = 5; x is y
   returns True because both labels point to the same cached object. This is
   an implementation detail, not something to rely on in code.

---

## Troubleshooting

    ValueError: invalid literal for int() with base 10: '3.14'
    The string has a decimal point. Use int(float("3.14")) instead.

    TypeError: int() argument must be a string or number, not 'NoneType'
    Cannot cast None to int. Check that the value is not None before casting.

    Unexpected True from isinstance()
    Remember bool is a subclass of int. isinstance(True, int) is True by design.

---

## Checkpoint

    [ ] isinstance() vs type() — which to prefer and why?
    [ ] What are all the falsy values at this stage of learning?
    [ ] int(9.9) returns what? Does it round or truncate?
    [ ] == checks ___ equality. is checks ___ equality.
    [ ] Why does int("3.14") fail but int(float("3.14")) work?
    [ ] bool(" ") returns True or False? Why?

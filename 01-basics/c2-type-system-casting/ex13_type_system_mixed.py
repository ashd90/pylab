# Goal: mixed practice — type checking, casting, truthy/falsy, identity


# --- Part A: Type identification ---
values = 42, 3.14, "Python", True, None, 0, "", 10 ** 30

# Print each value with its type (write each print manually)
print(42, type(42))
print(3.14, type(3.14))
print("Python", type("Python"))
print(True, type(True))
print(None, type(None))
print("", type(""))
print(10 ** 30, type(10 ** 30))

# --- Part B: Truthiness check ---
print(bool(42))
print(bool(3.14))
print(bool("Python"))
print(bool(True))
print(bool(0))
print(bool(""))
print(bool(10 ** 30))

# --- Part C: isinstance chain ---
print(isinstance(True, bool))
print(isinstance(True, int))
print(isinstance(3.14, float))
print(isinstance(3.14, int))
print(isinstance("hello", str))
print(isinstance(None, type(None)))

# --- Part D: Safe casting chain ---
raw_int = "256"
raw_float = "3.99"
raw_bool = 0

print(int(raw_int))
print(float(raw_float))
print(int(float(raw_float)))
print(bool(raw_bool))
print(str(int(raw_int) + 100))
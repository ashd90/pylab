# Goal: know exactly which values are falsy in Python

# All falsy values
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool(None))

# All truthy — any non-zero, non-empty value
print(bool(1))
print(bool(-1))
print(bool(3.14))
print(bool("a"))
print(bool(" "))

# Comparison of falsy values to each other
print(0 == False)
print("" == False)
print(None == False)
print(None == 0)

# Correct None check
x = None
print(x is None)
print(x is not None)
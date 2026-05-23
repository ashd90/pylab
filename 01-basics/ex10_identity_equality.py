# Goal: understand the difference between value equality and object identity

# Value equality vs identity with large integers
a = 1000
b = 1000
print(a == b)
print(a is b)

# Small integers are cached by CPython (-5 to 256)
x = 5
y = 5
print(x == y)
print(x is y)

# None — only one object ever exists
n1 = None
n2 = None
print(n1 == n2)
print(n1 is n2)

# Bool identity
print(True is True)
print(False is False)

# id() — see the actual memory address
val1 = "hello"
val2 = "hello"
print(id(val1))
print(id(val2))
print(val1 is val2)
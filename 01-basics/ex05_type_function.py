# Goal: understand what type() returns and how to compare types

# ex05_type_function.py
# Goal: use type() on every data type and compare results

name = "Ashish"
age =  28
height = 5.9
is_active = True
nothing = None
big = 10 ** 50

print(type(name))
print(type(age))
print(type(height))
print(type(is_active))
print(type(nothing))
print(type(big))

# Compare type() result directly
print(type(age) == int)
print(type(age) == str)
print(type(height) == float)
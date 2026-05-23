# Goal: understand isinstance() and the bool/int inheritance gotcha

x = True

print(type(x))
print(type(x) == bool)
print(type(x) == int)

print(isinstance(x, bool))
print(isinstance(x, int))

# None Check

result = None

print(type(result))
print(isinstance(result,type(None)))
print(result is None)
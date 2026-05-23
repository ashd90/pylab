# Goal: observe implicit int → float promotion

a = 10
b = 3.5

result = a+b
print(result)
print(type(result))

result2 =  a*b
print(result2)
print(type(result2))

# bool behaves as int in arithmetic
print(True + True)
print(True + 1)
print(False + 10)
print(type(True + 1))
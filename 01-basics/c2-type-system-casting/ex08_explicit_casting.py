# Goal: practice int(), float(), str(), bool() casting

# str → int and float

print(int("42"))
print(float("3.14"))
print(int(float("3.14")))

# number → str
print(str(100))
print(str(3.14))
print(str(True))

# number → bool
print(bool(0))
print(bool(1))
print(bool(-99))
print(bool(0.0))
print(bool(0.1))

# str → bool
print(bool(""))
print(bool("hello"))
print(bool(" "))

# int ↔ float
print(int(9.9))
print(int(9.1))
print(float(5))
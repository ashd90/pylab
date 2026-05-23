# Goal: format int, float, bool, None cleanly in f-strings

name = "Ashish"
age = 28
salary = 75000.5
score = 98.6789
active = True
manager = None

# Basic f-string
print(f"Name: {name}")
print(f"Age : {age}")

# Float precision — :.2f means 2 decimal places
print(f"Salary: {salary:.2f}")
print(f"Score : {score:.2f}")

# Width alignment — :>10 means right-align in 10 chars
print(f"{'Field':<12} {'Value':>10}")
print(f"{'Name':<12} {name:>10}")
print(f"{'Age':<12} {age:>10}")
print(f"{'Salary':<12} {salary:>10.2f}")

# Bool and None in f-strings
print(f"Active : {active}")
print(f"Manager: {manager}")

# Casting inside f-string
pi = 3.14159265
print(f"Pi as int : {int(pi)}")
print(f"Pi 4dp : {pi:.4f}")
# ex04_big_numbers.py
# Goal: see that Python ints never overflow

small = 1_000
medium = 1_000_000
large = 1_000_000_000
huge = 10 ** 100

print(small, type(small))
print(small, type(medium))
print(small, type(large))
print(small, type(huge))
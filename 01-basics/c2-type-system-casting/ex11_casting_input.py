# Goal: take input from user and cast it to the correct type for calculation

# Run this interactively — type real values when prompted
lenght = float(input("Enter length in meters: "))
width = float(input("Enter width in meters: "))

area = lenght * width
perimeter = 2 * (lenght + width)

print(f"\nLenght : {lenght} m")
print(f"\nWidth : {width} m")
print(f"\nArea : {area} sq.m")
print(f"\nPerimeter : {perimeter} m")

# Show what input() returns before casting
raw = input("Type any number: ")
print(f"Raw type : {type(raw)}")
print(f"Raw value : {raw!r}")  # !r shows the repr — quotes included for str
casted = float(raw)
print(f"After cast: {casted}, type: {type(casted)}")
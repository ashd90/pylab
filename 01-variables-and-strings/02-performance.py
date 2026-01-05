# --- LESSON 1: INPUTS AND MATH ---

# 1. Getting Text (String)
user_name = input("Enter your hacker name: ")

# 2. Getting Numbers (We must convert them!)
# We wrap input() inside int() to turn the text "6" into the number 6
ram_amount = int(input("How much RAM do you have (in GB)? "))

# We wrap input() inside float() for decimal numbers
cpu_speed = float(input("What is your CPU speed (e.g. 1.48)? "))

# Taking User input
tabs_open = int(input("How many Chrome tabs do you have open?: "))

# 3. Doing Logic (Math)
# Python follows standard math rules (PEMDAS)
performance_score = ram_amount * cpu_speed
real_world_score =  performance_score - tabs_open

# 4. The f-string (The best way to show results)
# Putting an 'f' before a string lets you put variables inside { }
print("-" * 30) # Prints a line of 30 dashes
print(f"System Report for {user_name}:")
print(f"Your performance score is: {performance_score}")
print(f"Your real world score is: {real_world_score}")
print("-" * 30)


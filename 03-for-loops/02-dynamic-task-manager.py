# --- PROJECT: PURPLE TASK MANAGER ---

tasks = ["Set up Geany", "Learn Variables"]

print(f"Current Tasks: {tasks}")

# 1. Adding a new task via input
new_task = input("What else do you need to do today? ")
tasks.append(new_task)

# 2. Sorting them alphabetically
tasks.sort()

print("\n--- Your Organized Todo List ---")
# Using a loop to print them neatly
for i, task in enumerate(tasks):
    # 'enumerate' gives us a counter (i) starting at 0
    print(f"{i + 1}. {task}")

# --- PROJECT: LOG TRIMMER ---

# A list representing system logs (newest at the end)
logs = ["User logged in", "Thorium opened", "Geany opened", "Python script run", "Battery low"]

# Concept: Slicing
# [-3:] means "Start at the 3rd item from the end and go to the very end"
recent_logs = logs[-3:]

print("--- Full Log History ---")
print(logs)

print("\n--- Recent Activity (Last 3) ---")
for log in recent_logs:
    print(f">> {log}")

# Concept: range()
print("\nCleaning up old logs...")
for i in range(3):
    print(f"Deleting archive chunk {i+1}...")

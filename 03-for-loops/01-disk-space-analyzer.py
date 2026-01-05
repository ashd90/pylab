# --- PROJECT: DISK SPACE ANALYZER ---

# 1. Concept: The List (Your data set)
file_sizes = [12, 450, 8, 1000, 35, 600]

# 2. Concept: The Accumulator (Starting at zero)
total_size = 0

print("--- Scanning Directory: /home/purple/downloads ---")

# 3. The Loop
for size in file_sizes:
    # Adding the current size to our running total
    total_size = total_size + size
    
    # Logic inside the loop
    if size > 500:
        print(f"⚠️  [LARGE] {size}MB - Consider deleting.")
    else:
        print(f"✅ [SMALL] {size}MB - Optimized.")

# 4. Final Calculation
print("-" * 30)
print(f"Total Disk Space Used: {total_size} MB")

# Level 2 Logic check:
if total_size > 2000:
    print("Action Required: Storage is nearly full!")
else:
    print("Storage status: Healthy.")

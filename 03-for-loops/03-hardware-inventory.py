# --- PROJECT: HARDWARE INVENTORY ---

# 1. Start with lowercase to match our .lower() inputs
hardware = ["monitor", "keyboard", "mouse"]

# 2. Add Item
new_item = input("Please add new item to your inventory: ").lower()
hardware.append(new_item)
hardware.sort()

print(f"Your updated inventory is: {hardware}")

# 3. Remove Item with a Safety Check
remove_item = input("Please enter an item to remove: ").lower()

# New Concept: The 'in' keyword
# This checks if the item exists BEFORE trying to remove it
if remove_item in hardware:
    hardware.remove(remove_item)
    print(f"Done! {remove_item} has been removed.")
else:
    print(f"Error: {remove_item} was not found in your inventory.")

# 4. Final Display
print("\n--- FINAL HARDWARE LIST ---")
for i, item in enumerate(hardware):
    print(f"{i+1}. {item.title()}") # .title() makes it look pretty (Keyboard)

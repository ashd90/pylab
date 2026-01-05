# --- PROJECT: UPDATE SAFETY CHECK ---

battery = int(input("Battery Percentage: "))
plugged_in = input("Is the charger plugged in? (yes/no): ").lower()

# Using 'and' to check two conditions at once
if battery > 80 or plugged_in == "yes":
    print("✅ Safe to update! You have plenty of power.")
    
elif battery > 20 and plugged_in == "no":
    print("⚠️  Safe for coding, but don't start any big updates without your charger.")

else:
    print("❌ DANGER! Plug in your laptop before your system dies!")

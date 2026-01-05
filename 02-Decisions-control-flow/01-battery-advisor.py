# --- PROJECT: BATTERY ADVISOR ---

# 1. Get the current percentage (we'll type it manually for now)
percent = int(input("What is your current battery percentage? "))

# 2. The Decision Logic
if percent == 100:
    print("🔋 Battery is full! You're ready to code for hours.")
    
elif percent >= 50:
    print("⚡ You're in the safe zone. No charger needed yet.")
    
elif percent >= 20:
    print("⚠️  Getting low. Maybe start looking for your charger?")
    
else:
    print("🚨 CRITICAL! Save your work in Geany and plug in NOW!")

print("\nAdvisor check complete.")

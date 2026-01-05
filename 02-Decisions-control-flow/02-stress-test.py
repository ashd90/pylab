# ------ Project: Stess Test ----------

# Ask for the Number of Apps open (e.g., Thorium, Geany, SMPlayer).

apps_open =  int(input("Enter the number of Apps open (e.g Thorium,Alacritty)? "))

if apps_open >= 5:
	print("System stress is high! Close some tabs in Thorium")
elif apps_open >=3:
	print("System is working hard, but stable.")
else:
	print("Smooth sailing! Your AMD E1-1500 is chilling.")	

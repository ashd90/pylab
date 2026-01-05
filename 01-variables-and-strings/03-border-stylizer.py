# --- PROJECT: TERMINAL STYLIZER ---

# 1. Ask the user for the text they want to "Purple-ify"
title = input("What is the title of your project? ")
decorator = input("Enter a symbol for the border (like * or # or -): ")

# 2. Logic: Calculate how long the border should be
# len() counts the number of characters in a string
text_length = len(title)
border_length = text_length + 4 

# 3. Create the styled output
border = decorator * border_length

print("\n" + border)
print(f"{decorator} {title.upper()} {decorator}") # .upper() makes it ALL CAPS
print(border)

print(f"\nSuccess! Header created for {title}.")

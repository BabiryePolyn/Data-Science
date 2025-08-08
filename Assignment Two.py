# Ask user for their first name and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Create full_name by combining names in uppercase with space
full_name = first_name.upper() + " " + last_name.upper()

# Count the number of characters in full name (including space)
name_length = len(full_name)

# Print the greeting message
print(f"Hello, {full_name}! Your name has {name_length} characters.")
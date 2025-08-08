# Get user's name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Calculate birth year (current year - age)
current_year = 2025  # Current year is 2025
birth_year = current_year - age

# Print the message
print(f"Hi {name}, you are {age} years old, so you were born in {birth_year}.")
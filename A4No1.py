# Dictionary operations with car information

# Create a dictionary representing a car
car = {
    'brand': 'Toyota',
    'model': 'Camry',
    'year': 2018
}

print("Original car dictionary:")
print(car)

# Add a new key-value pair for 'color'
car['color'] = 'Blue'
print("\nAfter adding color:")
print(car)

# Update the 'year' to a newer year
car['year'] = 2023
print("\nAfter updating year:")
print(car)

# Remove the 'model' key
del car['model']
print("\nAfter removing model:")
print(car)

# Display final dictionary
print("\nFinal car dictionary:")
print(car)
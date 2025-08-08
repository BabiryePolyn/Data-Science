import math

# Prompt user to enter the radius
radius = float(input("Enter the radius of the circle: "))

# Calculate area (π * r²)
area = math.pi * radius ** 2

# Calculate circumference (2 * π * r)
circumference = 2 * math.pi * radius

# Print results in user-friendly format
print(f"\nResults for circle with radius {radius}:")
print(f"Area: {area:.2f} square units")
print(f"Circumference: {circumference:.2f} units")

print(f"\nThank you for using the circle calculator!")
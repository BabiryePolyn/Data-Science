# Set operations with number sets

# Given sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Set A:")
print(A)
print("\nSet B:")
print(B)

# Find the union of both sets (all unique numbers from both sets)
union_AB = A.union(B)
print("\nUnion of A and B (all unique numbers from both sets):")
print(union_AB)

# Find the difference between set A and set B (numbers in A but not in B)
difference_A_B = A.difference(B)
print("\nDifference A - B (numbers in A but not in B):")
print(difference_A_B)

# Additional operations for better understanding
print("\nAdditional information:")
print(f"Numbers common to both sets (intersection): {A.intersection(B)}")
print(f"Numbers in B but not in A: {B.difference(A)}")
print(f"Numbers unique to either set: {A.symmetric_difference(B)}")
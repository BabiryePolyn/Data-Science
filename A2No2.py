# Given tuple of student scores
scores = (85, 92, 78, 85, 90, 85)
print("Student scores:")
print(scores)

# Find how many times score 85 appears
count_85 = scores.count(85)
print(f"\nThe score 85 appears {count_85} times")

# Find the index of the first occurrence of score 92
index_92 = scores.index(92)
print(f"The first occurrence of score 92 is at index {index_92}")

# Display additional information
print(f"\nScore at index {index_92}: {scores[index_92]}")
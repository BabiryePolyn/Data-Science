# Create a set of my favorite hobbies
my_hobbies = {"reading", "swimming", "cooking", "gaming"}
print("My hobbies:")
print(my_hobbies)

# Add a new hobby to my set
my_hobbies.add("photography")
print("\nAfter adding photography:")
print(my_hobbies)

# Create another set with friend's hobbies
friend_hobbies = {"gaming", "dancing", "cooking", "drawing", "hiking"}
print("\nFriend's hobbies:")
print(friend_hobbies)

# Find hobbies we both have in common (intersection)
common_hobbies = my_hobbies.intersection(friend_hobbies)
print("\nHobbies we both have in common:")
print(common_hobbies)

# Find hobbies unique to me (difference)
my_unique_hobbies = my_hobbies.difference(friend_hobbies)
print("\nHobbies unique to me:")
print(my_unique_hobbies)

# Find hobbies unique to my friend (difference)
friend_unique_hobbies = friend_hobbies.difference(my_hobbies)
print("\nHobbies unique to my friend:")
print(friend_unique_hobbies)

# Find all unique hobbies (symmetric difference)
all_unique_hobbies = my_hobbies.symmetric_difference(friend_hobbies)
print("\nAll hobbies that are unique to either of us:")
print(all_unique_hobbies)
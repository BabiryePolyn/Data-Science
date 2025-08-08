
stationery = ('pen', 'pencil', 'eraser')
print("Original tuple:")
print(stationery)

stationery_list = list(stationery)
stationery_list.remove('pencil')  # Remove pencil
stationery_list.append('ruler')   # Add ruler
new_stationery = tuple(stationery_list)

print("\nAfter friend borrows pencil and adding ruler:")
print(new_stationery)

print("\nAlternative method using tuple operations:")
# Create tuple without pencil
without_pencil = ('pen', 'eraser')  # manually create without pencil

# Add ruler
final_stationery = without_pencil + ('ruler',)
print(final_stationery)
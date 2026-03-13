#lambda and map()to double the elements of a list
numbers = [1, 2, 3, 4, 5]


doubled_numbers = list(map(lambda x: x * 2, numbers))

# Print the new list
print(doubled_numbers)

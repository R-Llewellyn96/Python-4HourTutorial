# Welcome to Python Tutorial 6!

# Dealing with Tuples

# Create a tuple, Tuples are immutable it cant be changed or modified after creation
coordinates = (4, 5)

print(coordinates)

# Can also use an index to access tuple values
print(coordinates[0])

# Trying to change tuple values will cause error e.g.
# coordinates[1] = 10 - ***This will cause an error

# Difference between tuples and lists ****
# Lists can be modified changed or manipulated however you want,
# but a tuple is basically an immutable list, use it to store data that you never want to change
# during program execution

# Tuples can contain multiple sets of elements
coordinates2 = [(4, 5), (6, 7), (80, 34)]

print(coordinates2[2])

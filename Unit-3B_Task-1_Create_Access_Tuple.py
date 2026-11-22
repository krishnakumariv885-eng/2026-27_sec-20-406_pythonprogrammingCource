# Create and Access a Tuple

# Creating a tuple
my_tuple = (10, 20, 30, 40, 50)

# Displaying the tuple
print("Original Tuple:", my_tuple)

# Accessing elements using index
print("First Element:", my_tuple[0])
print("Second Element:", my_tuple[1])
print("Last Element:", my_tuple[-1])

# Accessing elements using slicing
print("First Three Elements:", my_tuple[0:3])
print("Last Two Elements:", my_tuple[-2:])

# Traversing the tuple
print("Tuple Elements:")
for i in my_tuple:
    print(i)

# Finding length of tuple
print("Length of Tuple:", len(my_tuple))

# Checking an element
print("Is 30 present in tuple?", 30 in my_tuple)
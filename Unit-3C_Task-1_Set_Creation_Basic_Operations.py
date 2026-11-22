# Set Creation and Basic Operations

# Creating a set
my_set = {10, 20, 30, 40, 50}

# Displaying the set
print("Original Set:", my_set)

# Adding an element
my_set.add(60)
print("After Adding Element:", my_set)

# Adding multiple elements
my_set.update([70, 80, 90])
print("After Updating Set:", my_set)

# Removing an element
my_set.remove(30)
print("After Removing Element:", my_set)

# Discarding an element
my_set.discard(40)
print("After Discarding Element:", my_set)

# Removing an arbitrary element
my_set.pop()
print("After Pop Operation:", my_set)

# Finding length of set
print("Length of Set:", len(my_set))

# Checking an element
print("Is 50 present in set?", 50 in my_set)

# Clearing the set
my_set.clear()
print("After Clearing Set:", my_set)
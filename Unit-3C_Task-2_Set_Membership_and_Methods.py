# Set Membership and Methods

# Creating a set
my_set = {10, 20, 30, 40, 50}

# Displaying the set
print("Original Set:", my_set)

# Checking membership
print("Is 20 present in set?", 20 in my_set)
print("Is 60 present in set?", 60 in my_set)

# Adding an element
my_set.add(60)
print("After Adding 60:", my_set)

# Updating the set
my_set.update([70, 80])
print("After Update:", my_set)

# Copying the set
new_set = my_set.copy()
print("Copied Set:", new_set)

# Finding length
print("Length of Set:", len(my_set))

# Removing an element
my_set.remove(30)
print("After Remove:", my_set)

# Discarding an element
my_set.discard(40)
print("After Discard:", my_set)

# Checking subset
set1 = {10, 20}
print("Is set1 a subset?", set1.issubset(my_set))

# Checking superset
set2 = {10, 20, 50}
print("Is my_set a superset?", my_set.issuperset(set2))

# Checking disjoint sets
set3 = {100, 200}
print("Are sets disjoint?", my_set.isdisjoint(set3))
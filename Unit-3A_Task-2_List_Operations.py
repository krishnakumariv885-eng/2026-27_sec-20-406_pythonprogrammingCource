# List Operations

# Creating a list
my_list = [10, 20, 30, 40, 50]

print("Original List:", my_list)

# Adding elements
my_list.append(60)
print("After Append:", my_list)

my_list.insert(2, 25)
print("After Insert:", my_list)

# Removing elements
my_list.remove(30)
print("After Remove:", my_list)

my_list.pop()
print("After Pop:", my_list)

# Updating an element
my_list[1] = 100
print("After Update:", my_list)

# Sorting the list
my_list.sort()
print("After Sorting:", my_list)

# Reversing the list
my_list.reverse()
print("After Reversing:", my_list)

# Finding length of list
print("Length of List:", len(my_list))

# Checking an element
print("Is 40 present in list?", 40 in my_list)

# Clearing the list
my_list.clear()
print("After Clear:", my_list)
# Create, Traverse and Display a List

# Creating a list
my_list = [10, 20, 30, 40, 50]

# Displaying the list
print("Original List:", my_list)

# Traversing the list
print("List Elements:")
for i in my_list:
    print(i)

# Accessing elements using index
print("First Element:", my_list[0])
print("Last Element:", my_list[-1])

# Displaying list using index
print("Displaying List using Index:")
for i in range(len(my_list)):
    print("Element at index", i, ":", my_list[i])
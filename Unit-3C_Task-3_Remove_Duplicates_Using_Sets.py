# Remove Duplicates Using Sets

# Creating a list with duplicate elements
my_list = [10, 20, 30, 20, 40, 10, 50, 30]

# Displaying original list
print("Original List:", my_list)

# Converting list into set to remove duplicates
my_set = set(my_list)

# Converting set back into list
new_list = list(my_set)

# Displaying list without duplicates
print("List After Removing Duplicates:", new_list)
# Merge Two Dictionaries

# Creating first dictionary
dict1 = {
    "name": "Krishna",
    "age": 20,
    "course": "Python"
}

# Creating second dictionary
dict2 = {
    "city": "Vijayawada",
    "marks": 90,
    "college": "ABC College"
}

# Displaying original dictionaries
print("First Dictionary:", dict1)
print("Second Dictionary:", dict2)

# Method 1: Using update() method
merged_dict1 = dict1.copy()
merged_dict1.update(dict2)
print("\nMerged Dictionary using update():", merged_dict1)

# Method 2: Using ** operator
merged_dict2 = {**dict1, **dict2}
print("Merged Dictionary using **:", merged_dict2)

# Method 3: Using | operator
merged_dict3 = dict1 | dict2
print("Merged Dictionary using |:", merged_dict3)

# Method 4: Using dictionary unpacking
merged_dict4 = {**dict1, **dict2}
print("Final Merged Dictionary:", merged_dict4)
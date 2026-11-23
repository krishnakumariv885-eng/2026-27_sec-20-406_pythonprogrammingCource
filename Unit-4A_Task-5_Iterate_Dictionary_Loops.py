# Iterate Dictionary using Loops

# Creating a dictionary
student = {
    "name": "Krishna",
    "age": 20,
    "course": "Python",
    "marks": 90,
    "city": "Vijayawada"
}

# Displaying original dictionary
print("Original Dictionary:")
print(student)

# 1. Iterating through keys
print("\nDictionary Keys:")
for key in student:
    print(key)

# 2. Iterating through values
print("\nDictionary Values:")
for value in student.values():
    print(value)

# 3. Iterating through keys and values
print("\nDictionary Items:")
for key, value in student.items():
    print(key, ":", value)

# 4. Iterating using keys() method
print("\nUsing keys() Method:")
for key in student.keys():
    print(key)

# 5. Iterating using items() method
print("\nUsing items() Method:")
for item in student.items():
    print(item)

# 6. Displaying dictionary with numbering
print("\nStudent Details:")
count = 1
for key, value in student.items():
    print(count, ".", key, ":", value)
    count += 1
# Dictionary Methods

# Creating a dictionary
student = {
    "name": "Krishna",
    "age": 20,
    "course": "Python",
    "marks": 90
}

print("Original Dictionary:", student)

# 1. keys() - Returns all keys
print("Keys:", student.keys())

# 2. values() - Returns all values
print("Values:", student.values())

# 3. items() - Returns all key-value pairs
print("Items:", student.items())

# 4. get() - Returns the value of a key
print("Name:", student.get("name"))

# 5. update() - Updates dictionary elements
student.update({"age": 21})
print("After Update:", student)

# 6. pop() - Removes the specified key
student.pop("marks")
print("After Pop:", student)

# 7. popitem() - Removes the last inserted item
student.popitem()
print("After Popitem:", student)

# 8. setdefault() - Returns the value of a key
student.setdefault("city", "Vijayawada")
print("After Setdefault:", student)

# 9. copy() - Creates a copy of dictionary
new_student = student.copy()
print("Copied Dictionary:", new_student)

# 10. clear() - Removes all elements
student.clear()
print("After Clear:", student)
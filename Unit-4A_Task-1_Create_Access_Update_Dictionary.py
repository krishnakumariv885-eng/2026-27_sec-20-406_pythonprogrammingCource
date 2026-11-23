# Create, Access and Update Dictionary

# Creating a dictionary
student = {
    "name": "Krishna",
    "age": 20,
    "course": "Python",
    "marks": 90
}

# Display the dictionary
print("Original Dictionary:", student)

# Accessing dictionary elements
print("Student Name:", student["name"])
print("Student Age:", student["age"])
print("Student Course:", student["course"])
print("Student Marks:", student["marks"])

# Accessing using get()
print("Name using get():", student.get("name"))

# Updating dictionary elements
student["age"] = 21
student["marks"] = 95

# Adding a new element
student["city"] = "Vijayawada"

# Display updated dictionary
print("Updated Dictionary:", student)
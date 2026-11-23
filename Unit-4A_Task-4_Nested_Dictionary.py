# Nested Dictionary

# Creating a nested dictionary
students = {
    "student1": {
        "name": "Krishna",
        "age": 20,
        "course": "Python",
        "marks": 90
    },
    "student2": {
        "name": "Ram",
        "age": 21,
        "course": "Java",
        "marks": 85
    },
    "student3": {
        "name": "Sita",
        "age": 19,
        "course": "C Programming",
        "marks": 95
    }
}

# Displaying the complete dictionary
print("Student Details:")
print(students)

# Accessing nested dictionary elements
print("\nAccessing Student Details:")
print("Student 1 Name:", students["student1"]["name"])
print("Student 1 Age:", students["student1"]["age"])
print("Student 1 Course:", students["student1"]["course"])
print("Student 1 Marks:", students["student1"]["marks"])

# Accessing another student
print("\nStudent 2 Name:", students["student2"]["name"])
print("Student 2 Marks:", students["student2"]["marks"])

# Updating nested dictionary
students["student1"]["marks"] = 98
students["student2"]["age"] = 22

print("\nAfter Updating:")
print(students)

# Adding a new student
students["student4"] = {
    "name": "Ravi",
    "age": 20,
    "course": "HTML",
    "marks": 88
}

print("\nAfter Adding New Student:")
print(students)

# Displaying all student details
print("\nAll Student Details:")
for student, details in students.items():
    print(student)
    for key, value in details.items():
        print(key, ":", value)
    print()
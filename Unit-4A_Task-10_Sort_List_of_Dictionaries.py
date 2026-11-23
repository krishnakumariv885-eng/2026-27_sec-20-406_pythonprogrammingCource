# Sort List of Dictionaries

# Creating a list of dictionaries
students = [
    {"name": "Krishna", "age": 20, "marks": 90},
    {"name": "Ram", "age": 21, "marks": 85},
    {"name": "Sita", "age": 19, "marks": 95},
    {"name": "Ravi", "age": 22, "marks": 80}
]

# Displaying original list
print("Original Student Records:")
for student in students:
    print(student)

# Sorting by name in ascending order
students_by_name = sorted(students, key=lambda x: x["name"])
print("\nSorted by Name:")
for student in students_by_name:
    print(student)

# Sorting by age in ascending order
students_by_age = sorted(students, key=lambda x: x["age"])
print("\nSorted by Age:")
for student in students_by_age:
    print(student)

# Sorting by marks in ascending order
students_by_marks = sorted(students, key=lambda x: x["marks"])
print("\nSorted by Marks (Ascending):")
for student in students_by_marks:
    print(student)

# Sorting by marks in descending order
students_by_marks_desc = sorted(
    students, key=lambda x: x["marks"], reverse=True
)
print("\nSorted by Marks (Descending):")
for student in students_by_marks_desc:
    print(student)

# Sorting the original list by marks
students.sort(key=lambda x: x["marks"])

print("\nOriginal List After Sorting:")
for student in students:
    print(student)
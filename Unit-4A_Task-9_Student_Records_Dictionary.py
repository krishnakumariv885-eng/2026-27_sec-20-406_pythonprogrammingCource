# Student Records using Dictionary

# Creating student records
students = {
    101: {
        "name": "Krishna",
        "age": 20,
        "course": "Python",
        "marks": 90
    },
    102: {
        "name": "Ram",
        "age": 21,
        "course": "Java",
        "marks": 85
    },
    103: {
        "name": "Sita",
        "age": 19,
        "course": "C Programming",
        "marks": 95
    }
}

# Displaying all student records
print("Student Records:")
for roll_no, details in students.items():
    print("\nRoll Number:", roll_no)
    print("Name:", details["name"])
    print("Age:", details["age"])
    print("Course:", details["course"])
    print("Marks:", details["marks"])

# Adding a new student
students[104] = {
    "name": "Ravi",
    "age": 20,
    "course": "HTML",
    "marks": 88
}

print("\nAfter Adding New Student:")
print(students)

# Updating student marks
students[101]["marks"] = 98

print("\nAfter Updating Marks:")
print(students)

# Searching for a student
roll_no = 102

if roll_no in students:
    print("\nStudent Found:")
    print("Name:", students[roll_no]["name"])
    print("Marks:", students[roll_no]["marks"])
else:
    print("\nStudent Not Found")

# Finding average marks
total = 0

for details in students.values():
    total += details["marks"]

average = total / len(students)

print("\nAverage Marks:", average)

# Finding highest marks
topper = max(students, key=lambda x: students[x]["marks"])

print("\nTopper Details:")
print("Name:", students[topper]["name"])
print("Marks:", students[topper]["marks"])

# Deleting a student record
del students[104]

print("\nAfter Deleting Student:")
print(students)
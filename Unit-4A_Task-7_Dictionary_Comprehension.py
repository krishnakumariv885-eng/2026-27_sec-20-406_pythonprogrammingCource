# Dictionary Comprehension

# 1. Creating a dictionary using dictionary comprehension
numbers = [1, 2, 3, 4, 5]
squares = {x: x * x for x in numbers}
print("Squares Dictionary:", squares)

# 2. Creating a dictionary of cubes
cubes = {x: x ** 3 for x in numbers}
print("Cubes Dictionary:", cubes)

# 3. Creating a dictionary of even numbers
even_numbers = {x: x for x in numbers if x % 2 == 0}
print("Even Numbers Dictionary:", even_numbers)

# 4. Creating a dictionary of odd numbers
odd_numbers = {x: x for x in numbers if x % 2 != 0}
print("Odd Numbers Dictionary:", odd_numbers)

# 5. Creating a dictionary using two lists
keys = ["name", "age", "course"]
values = ["Krishna", 20, "Python"]

student = {keys[i]: values[i] for i in range(len(keys))}
print("Student Dictionary:", student)

# 6. Converting values into uppercase
names = ["ram", "sita", "ravi"]
uppercase = {name: name.upper() for name in names}
print("Uppercase Dictionary:", uppercase)

# 7. Creating a dictionary using if-else
result = {x: "Even" if x % 2 == 0 else "Odd" for x in numbers}
print("Even or Odd Dictionary:", result)

# 8. Creating a dictionary from another dictionary
marks = {"Maths": 90, "Science": 85, "English": 95}
updated_marks = {subject: mark + 5 for subject, mark in marks.items()}
print("Updated Marks:", updated_marks)
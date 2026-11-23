# List Comprehension

# Creating a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original List:", numbers)

# 1. Creating a list of squares
squares = [x * x for x in numbers]
print("Squares:", squares)

# 2. Creating a list of even numbers
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even Numbers:", even_numbers)

# 3. Creating a list of odd numbers
odd_numbers = [x for x in numbers if x % 2 != 0]
print("Odd Numbers:", odd_numbers)

# 4. Creating a list of cubes
cubes = [x ** 3 for x in numbers]
print("Cubes:", cubes)

# 5. Creating a list of numbers greater than 5
greater_numbers = [x for x in numbers if x > 5]
print("Numbers Greater Than 5:", greater_numbers)

# 6. Converting names to uppercase
names = ["krishna", "ram", "sita", "ravi"]
uppercase_names = [name.upper() for name in names]
print("Uppercase Names:", uppercase_names)

# 7. Creating a list of even squares
even_squares = [x * x for x in numbers if x % 2 == 0]
print("Even Squares:", even_squares)

# 8. Creating a list using if-else
result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print("Even or Odd:", result)
# Lambda, Map, Filter and Reduce

from functools import reduce

# Creating a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original List:", numbers)

# Using Lambda
square = lambda x: x * x
print("Square of 5:", square(5))

# Using Map to find squares
squares = list(map(lambda x: x * x, numbers))
print("Squares using Map:", squares)

# Using Filter to find even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers using Filter:", even_numbers)

# Using Reduce to find sum
total = reduce(lambda x, y: x + y, numbers)
print("Sum using Reduce:", total)

# Using Reduce to find product
product = reduce(lambda x, y: x * y, numbers)
print("Product using Reduce:", product)
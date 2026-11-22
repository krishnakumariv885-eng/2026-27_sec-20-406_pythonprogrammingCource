# Find Factorial of a Number Using Recursion

# Recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Taking input from user
num = int(input("Enter a number: "))

# Calling the recursive function
result = factorial(num)

# Displaying the result
print("Factorial of", num, "is:", result)
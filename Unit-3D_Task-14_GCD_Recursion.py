# Find GCD of Two Numbers Using Recursion

# Recursive function to calculate GCD
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calling recursive function
result = gcd(num1, num2)

# Displaying the result
print("GCD of", num1, "and", num2, "is:", result)
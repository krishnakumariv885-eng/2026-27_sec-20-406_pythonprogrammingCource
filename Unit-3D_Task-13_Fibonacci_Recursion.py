# Generate Fibonacci Series Using Recursion

# Recursive function to calculate Fibonacci number
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Taking input from user
n = int(input("Enter the number of terms: "))

# Displaying Fibonacci series
print("Fibonacci Series:")

for i in range(n):
    print(fibonacci(i), end=" ")
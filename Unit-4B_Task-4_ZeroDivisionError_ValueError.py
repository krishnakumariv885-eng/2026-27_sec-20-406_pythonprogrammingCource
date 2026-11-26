# Program: ZeroDivisionError and ValueError

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Division Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide a number by zero.")

except ValueError:
    print("Error: Please enter valid integer values.")

print("Program completed successfully.")
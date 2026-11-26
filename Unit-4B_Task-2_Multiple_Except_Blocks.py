# Program: Multiple Except Blocks

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Division Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter only integer values.")

except TypeError:
    print("Error: Invalid data type.")

except Exception as e:
    print("An unexpected error occurred:", e)

print("Program completed successfully.")
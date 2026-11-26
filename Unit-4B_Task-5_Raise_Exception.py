# Program: Raise Exception

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise ValueError("Age must be 18 or above.")

    print("You are eligible to vote.")

except ValueError as e:
    print("Error:", e)

print("Program completed successfully.")
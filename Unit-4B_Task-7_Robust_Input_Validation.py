# Program: Robust Input Validation

while True:
    try:
        age = int(input("Enter your age: "))

        if age <= 0:
            print("Error: Age must be greater than zero.")
            continue

        if age > 120:
            print("Error: Please enter a valid age.")
            continue

        print("Valid Age:", age)
        print("Input accepted successfully.")
        break

    except ValueError:
        print("Error: Please enter numbers only.")
        print("Try again.")

print("Program completed successfully.")
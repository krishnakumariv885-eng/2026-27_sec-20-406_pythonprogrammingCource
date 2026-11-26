# Program: InvalidSpeedError

class InvalidSpeedError(Exception):
    pass


try:
    speed = int(input("Enter vehicle speed: "))

    if speed < 0:
        raise InvalidSpeedError("Speed cannot be negative.")

    elif speed > 120:
        raise InvalidSpeedError("Speed exceeds the allowed limit.")

    else:
        print("Valid Speed:", speed)
        print("Vehicle speed is within the limit.")

except InvalidSpeedError as e:
    print("Error:", e)

except ValueError:
    print("Error: Please enter a valid number.")

print("Program completed successfully.")
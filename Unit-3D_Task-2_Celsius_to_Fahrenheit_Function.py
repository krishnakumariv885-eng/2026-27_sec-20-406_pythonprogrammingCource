# Convert Celsius to Fahrenheit Using Function

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Taking input from user
celsius = float(input("Enter temperature in Celsius: "))

# Calling the function
fahrenheit = celsius_to_fahrenheit(celsius)

# Displaying the result
print("Temperature in Fahrenheit:", fahrenheit)
# Local Variable Does Not Change Global Variable

# Global variable
x = 100

# Function
def display():
    # Local variable
    x = 50
    print("Local Variable x:", x)

# Displaying global variable before function call
print("Global Variable Before Function Call:", x)

# Calling function
display()

# Displaying global variable after function call
print("Global Variable After Function Call:", x)
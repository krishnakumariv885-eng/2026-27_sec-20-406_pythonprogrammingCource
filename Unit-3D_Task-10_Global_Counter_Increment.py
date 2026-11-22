# Global Counter Increment

# Global variable
count = 0

# Function to increment counter
def increment():
    global count
    count += 1
    print("Counter Value:", count)

# Calling the function multiple times
print("Initial Counter Value:", count)

increment()
increment()
increment()
increment()
increment()

# Displaying final counter value
print("Final Counter Value:", count)
# Calculate Simple Interest Using Default Arguments

# Function to calculate simple interest
def simple_interest(principal, rate=5, time=2):
    si = (principal * rate * time) / 100
    return si

# Taking input from user
principal = float(input("Enter principal amount: "))

# Calling function with default arguments
si1 = simple_interest(principal)

# Displaying result
print("Simple Interest with Default Rate and Time:", si1)

# Calling function with user-defined arguments
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

si2 = simple_interest(principal, rate, time)

# Displaying result
print("Simple Interest with User Given Rate and Time:", si2)
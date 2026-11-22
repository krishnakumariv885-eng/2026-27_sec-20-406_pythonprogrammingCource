# Bank Balance Using Global and Local Variables

# Global variable
balance = 10000

# Function to deposit money
def deposit(amount):
    global balance
    balance += amount
    print("Amount Deposited:", amount)
    print("Updated Balance:", balance)

# Function to withdraw money
def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Amount Withdrawn:", amount)
        print("Updated Balance:", balance)
    else:
        print("Insufficient Balance!")

# Function to display balance
def display_balance():
    print("Current Bank Balance:", balance)

# Display initial balance
print("Initial Balance:", balance)

# Deposit money
deposit(5000)

# Withdraw money
withdraw(3000)

# Display final balance
display_balance()
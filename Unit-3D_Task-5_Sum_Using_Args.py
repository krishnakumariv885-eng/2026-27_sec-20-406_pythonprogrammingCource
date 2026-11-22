# Find Sum of Numbers Using *args

# Function to calculate sum
def calculate_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

# Calling the function
result1 = calculate_sum(10, 20, 30)
result2 = calculate_sum(5, 10, 15, 20)
result3 = calculate_sum(1, 2, 3, 4, 5)

# Displaying results
print("Sum of 3 Numbers:", result1)
print("Sum of 4 Numbers:", result2)
print("Sum of 5 Numbers:", result3)
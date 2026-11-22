# Calculate Total and Average Marks Using Function

# Function to calculate total marks
def calculate_total(marks):
    total = sum(marks)
    return total

# Function to calculate average marks
def calculate_average(marks):
    average = sum(marks) / len(marks)
    return average

# Taking input from user
n = int(input("Enter number of subjects: "))

marks = []

for i in range(n):
    mark = float(input("Enter marks for subject " + str(i + 1) + ": "))
    marks.append(mark)

# Calling functions
total = calculate_total(marks)
average = calculate_average(marks)

# Displaying results
print("Total Marks:", total)
print("Average Marks:", average)
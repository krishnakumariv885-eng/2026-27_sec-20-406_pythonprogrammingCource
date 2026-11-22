# Calculate Area and Perimeter of a Rectangle Using Functions

# Function to calculate area
def calculate_area(length, breadth):
    area = length * breadth
    return area

# Function to calculate perimeter
def calculate_perimeter(length, breadth):
    perimeter = 2 * (length + breadth)
    return perimeter

# Taking input from user
length = float(input("Enter the length of rectangle: "))
breadth = float(input("Enter the breadth of rectangle: "))

# Calling functions
area = calculate_area(length, breadth)
perimeter = calculate_perimeter(length, breadth)

# Displaying results
print("Area of Rectangle:", area)
print("Perimeter of Rectangle:", perimeter)
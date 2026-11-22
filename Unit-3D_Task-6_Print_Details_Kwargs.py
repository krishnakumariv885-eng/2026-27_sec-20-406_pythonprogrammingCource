# Print Details Using **kwargs

# Function to print details
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

# Calling the function
print("Student Details:")
print_details(
    Name="Krishna",
    Age=20,
    Course="Python",
    College="ABC College",
    Marks=90
)

print("\nEmployee Details:")
print_details(
    Name="Rahul",
    Age=25,
    Department="IT",
    Salary=30000
)
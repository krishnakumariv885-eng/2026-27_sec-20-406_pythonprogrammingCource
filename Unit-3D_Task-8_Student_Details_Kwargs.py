# Student Details Using **kwargs

# Function to display student details
def student_details(**kwargs):
    print("Student Details:")

    for key, value in kwargs.items():
        print(key, ":", value)

# Calling the function
student_details(
    Name="Krishna",
    Roll_Number=101,
    Age=20,
    Course="Python",
    College="ABC College",
    Marks=90
)
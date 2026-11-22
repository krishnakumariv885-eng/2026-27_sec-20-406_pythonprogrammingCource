# Matrix Operations using Nested Lists

# Creating two matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Displaying first matrix
print("First Matrix:")
for row in matrix1:
    print(row)

# Displaying second matrix
print("\nSecond Matrix:")
for row in matrix2:
    print(row)

# Matrix Addition
addition = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(matrix1[i][j] + matrix2[i][j])
    addition.append(row)

print("\nMatrix Addition:")
for row in addition:
    print(row)

# Matrix Subtraction
subtraction = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(matrix1[i][j] - matrix2[i][j])
    subtraction.append(row)

print("\nMatrix Subtraction:")
for row in subtraction:
    print(row)

# Matrix Multiplication
multiplication = []
for i in range(3):
    row = []
    for j in range(3):
        total = 0
        for k in range(3):
            total += matrix1[i][k] * matrix2[k][j]
        row.append(total)
    multiplication.append(row)

print("\nMatrix Multiplication:")
for row in multiplication:
    print(row)

# Transpose of First Matrix
transpose = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(matrix1[j][i])
    transpose.append(row)

print("\nTranspose of First Matrix:")
for row in transpose:
    print(row)
# Tuple Operations

# Creating tuples
tuple1 = (10, 20, 30, 40, 50)
tuple2 = (60, 70, 80, 90)

# Displaying tuples
print("First Tuple:", tuple1)
print("Second Tuple:", tuple2)

# Concatenation
tuple3 = tuple1 + tuple2
print("After Concatenation:", tuple3)

# Repetition
tuple4 = tuple1 * 2
print("After Repetition:", tuple4)

# Accessing elements
print("First Element:", tuple1[0])
print("Last Element:", tuple1[-1])

# Slicing
print("Sliced Tuple:", tuple1[1:4])

# Finding length
print("Length of Tuple:", len(tuple1))

# Finding maximum and minimum
print("Maximum Element:", max(tuple1))
print("Minimum Element:", min(tuple1))

# Counting elements
print("Count of 20:", tuple1.count(20))

# Finding index
print("Index of 30:", tuple1.index(30))

# Checking an element
print("Is 40 present?", 40 in tuple1)

# Converting tuple into list
my_list = list(tuple1)
print("Tuple Converted into List:", my_list)
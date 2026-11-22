# Swap Two Numbers Using Tuple Unpacking

# Taking input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Displaying values before swapping
print("Before Swapping:")
print("a =", a)
print("b =", b)

# Swapping using tuple unpacking
a, b = b, a

# Displaying values after swapping
print("After Swapping:")
print("a =", a)
print("b =", b)
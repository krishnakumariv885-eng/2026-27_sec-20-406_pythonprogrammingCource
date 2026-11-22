# Program to calculate Compound Interest

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time in years: "))

amount = principal * (1 + rate / 100) ** time

compound_interest = amount - principal

print("Total Amount:", amount)
print("Compound Interest:", compound_interest)
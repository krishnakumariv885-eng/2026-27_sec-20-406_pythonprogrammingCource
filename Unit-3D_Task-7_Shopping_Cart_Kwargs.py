# Shopping Cart Using **kwargs

# Function to calculate shopping cart total
def shopping_cart(**items):
    total = 0

    print("Shopping Cart Details:")

    for item, price in items.items():
        print(item, ":", price)
        total += price

    print("Total Amount:", total)

# Calling the function
shopping_cart(
    Apple=50,
    Banana=30,
    Mango=60,
    Orange=40,
    Grapes=80
)
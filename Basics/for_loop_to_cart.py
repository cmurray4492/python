cart = []

try:
    n = int(input("Enter the number of items you want to add to the cart: "))
except ValueError:
    print("Please enter a valid number.")
    n = int(input("Enter the number of items you want to add to the cart: "))

while n <= 0:
    print("Please enter a valid number of items.")
    n = int(input("Enter the number of items you want to add to the cart: "))

for i in range(n):
    item = input(f"Enter the name of item {i + 1}: ")
    cart.append(item)

print("\n")

print("Items in your cart:")
for item in cart:
    print(item)

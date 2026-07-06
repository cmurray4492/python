cart = []

while True:
    # need a try block to handle blank input or unexpected errors
    try:
        item = input("Enter item to add to cart (or type 'done' to end): ")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        break
    if not item:
        print("Please enter a valid item.")
        continue
    if item.lower() == 'done':
        break
    cart.append(item)
    print(f"{item} has been added to your cart.")

print("\nYour shopping cart contains:")
for i, item in enumerate(cart, start=1):
    print(f"{i}. {item}")

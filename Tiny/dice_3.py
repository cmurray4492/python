import random

while True:
    roll = random.randint(1, 6)
    print(f"You rolled a {roll}.")

    again = input("Roll again? (y/n): ")
    if again.lower() != 'y':
        print("Thanks for playing!")
        break

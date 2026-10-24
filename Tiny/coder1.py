# This will the user pick decoder or encoder and then run the function
from decoder3 import decoder
from encoder3 import encoder


def main():
    choice = (input("Do you want to encode or decode a "
              "message? (e/d/q): ").lower())

    if choice == 'e':
        encoder()
    elif choice == 'd':
        decoder()
    elif choice == 'q':
        print("Exiting the program.")
        return
    else:
        print("Invalid choice. Please enter 'e' for encode or 'd' "
              "for decode or 'q' to quit.")

    main()


if __name__ == "__main__":
    main()

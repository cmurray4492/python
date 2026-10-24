
def decoder():
    secret = input("Enter a message to decode: ").upper()
    message = ""

    for letter in secret:
        if letter.isalpha():
            # Convert letter to number, shift, wrap around with %
            shifted = (ord(letter) - 65 - 3) % 26 + 65
            message += chr(shifted)
        else:
            message += letter  # Non-alphabetic characters are not encoded

    print("Original message:", secret)
    print("Decoded message:", message)


if __name__ == "__main__":
    decoder()

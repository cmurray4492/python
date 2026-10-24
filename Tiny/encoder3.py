
def encoder():
    # The is the encoder function
    message = input("Enter a message to encode: ").upper()
    secret = ""

    for letter in message:
        if letter.isalpha():
            # Convert letter to number, shift, wrap around with %
            shifted = (ord(letter) - 65 + 3) % 26 + 65
            secret += chr(shifted)
        else:
            secret += letter  # Non-alphabetic characters are not encoded

    print("Original message:", message)
    print("Encoded message:", secret)


if __name__ == "__main__":
    encoder()

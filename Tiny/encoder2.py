message = "ZEBRA" 
secret = ""

for letter in message:
    # Convert letter to number, shift, wrap around with %
    shifted = (ord(letter) - 65 + 3) % 26 + 65
    secret += chr(shifted)

print("Original message:", message)
print("Encoded message:", secret)

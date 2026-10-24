message = "HELLO"
secret = ""

for letter in message:
    secret += chr(ord(letter) + 3)

print("Original message:", message)
print("Encoded message:", secret)

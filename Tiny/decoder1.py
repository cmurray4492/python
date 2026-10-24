secret = "KHOOR"
decoded = ""

for letter in secret:
    decoded += chr(ord(letter) - 3)

print("Encoded message:", secret)
print("Decoded message:", decoded)

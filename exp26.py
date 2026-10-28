def caesar(text, shift):
    result = ""

    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) - 97 + shift) % 26 + 97)
        else:
            result += ch

    return result


text = input("Enter message: ")
shift = int(input("Enter shift: "))

encrypted = caesar(text, shift)
decrypted = caesar(encrypted, -shift)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
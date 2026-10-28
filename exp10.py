f = open("student.txt", "r")
data = f.read()
alphabets = 0
digits = 0
spaces = 0
special = 0
for ch in data:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1
nprint("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

f.close()
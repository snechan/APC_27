s = input("Enter a string: ")
ch = input("Enter a character: ")

count = 0

for x in s:
    if x == ch:
        count += 1

print("Frequency:", count)
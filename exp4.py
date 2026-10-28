s = input("Enter a string: ")

reverse = ""

for ch in s:
    reverse = ch + reverse

if s == reverse:
    print("String is Palindrome")
else:
    print("String is Not Palindrome")
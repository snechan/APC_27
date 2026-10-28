def palindrome(s):
    return str(s) == str(s)[::-1]

print(palindrome("madam"))
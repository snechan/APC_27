f = open("student.txt", "r")
text = f.read()
f.close()

words = text.split()

if words:
    longest = max(words, key=len)
    print("Longest word:", longest)
    print("Length:", len(longest))
else:
    print("File is empty.")
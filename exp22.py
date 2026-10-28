with open("file1.txt", "r") as f1:
    text1 = f1.read()

with open("file2.txt", "r") as f2:
    text2 = f2.read()

with open("combined.txt", "w") as f3:
    f3.write(text1 + "\n" + text2)

print("Files combined successfully.")
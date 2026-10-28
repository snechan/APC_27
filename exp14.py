old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

f = open("student.txt", "r")
text = f.read()
f.close()

text = text.replace(old_word, new_word)

f = open("student.txt", "w")
f.write(text)
f.close()

print("Word replaced successfully.")
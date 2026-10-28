f = open("student.txt", "r")
text = f.read().lower()
f.close()

words = text.split()
frequency = {}

for word in words:
    word = word.strip(".,!?;:")
    if word:
        frequency[word] = frequency.get(word, 0) + 1

print("Word frequency:")
print(frequency)
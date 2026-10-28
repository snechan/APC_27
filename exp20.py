sentence = input("Enter a sentence: ")
word = input("Enter word: ")

words = sentence.split()
count = words.count(word)

print("Occurrences:", count)
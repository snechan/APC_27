words = ["apple", "banana", "cat", "orange"]

print(list(map(lambda x: len(x), words)))
print(list(filter(lambda x: len(x) > 5, words)))
print(sorted(words, key=lambda x: len(x)))
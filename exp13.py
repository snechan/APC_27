word = input("Enter word to search: ").lower()

f = open("student.txt", "r")
count = 0

for line_no, line in enumerate(f, start=1):
    words = line.lower().split()
    occurrences = sum(
        1 for w in words
        if w.strip(".,!?;:") == word
    )

    if occurrences > 0:
        print("Line number:", line_no)
        count += occurrences

f.close()
print("Total occurrences:", count)
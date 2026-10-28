s = input("Enter a string: ")

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

values = sorted(freq.values(), reverse=True)

if len(values) < 2:
    print("Second most frequent character does not exist")
else:
    second = values[1]

    for ch, count in freq.items():
        if count == second:
            print("Second most frequent character:", ch)
            print("Frequency:", count)
            break
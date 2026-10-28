products = [("Pen", 20, 10), ("Bag", 1500, 2)]

total = list(map(lambda x: (x[0], x[1] * x[2]), products))
print(total)
print(list(filter(lambda x: x[1] > 1000, total)))
print(sorted(total, key=lambda x: x[1]))
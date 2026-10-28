# 25. Remove all duplicate elements while preserving original order.

a = [1, 2, 2, 3, 1, 4, 3]
b = []

for x in a:
    if x not in b:
        b.append(x)

print(b)
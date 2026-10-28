# 23. Count the frequency of each element in a list.

a = [1, 2, 2, 3, 3, 3]

for x in set(a):
    print(x, "=", a.count(x))
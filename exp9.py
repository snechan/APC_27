def largest(a):
    big = a[0]
    for i in a:
        if i > big:
            big = i
    return big

print(largest([10, 25, 5, 40, 15]))
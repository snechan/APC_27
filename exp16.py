def second_largest(a):
    a = sorted(set(a))
    return a[-2]

print(second_largest([10, 20, 30, 40]))
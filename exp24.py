# 24. Rotate a list left by one position and right by one position.

a = [1, 2, 3, 4, 5]

print("Left:", a[1:] + a[:1])
print("Right:", a[-1:] + a[:-1])
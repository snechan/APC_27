# Q6. Write a PYTHON program to compute the cosine series.
# cos(x) = 1 - x²/2! + x⁴/4! - x⁶/6! + ... xⁿ/n!

import math

x = float(input("Enter x: "))
n = int(input("Enter n: "))

sum = 0

for i in range(0, n + 1, 2):
    term = (x ** i) / math.factorial(i)

    if (i // 2) % 2 == 0:
        sum = sum + term
    else:
        sum = sum - term

print("Cosine value =", sum)
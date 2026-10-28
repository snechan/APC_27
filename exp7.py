# Q7. Write a short PYTHON program to check whether
# the square root of number is prime or not.

import math

n = int(input("Enter a number: "))

root = int(math.sqrt(n))
count = 0

for i in range(1, root + 1):
    if root % i == 0:
        count = count + 1

if count == 2:
    print("Square root is Prime")
else:
    print("Square root is Not Prime")
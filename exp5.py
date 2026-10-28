# Q5. Write a PYTHON program to sum the given sequence
# 1 + 1/1! + 1/2! + 1/3! + .... + 1/n!

n = int(input("Enter n: "))

fact = 1
sum = 1

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + (1 / fact)

print("Sum =", sum)
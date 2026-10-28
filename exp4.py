# Q4. Write a PYTHON program that prints 1 2 4 8 16 32 ... n².

n = int(input("Enter n: "))

for i in range(n + 1):
    print(2 ** i)
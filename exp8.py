# Q8. Write a PYTHON program to produce following design.
# A B C
# A B C
# A B C

n = int(input("Enter n: "))

for i in range(n):
    for j in range(3):
        print(chr(65 + j), end=" ")
    print()
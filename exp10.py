def prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, n))

a = [2, 3, 4, 5, 6, 7]
print(list(filter(lambda x: prime(x), a)))
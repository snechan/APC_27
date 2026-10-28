def search(a, x, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if a[mid] == x:
        return mid
    elif x < a[mid]:
        return search(a, x, low, mid - 1)
    else:
        return search(a, x, mid + 1, high)

a = [10, 20, 30, 40, 50]
print(search(a, 30, 0, len(a) - 1))
def bill(price, quantity):
    total = price * quantity
    discount = total * 0.10
    return total - discount

print(bill(100, 5))
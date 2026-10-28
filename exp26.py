def bill(units):
    amount = units * 5
    tax = amount * 0.05
    return amount + tax

print(bill(100))
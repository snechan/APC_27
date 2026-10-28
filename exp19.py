def bill(units):
    if units <= 100:
        amount = units * 2
    elif units <= 200:
        amount = 200 + (units - 100) * 3
    else:
        amount = 500 + (units - 200) * 5
    return amount

print(bill(150))
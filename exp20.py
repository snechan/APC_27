transactions = [
    ("Deposit", 5000),
    ("Withdrawal", 1000),
    ("Deposit", 2000),
    ("Withdrawal", 500)
]

with open("transactions.txt", "w") as f:
    for kind, amount in transactions:
        f.write(f"{kind},{amount}\n")

deposits = 0
withdrawals = 0
amounts = []

with open("transactions.txt", "r") as f:
    for line in f:
        kind, amount = line.strip().split(",")
        amount = float(amount)
        amounts.append(amount)

        if kind == "Deposit":
            deposits += amount
        else:
            withdrawals += amount

print("Total deposits:", deposits)
print("Total withdrawals:", withdrawals)
print("Final balance:", deposits - withdrawals)
print("Largest transaction:", max(amounts))
balance = 1000
history = []

def deposit(amount):
    global balance
    balance += amount
    history.append("Deposited")

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        history.append("Withdrawn")
    else:
        print("Insufficient balance")

def enquiry():
    print("Balance:", balance)

deposit(500)
withdraw(200)
enquiry()
print(history)
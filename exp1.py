class BankAccount:
    account_counter = 1000

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        BankAccount.account_counter += 1
        self.account_number = BankAccount.account_counter

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Error: Insufficient balance.")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ₹{self.balance}")

    def transfer(self, amount, other_account):
        if amount <= 0:
            print("Invalid transfer amount.")
        elif amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(
                f"₹{amount} transferred successfully "
                f"to {other_account.account_holder}."
            )
        else:
            print("Error: Insufficient balance for transfer.")


# Create two bank accounts
account1 = BankAccount("Rahul")
account2 = BankAccount("Priya")

# Perform operations
account1.deposit(5000)
account1.withdraw(1000)
account1.transfer(1500, account2)

account2.deposit(2000)
account2.withdraw(500)

# Display final balances
print("\n--- Final Account Details ---")
account1.display_balance()

print()
account2.display_balance()
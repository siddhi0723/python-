class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid Deposit Amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
        else:
            print("Invalid Withdrawal Amount.")

    def check_balance(self):
        print(f"Account Balance: {self.balance}")


print("Total summary of your account:")
account = BankAccount(10000, 350)
account.deposit(3000)
account.withdraw(100)
account.check_balance()
import json
import random

class Account:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit successful. New balance: {self.balance}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal successful. New balance: {self.balance}"
        return "Insufficient funds or invalid amount."

    def to_dict(self):
        return {"account_number": self.account_number, "name": self.name, "balance": self.balance}

    @staticmethod
    def from_dict(data):
        return Account(data["account_number"], data["name"], data["balance"])

class Bank:
    def __init__(self, filename="accounts.txt"):
        self.accounts = {}
        self.filename = filename
        self.load_from_file()

    def create_account(self, name, initial_deposit=0.0):
        account_number = str(random.randint(100000, 999999))
        while account_number in self.accounts:
            account_number = str(random.randint(100000, 999999))
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        self.save_to_file()
        return f"Account created successfully! Account Number: {account_number}"

    def view_account(self, account_number):
        if account_number in self.accounts:
            acc = self.accounts[account_number]
            return f"Account Number: {acc.account_number}, Name: {acc.name}, Balance: {acc.balance}"
        return "Account not found."

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            result = self.accounts[account_number].deposit(amount)
            self.save_to_file()
            return result
        return "Account not found."

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            result = self.accounts[account_number].withdraw(amount)
            self.save_to_file()
            return result
        return "Account not found."

    def save_to_file(self):
        with open(self.filename, "w") as file:
            json.dump({acc: self.accounts[acc].to_dict() for acc in self.accounts}, file)

    def load_from_file(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.accounts = {acc: Account.from_dict(data[acc]) for acc in data}
        except (FileNotFoundError, json.JSONDecodeError):
            self.accounts = {}

# Sample CLI Menu
def main():
    bank = Bank()
    while True:
        print("\nWelcome to the Bank Application")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter your name: ")
            deposit = float(input("Enter initial deposit: "))
            print(bank.create_account(name, deposit))
        elif choice == "2":
            acc_num = input("Enter account number: ")
            print(bank.view_account(acc_num))
        elif choice == "3":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            print(bank.deposit(acc_num, amount))
        elif choice == "4":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            print(bank.withdraw(acc_num, amount))
        elif choice == "5":
            print("Thank you for using the bank application!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

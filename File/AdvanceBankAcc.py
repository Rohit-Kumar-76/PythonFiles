import random
import datetime

class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.account_number = self.generate_account_number()
        self.balance = initial_balance
        self.transactions = []

    def generate_account_number(self):
        return random.randint(10000000, 99999999)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append((datetime.datetime.now(), f"Deposited ₹{amount}"))
            print(f"₹{amount} deposited. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            self.transactions.append((datetime.datetime.now(), f"Withdrew ₹{amount}"))
            print(f"₹{amount} withdrawn. New balance: ₹{self.balance}")

    def get_balance(self):
        print(f"Current balance: ₹{self.balance}")
        return self.balance

    def apply_interest(self, rate):
        interest = self.balance * (rate / 100)
        self.balance += interest
        self.transactions.append((datetime.datetime.now(), f"Interest added ₹{interest:.2f}"))
        print(f"Interest ₹{interest:.2f} applied. New balance: ₹{self.balance:.2f}")

    def show_transactions(self):
        print(f"Transaction history for {self.owner}:")
        for time, action in self.transactions:
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {action}")

# 🔹 Menu system
def main():
    name = input("Enter your name: ")
    account = BankAccount(name, 0)
    print(f"\nWelcome, {account.owner}! Your account number is {account.account_number}")

    while True:
        print("\n--- Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Apply Interest")
        print("5. Show Transactions")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            amt = float(input("Enter amount to deposit: "))
            account.deposit(amt)
        elif choice == '2':
            amt = float(input("Enter amount to withdraw: "))
            account.withdraw(amt)
        elif choice == '3':
            account.get_balance()
        elif choice == '4':
            rate = float(input("Enter interest rate (%): "))
            account.apply_interest(rate)
        elif choice == '5':
            account.show_transactions()
        elif choice == '6':
            print("Thank you for using the bank system.")
            break
        else:
            print("Invalid option. Try again.")

# 🔹 Run the program
if __name__ == "__main__":
    main()

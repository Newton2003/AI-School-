"""
class exercise:

create a bank account class with account_name,account_number 
and balance with methods for deposit, withdraw and get_balance

then create a new instance of the class 
"""

class BankAccount:
    def __init__(self, Account_Name, account_number, balance):
        self.Account_Name = Account_Name
        self.account_numbe
        r = account_number
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")
        
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Withdrawal amount must be positive and less than or equal to the current balance.")
        
    def get_balance(self):
        return self.balance
                       
        
        
my_account = BankAccount("newton",123456789, 1000)    
print(f"account holder {my_account.Account_Name}")
print(f"Account Number: {my_account.account_number}")
print(f"Initial Balance: {my_account.get_balance()}")
print("Depositing $500...")
        
        
import random

class bank:
    def __init__(self, Holder:str, account_number:int, balance=0):
        #assign to self object
        self.account_number = account_number
        self.balance = balance
        self.Holder = Holder
        
        
    def deposit(self, amount:float):
    
        if amount>0:
            self.balance+=amount
            print(f"Depoisted amount: {amount}, New Balance: {self.balance}")
        else:
            print("deposite must be a positive amount") 
            
    def withdraw (self, amount:float):
        if  amount<=self.balance:
            self.balance-=amount
            print(f"withdrew {amount}, New balance: {self.balance}.")
        else:
            print("withdraw amount must be positive and less than or equal to current balance")   
            
    def get_balance(self):
        return self.balance
    
    
acc1=bank("Newton", 42429294004, 20000000)
acc2=bank("Jake", 9023313139, 400000)
acc3=bank("Mike", 9183173842, 70033445)    

max_amount = 1000000
min_amount = 20000

for accounts in [acc1, acc2, acc3]:
    print(f"{accounts.Holder}: Balance ==> {accounts.get_balance()}")
    accounts.deposit(random.randint(1,max_amount))
    accounts.withdraw(random.randint(1,min_amount))
    print("")
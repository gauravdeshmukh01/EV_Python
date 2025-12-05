class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acct_name):
        self.balance = initialAmount
        self.acct_name = acct_name
        
    def get_balance(self):
        print(f"Account balance is:{self.balance:.2f}")
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount:.2f}. New balance is:{self.balance:.2f}")
        
    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException("Sorry less amount")
            
    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print(f"new balance is {self.balance:.2f}")
        except BalanceException as e:
            print(e)

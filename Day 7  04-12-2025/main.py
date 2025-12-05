from exception import *

sudha = BankAccount(1000, "sudha")
ramesh = BankAccount(2000, "ramesh")

sudha.get_balance()
ramesh.get_balance()

sudha.deposit(5000)
ramesh.deposit(6000)

sudha.withdraw(100)

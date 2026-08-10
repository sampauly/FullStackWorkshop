""" Define abstract class for generic account details and abstract method for withdraws """

from abc import ABC, abstractmethod
from transaction import Transaction

# Base class
class Account(ABC):
    def __init__(self, account_id, balance=0):
        self.account_id = account_id 
        self.balance = balance # should be protected 

    def deposit(self, amount):
        self.balance += amount

    @abstractmethod
    def withdraw(self, amount):
        pass

class CheckingAccount(Account, Transaction):
    def __init__(self, account_id, balance=0, overdraft_limit=100):
        super().__init__(account_id, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        # overdraft allowed
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Insufficient funds: exceeds overdraft limit")
        self.balance -= amount

class SavingsAccount(Account, Transaction):
    def __init__(self, account_id, balance=0):
        super().__init__(account_id, balance)

    def withdraw(self, amount):
        # overdraft NOT allowed
        if self.balance < amount:
            raise ValueError("Insufficient funds: below minimum balance")
        self.balance -= amount


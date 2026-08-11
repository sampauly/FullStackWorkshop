""" Defines Transaction pseudo interface using an ABC """

from abc import ABC, abstractmethod

class Transaction(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass
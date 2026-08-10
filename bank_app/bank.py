""" Defines bank class """
from customer import Customer
from transaction import Transaction
from accounts import Account


class Bank:
    def __init__(self, branch_id):
        self.customers = {} # map customer id to a customer
        self.branch_id = branch_id

    def add_customer(self, customer):
        if customer.customer_id not in self.customers:
            self.customers[customer.customer_id] = customer
        # can only add customer if the customer_id is not already used
        # let user know that the customer id is already in use

    def get_customer(self, customer_id):
        return self.customers.get(customer_id)

    def transfer(self, from_account, to_account, amount):
        from_account.withdraw(amount)
        to_account.deposit(amount)
    
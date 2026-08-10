""" Define the customer class """

class Customer:
    def __init__(self, name, email, branch_id, customer_id, accounts=None):
        self.name = name
        self.email = email
        self.branch_id = branch_id
        self.customer_id = customer_id
        self.accounts = accounts if accounts is not None else []





from models.customer import Customer

class CustomerService:
    def __init__(self):
        self.customers = {}
        self._next_id = 1

    def create_customer(self, name, email, branch_id):
        customer_id = self._next_id
        customer = Customer(name=name, email=email, branch_id=branch_id, customer_id=customer_id)
        self.customers[customer_id] = customer
        self._next_id += 1
        return customer

    def list_customers(self):
        return list(self.customers.values())

# shared instance standing in for database
customer_service = CustomerService()
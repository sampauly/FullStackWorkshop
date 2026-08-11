from models.customer import Customer
from db import db 

class CustomerService:
    def __init__(self):
        self.collection = db["users"]

    def create_customer(self, name, email, branch_id):
        result = self.collection.insert_one({
            "name": name,
            "email": email,
            "branch_id": branch_id,
        })
        return self.collection.find_one({"_id": result.inserted_id})

    def list_customers(self):
        return list(self.collection.find())

customer_service = CustomerService()
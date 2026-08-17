from db import db
from bson import ObjectId
from bson.errors import InvalidId

class CustomerRepository:
    def __init__(self):
        self.collection = db["users"]

    def insert(self, customer_dict):
        result = self.collection.insert_one(customer_dict)
        return self.collection.find_one({"_id": result.inserted_id})

    def find_all(self):
        return list(self.collection.find())

    def find_by_id(self, customer_id):
        try:
            object_id = ObjectId(customer_id)
        except InvalidId:
            return None
        return self.collection.find_one({"_id": object_id})

    def delete(self, customer_id):
        try:
            object_id = ObjectId(customer_id)
        except InvalidId:
            return None
        result = self.collection.delete_one({"_id": object_id})
        return result.deleted_count > 0 # True if customer was actually deleted 

customer_repository = CustomerRepository()
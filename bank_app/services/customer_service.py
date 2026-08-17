from repositories.customer_repository import customer_repository

class CustomerService:
    def create_customer(self, name, email, branch_id):
        return customer_repository.insert({"name": name, "email": email, "branch_id": branch_id})

    def list_customers(self):
        return customer_repository.find_all()
    
    def get_customer(self, customer_id):
        return customer_repository.find_by_id(customer_id)

    def delete_customer(self, customer_id):
        return customer_repository.delete(customer_id)

customer_service = CustomerService()
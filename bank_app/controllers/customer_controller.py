from pydantic import BaseModel
from fastapi import APIRouter
from services.customer_service import customer_service

router = APIRouter(prefix="/api/v1/customers")

# request shape
class CustomerCreateRequest(BaseModel):
    name: str
    email: str
    branch_id: str

# response shape 
class CustomerResponse(BaseModel):
    customer_id: int
    name: str
    email: str
    branch_id: str

# POST Method for creating a customer
@router.post("", response_model=CustomerResponse, status_code=201)
def create_customer(body: CustomerCreateRequest):
    customer = customer_service.create_customer(body.name, body.email, body.branch_id)
    return CustomerResponse(
        customer_id=customer.customer_id,
        name=customer.name,
        email=customer.email,
        branch_id=customer.branch_id,
    )

# GET Method for list of customers
@router.get("", response_model=list[CustomerResponse])
def list_customers():
    customers = customer_service.list_customers()
    return [
        CustomerResponse(
            customer_id=c.customer_id,
            name=c.name,
            email=c.email,
            branch_id=c.branch_id,
        )
        for c in customers
    ]







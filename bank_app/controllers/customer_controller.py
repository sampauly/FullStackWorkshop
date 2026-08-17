from pydantic import BaseModel, Field
from fastapi import APIRouter, HTTPException
from services.customer_service import customer_service

router = APIRouter(prefix="/api/v1/customers")

# request shape
class CustomerCreateRequest(BaseModel):
    name: str
    email: str
    branch_id: str

# response shape 
class CustomerResponse(BaseModel):
    id: str = Field(alias="_id")
    name: str
    email: str
    branch_id: str

    model_config = {
                    "validate_by_name": True,
                    "validate_by_alias": True,
                    "populate_by_name": True,
                    }

# POST Method for creating a customer
@router.post("", response_model=CustomerResponse, status_code=201)
def create_customer(body: CustomerCreateRequest):
    customer = customer_service.create_customer(body.name, body.email, body.branch_id)
    return CustomerResponse(
        id=str(customer["_id"]),
        name=customer["name"],
        email=customer["email"],
        branch_id=customer["branch_id"],
    )

# GET Method for list of customers
@router.get("", response_model=list[CustomerResponse])
def list_customers():
    customers = customer_service.list_customers()
    return [
        CustomerResponse(
            id=str(c["_id"]),
            name=c["name"],
            email=c["email"],
            branch_id=c["branch_id"],
        )
        for c in customers
    ]

# GET Method for finding a certain customer 
@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer(customer_id: str):
    customer = customer_service.get_customer(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return CustomerResponse(
        id=str(customer["_id"]),
        name=customer["name"],
        email=customer["email"],
        branch_id=customer["branch_id"],
    )


# DELETE Method for finding a certain customer
@router.delete("/{customer_id}", status_code=204)
def delete_customer(customer_id: str):
    deleted_customer = customer_service.delete_customer(customer_id)
    if not deleted_customer:
        raise HTTPException(status_code=404, detail="Customer not found")







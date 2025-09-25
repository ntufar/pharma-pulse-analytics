from typing import List
from fastapi import APIRouter, HTTPException
from ..models.customer import Customer
from ..services.customer_service import CustomerService

router = APIRouter()

customer_service = CustomerService()

@router.post("/customers", response_model=Customer)
async def create_customer(customer: Customer):
    return customer_service.create_customer(customer)

@router.get("/customers", response_model=List[Customer])
async def get_all_customers():
    return customer_service.get_all_customers()

@router.get("/customers/{customer_id}", response_model=Customer)
async def get_customer(customer_id: str):
    customer = customer_service.get_customer(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.put("/customers/{customer_id}", response_model=Customer)
async def update_customer(customer_id: str, customer: Customer):
    updated_customer = customer_service.update_customer(customer_id, customer)
    if not updated_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return updated_customer

@router.delete("/customers/{customer_id}", response_model=dict)
async def delete_customer(customer_id: str):
    if not customer_service.delete_customer(customer_id):
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"message": "Customer deleted successfully"}

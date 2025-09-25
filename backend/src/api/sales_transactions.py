from typing import List
from fastapi import APIRouter, HTTPException
from ..models.sales_transaction import SalesTransaction
from ..services.sales_transaction_service import SalesTransactionService

router = APIRouter()

sales_transaction_service = SalesTransactionService()

@router.post("/sales-transactions", response_model=SalesTransaction)
async def create_sales_transaction(sales_transaction: SalesTransaction):
    return sales_transaction_service.create_sales_transaction(sales_transaction)

@router.get("/sales-transactions", response_model=List[SalesTransaction])
async def get_all_sales_transactions():
    return sales_transaction_service.get_all_sales_transactions()

@router.get("/sales-transactions/{transaction_id}", response_model=SalesTransaction)
async def get_sales_transaction(transaction_id: str):
    transaction = sales_transaction_service.get_sales_transaction(transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Sales Transaction not found")
    return transaction

@router.put("/sales-transactions/{transaction_id}", response_model=SalesTransaction)
async def update_sales_transaction(transaction_id: str, sales_transaction: SalesTransaction):
    updated_transaction = sales_transaction_service.update_sales_transaction(transaction_id, sales_transaction)
    if not updated_transaction:
        raise HTTPException(status_code=404, detail="Sales Transaction not found")
    return updated_transaction

@router.delete("/sales-transactions/{transaction_id}", response_model=dict)
async def delete_sales_transaction(transaction_id: str):
    if not sales_transaction_service.delete_sales_transaction(transaction_id):
        raise HTTPException(status_code=404, detail="Sales Transaction not found")
    return {"message": "Sales Transaction deleted successfully"}

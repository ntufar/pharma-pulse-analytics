from typing import List
from fastapi import APIRouter, HTTPException
from ..models.product import Product
from ..services.product_service import ProductService

router = APIRouter()

product_service = ProductService()

@router.post("/products", response_model=Product)
async def create_product(product: Product):
    return product_service.create_product(product)

@router.get("/products", response_model=List[Product])
async def get_all_products():
    return product_service.get_all_products()

@router.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: str):
    product = product_service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: str, product: Product):
    updated_product = product_service.update_product(product_id, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@router.delete("/products/{product_id}", response_model=dict)
async def delete_product(product_id: str):
    if not product_service.delete_product(product_id):
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}

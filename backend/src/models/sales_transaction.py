from pydantic import BaseModel, Field
from datetime import datetime

class SalesTransaction(BaseModel):
    id: str = Field(..., description="Unique identifier for the sales transaction")
    product_id: str = Field(..., description="ID of the product sold")
    customer_id: str = Field(..., description="ID of the customer who made the purchase")
    territory_id: str = Field(..., description="ID of the sales territory")
    transaction_date: datetime = Field(..., description="Date and time of the transaction")
    quantity: int = Field(..., gt=0, description="Quantity of the product sold")
    price_per_unit: float = Field(..., gt=0, description="Price per unit of the product")
    total_amount: float = Field(..., gt=0, description="Total amount of the transaction")

    class Config:
        schema_extra = {
            "example": {
                "id": "st_001",
                "product_id": "prod_001",
                "customer_id": "cust_001",
                "territory_id": "terr_001",
                "transaction_date": "2025-09-25T10:00:00Z",
                "quantity": 2,
                "price_per_unit": 25.50,
                "total_amount": 51.00,
            }
        }

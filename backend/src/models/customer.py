from pydantic import BaseModel, Field

class Customer(BaseModel):
    id: str = Field(..., description="Unique identifier for the customer")
    name: str = Field(..., description="Name of the customer")
    address: str = Field(..., description="Address of the customer")
    city: str = Field(..., description="City of the customer")
    state: str = Field(..., description="State of the customer")
    zip_code: str = Field(..., description="Zip code of the customer")

    class Config:
        schema_extra = {
            "example": {
                "id": "cust_001",
                "name": "John Doe",
                "address": "123 Main St",
                "city": "Anytown",
                "state": "CA",
                "zip_code": "90210",
            }
        }

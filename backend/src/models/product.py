from pydantic import BaseModel, Field

class Product(BaseModel):
    id: str = Field(..., description="Unique identifier for the product")
    name: str = Field(..., description="Name of the product")
    category: str = Field(..., description="Category of the product")
    manufacturer: str = Field(..., description="Manufacturer of the product")
    unit_cost: float = Field(..., gt=0, description="Cost per unit of the product")

    class Config:
        schema_extra = {
            "example": {
                "id": "prod_001",
                "name": "Product A",
                "category": "Category X",
                "manufacturer": "Manufacturer Y",
                "unit_cost": 15.75,
            }
        }

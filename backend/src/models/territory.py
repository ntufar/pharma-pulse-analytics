from pydantic import BaseModel, Field

class Territory(BaseModel):
    id: str = Field(..., description="Unique identifier for the territory")
    name: str = Field(..., description="Name of the territory")
    region: str = Field(..., description="Geographical region of the territory")

    class Config:
        schema_extra = {
            "example": {
                "id": "terr_001",
                "name": "North East",
                "region": "East",
            }
        }

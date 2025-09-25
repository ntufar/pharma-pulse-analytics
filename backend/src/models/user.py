from pydantic import BaseModel, Field

class User(BaseModel):
    id: str = Field(..., description="Unique identifier for the user")
    username: str = Field(..., description="Username of the user")
    email: str = Field(..., description="Email of the user")
    role: str = Field(..., description="Role of the user (e.g., admin, sales, viewer)")

    class Config:
        schema_extra = {
            "example": {
                "id": "user_001",
                "username": "johndoe",
                "email": "john.doe@example.com",
                "role": "sales",
            }
        }

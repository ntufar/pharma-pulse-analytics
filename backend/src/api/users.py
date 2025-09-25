from typing import List
from fastapi import APIRouter, HTTPException
from ..models.user import User
from ..services.user_service import UserService

router = APIRouter()

user_service = UserService()

@router.post("/users", response_model=User)
async def create_user(user: User):
    return user_service.create_user(user)

@router.get("/users", response_model=List[User])
async def get_all_users():
    return user_service.get_all_users()

@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: str):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: str, user: User):
    updated_user = user_service.update_user(user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: str):
    if not user_service.delete_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

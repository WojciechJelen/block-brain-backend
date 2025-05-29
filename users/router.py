from fastapi import APIRouter, Depends
from backend.auth.supabase_auth import get_current_user
from typing import Dict

user_router = APIRouter(prefix="/users")

@user_router.get("/me")
async def get_me(user: Dict = Depends(get_current_user)):
    return user

@user_router.get("/{user_id}")
async def get_user(user_id: int):
    return {"user_id": f"{user_id}"}


from fastapi import APIRouter   

user_router = APIRouter(prefix="/users")

@user_router.get("/{user_id}")
async def get_user(user_id: int):
    return {"user_id": f"{user_id}"}


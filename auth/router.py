from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth")  

@auth_router.post("/login")
async def login():
    return {"message": "Login successful"}
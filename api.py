from fastapi import FastAPI
from enum import Enum
from contextlib import asynccontextmanager 
from backend.users.router import user_router 
from backend.auth.router import auth_router

@asynccontextmanager
async def lifespan(app: FastAPI): 
    print("Starting up FastAPI application")
    yield
    print("Shutting down FastAPI application")

app = FastAPI(lifespan=lifespan) 
app.include_router(user_router)  
app.include_router(auth_router)



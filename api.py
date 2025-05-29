from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # Your Next.js frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)  
app.include_router(auth_router)



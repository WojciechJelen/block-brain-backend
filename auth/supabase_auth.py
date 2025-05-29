from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from backend.services.supabase import supabase
from typing import Dict

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> Dict:
    """
    Verify token using Supabase SDK
    """
    token = credentials.credentials

    user = supabase.auth.get_user(token)
    
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user.user

from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from backend.services.supabase import supabase
from typing import Dict, Optional

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> Dict:
    """
    Verify token using Supabase SDK and return user data
    """
    token = credentials.credentials
    
    try:
        # Use Supabase to verify the token
        user_response = supabase.auth.get_user(token)
        
        if not user_response.user:
            raise HTTPException(status_code=401, detail="Invalid token")
            
        return {
            "user_id": user_response.user.id,
            "email": user_response.user.email,
            "user_metadata": user_response.user.user_metadata,
            "app_metadata": user_response.user.app_metadata
        }
        
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Authentication failed: {str(e)}")

def get_optional_user(credentials: Optional[HTTPAuthorizationCredentials] = Depends(HTTPBearer(auto_error=False))) -> Optional[Dict]:
    """
    Get user data if token is provided, otherwise return None
    """
    if not credentials:
        return None
    
    try:
        return get_current_user(credentials)
    except:
        return None

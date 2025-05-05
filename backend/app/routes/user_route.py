# backend/app/routes/user.py

# from fastapi import APIRouter

# router = APIRouter()

# @router.get("/profile")
# def get_profile():
#     return {"message": "This is the user profile route"}
from fastapi import APIRouter, Header, HTTPException
from app.utils.token_utils import verify_login_token

router = APIRouter()

@router.get("/profile")
def get_profile(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid Authorization header")
    
    token = authorization.split(" ")[1]

    try:
        email = verify_login_token(token)
        return {"message": f"This is {email}'s profile"}
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

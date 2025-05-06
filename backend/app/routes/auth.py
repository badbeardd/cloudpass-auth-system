from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
from app.utils.token_utils import generate_login_token, verify_login_token
from app.utils.url_utils import generate_magic_link
from app.services.email_service import send_magic_link_email
from app.database import SessionLocal
from app.services.user_service import get_or_create_user
# from ..utils.token_utils import generate_login_token, verify_login_token
# from ..utils.url_utils import generate_magic_link
# from ..services.email_service import send_magic_link_email
# from ..services.user_service import get_or_create_user
# from ..database import SessionLocal
from fastapi import APIRouter, Request, HTTPException
import os
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")

router = APIRouter()

class LoginRequest(BaseModel):
    email: str

@router.post("/magic-link")
async def send_magic_link(req: LoginRequest):
    token = generate_login_token(req.email)
    magic_link = generate_magic_link(token)

    print(f"[DEBUG] Generated magic link: {magic_link}")

    sent = send_magic_link_email(req.email, magic_link)

    if not sent:
        raise HTTPException(status_code=500, detail="Failed to send email")

    return {"message": f"✅ Magic link sent to {req.email}"}

@router.get("/verify")
def verify_magic_link(token: str, request: Request):
    try:
        email = verify_login_token(token)
        print(f"✅ Verified login for: {email}")
        # Save user to DB if not exists
        db = SessionLocal()
        get_or_create_user(db, email)
        # Redirect to frontend (correct port)
        #return RedirectResponse(url=f"http://localhost:5173/dashboard?email={email}")
        #return RedirectResponse(url=f"http://localhost:5173/dashboard?email={email}&token={token}")
        return RedirectResponse(url=f"{FRONTEND_URL}/dashboard?email={email}&token={token}")
    except Exception as e:
        print(f"❌ Verification failed: {e}")
        raise HTTPException(status_code=401, detail="Invalid or expired token")

# ========================
# ✅ GITHUB OAUTH FLOW
# ========================

from app.services.oauth_service import (
    get_github_auth_url,
    exchange_github_code_for_token,
    get_github_user_info
)

@router.get("/oauth/github")
def github_login():
    return {"url": get_github_auth_url()}

@router.get("/github/callback")
def github_callback(code: str):
    token_data = exchange_github_code_for_token(code)
    access_token = token_data.get("access_token")

    if not access_token:
        raise HTTPException(status_code=400, detail="Invalid token exchange")

    user_info = get_github_user_info(access_token)

    email = user_info.get("email")
    if not email:
        # fallback if GitHub hides user email
        email = f"{user_info.get('login')}@github"

    db = SessionLocal()
    get_or_create_user(db, email)

    token = generate_login_token(email)
    return RedirectResponse(f"http://localhost:5173/dashboard?email={email}&token={token}")

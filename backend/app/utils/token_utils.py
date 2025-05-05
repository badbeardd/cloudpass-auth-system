import jwt
from datetime import datetime, timedelta
from app.config import JWT_SECRET

def generate_login_token(email: str) -> str:
    payload = {
        "sub": email,
        "exp": datetime.utcnow() + timedelta(minutes=10),
        "iat": datetime.utcnow()
    }
    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")

def verify_login_token(token: str) -> str:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return payload["sub"]  # ✅ FIXED: matches the key used during encoding
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Magic link expired, please request a new one.")

    except jwt.InvalidTokenError:
        raise Exception("Invalid token")

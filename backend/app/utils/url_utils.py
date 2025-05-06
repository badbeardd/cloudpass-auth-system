import os
from urllib.parse import urlencode

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

def generate_magic_link(token: str) -> str:
    return f"{BACKEND_URL}/auth/verify?{urlencode({'token': token})}"

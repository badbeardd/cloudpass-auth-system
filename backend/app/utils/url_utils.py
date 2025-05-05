from urllib.parse import urlencode

def generate_magic_link(token: str) -> str:
    base_url = "http://localhost:8000/auth/verify"
    return f"{base_url}?{urlencode({'token': token})}"

# backend/app/services/oauth_service.py

import requests
import os
from urllib.parse import urlencode

GITHUB_AUTH_URL = "https://github.com/login/oauth/authorize"
GITHUB_TOKEN_URL = "https://github.com/login/oauth/access_token"
GITHUB_USER_API = "https://api.github.com/user"

def get_github_auth_url():
    params = {
        "client_id": os.getenv("GITHUB_CLIENT_ID"),
        "redirect_uri": os.getenv("GITHUB_CALLBACK_URL"),
        "scope": "read:user user:email",
    }
    return f"{GITHUB_AUTH_URL}?{urlencode(params)}"

def exchange_github_code_for_token(code: str):
    data = {
        "client_id": os.getenv("GITHUB_CLIENT_ID"),
        "client_secret": os.getenv("GITHUB_CLIENT_SECRET"),
        "code": code,
        "redirect_uri": os.getenv("GITHUB_CALLBACK_URL"),
    }
    headers = {"Accept": "application/json"}
    response = requests.post(GITHUB_TOKEN_URL, data=data, headers=headers)
    return response.json()

def get_github_user_info(access_token: str):
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(GITHUB_USER_API, headers=headers)
    return response.json()

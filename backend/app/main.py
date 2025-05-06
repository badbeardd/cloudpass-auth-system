# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from app.routes import auth, user_route
# from app.database import Base, engine
# from app.models import user
from routes import auth, user_route
from database import Base, engine
from models import user
Base.metadata.create_all(bind=engine)
# Create FastAPI app
app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(auth.router, prefix="/auth")
app.include_router(user_route.router, prefix="/user")
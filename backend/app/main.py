# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#local run
from app.routes import auth, user_route
from app.database import Base, engine
from app.models import user
#for render
# from .routes import auth, user_route
# from .database import Base, engine
# from models import user

Base.metadata.create_all(bind=engine)
# Create FastAPI app
app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://cloudpass-frontend.onrender.com"],  # your exact frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(auth.router, prefix="/auth")
app.include_router(user_route.router, prefix="/user")

@app.get("/")
def root():
    return {"message": "CloudPass Auth Backend is running"}
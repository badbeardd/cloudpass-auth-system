# backend/app/services/user_service.py

from sqlalchemy.orm import Session
from app.models.user import User

def get_or_create_user(db: Session, email: str) -> User:
    user = db.query(User).filter(User.email == email).first()
    if user:
        return user
    user = User(email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

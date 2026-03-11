
from fastapi import HTTPException
from pytest import Session

from app.repository.user_repository import UserRepository
from app.security.security import create_access_token, verify_password


class AuthService:
    
    def __init__(self, db: Session):
        self.repository = UserRepository(db)
        
    def login(self, email: str, password: str):
        user = self.repository.get_by_email(email)
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid Credentials!")
        
        token = create_access_token(str(user.id))
        return token        
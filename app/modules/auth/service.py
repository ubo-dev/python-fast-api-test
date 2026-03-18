from fastapi import HTTPException

from app.modules.user.repository import UserRepository
from app.security.security import create_access_token, verify_password
from sqlalchemy.ext.asyncio import AsyncSession


class AuthService:
    
    def __init__(self, db: AsyncSession):
        self.repository = UserRepository(db)
        
    def login(self, email: str, password: str):
        user = self.repository.get_by_email(email)
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid Credentials!")
        
        token = create_access_token(str(user.id))
        return token     
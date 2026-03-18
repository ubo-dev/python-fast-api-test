from fastapi import HTTPException

from app.modules.auth.shemas import AuthResponse, LoginRequest, RegisterRequest
from app.modules.user.repository import UserRepository
from app.security.security import create_access_token, verify_password
from sqlalchemy.ext.asyncio import AsyncSession


class AuthService:
    
    def __init__(self, db: AsyncSession):
        self.repository = UserRepository(db)
        
    def login(self, request: LoginRequest) -> AuthResponse:
        user = self.repository.get_by_email(request.email)
        if not user or not verify_password(request.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid Credentials!")
        
        token = create_access_token(str(user.id))
        
        auth_response = AuthResponse(
            access_token = token
        )
        
        return auth_response 
   
        
    def register(self, request: RegisterRequest) -> AuthResponse:
        pass
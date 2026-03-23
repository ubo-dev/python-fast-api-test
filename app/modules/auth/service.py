from fastapi import HTTPException

from app.modules.auth.shemas import AuthResponse, LoginRequest, RegisterRequest
from app.modules.user.models import User
from app.modules.user.repository import UserRepository
from app.modules.user.service import UserService
from app.modules.user.shemas import UserCreate
from app.security.security import create_access_token, verify_password, hash_password
from sqlalchemy.ext.asyncio import AsyncSession


class AuthService:
    
    def __init__(self, user_service: UserService):
        self.user_service = user_service
        
    async def login(self, request: LoginRequest) -> AuthResponse:
        user = await self.user_service.get_by_email(request.email)
        if not user or not verify_password(request.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid Credentials!")
        
        token = create_access_token(str(user.id))
        
        auth_response = AuthResponse(
            access_token = token
        )
        
        return auth_response 
   
        
    async def register(self, request: RegisterRequest) -> AuthResponse:

        user_create = UserCreate(
            email = request.email,
            name = request.name,
            password = request.password,
        )

        user = await self.user_service.create_user(user_create)

        token = create_access_token(str(user.id))

        auth_response = AuthResponse(
            access_token=token
        )

        return auth_response

    async def apple(self, request: RegisterRequest) -> AuthResponse:
        pass

    async def logout(self, request: LoginRequest) -> AuthResponse:
        pass

    async def refresh(self, request: LoginRequest) -> AuthResponse:
        pass
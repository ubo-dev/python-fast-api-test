
from fastapi import HTTPException
from pytest import Session

import asyncio

from app.models.user import User
from app.repository.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.security.security import hash_password

class UserService:
    
    def __init__(self, db: Session):
        self.repository = UserRepository(db)
        
    async def create_user(self, user_create: UserCreate):
        existing_user = await self.repository.get_by_email(user_create.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="This email already registered!")
        
        loop = asyncio.get_event_loop() # bu sekilde blocking olan hash_passwordu 
        hashed_passwd = await loop.run_in_executor(None, hash_password, user_create.password)
        
        user = User(
            email = user_create.email,
            hashed_password = hashed_passwd
        )
        
        return await self.repository.create(user)

import uuid
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import asyncio
from app.modules.user.models import User
from app.modules.user.repository import UserRepository
from app.modules.user.shemas import UserCreate
from app.security.security import hash_password

class UserService:
    
    def __init__(self, db: AsyncSession):
        self.repository = UserRepository(db)
        
    async def create_user(self, user_create: UserCreate):
        existing_user = await self.repository.get_by_email(user_create.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="This email already registered!")
        
        # bu sekilde blocking olan hash_passwordu farklı thread icinde calıstırarak
        # event loopu blocklamamıs oluyoruz
        hashed_passwd = await asyncio.to_thread(hash_password, user_create.password)
        
        user = User(
            email = user_create.email,
            hashed_password = hashed_passwd
        )
        
        return await self.repository.create(user)
    
    async def get_by_id(self, id: uuid.UUID):
        existing_user = await self.repository.get_by_id(id)
        if existing_user is None:
            raise HTTPException(status_code=404, detail="No user found with given id.")
        
        return existing_user;
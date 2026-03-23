from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

import uuid

from app.modules.user.models import User

class UserRepository:
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_by_email(self, email: str) -> User | None:
        result = await self.db.execute(
            select(User).where(User.email == email) # sqli böyle yazıyoruz model ile 
        )
        return result.scalar_one_or_none() # return or null gibi yapi
    
    async def get_by_id(self, user_id: uuid.UUID) -> User | None:
        result = await self.db.execute(
            select(User).where(User.id == user_id)
        )
        return result.scalar_one_or_none()
    
    async def create(self, user: User) -> User | None:
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh()
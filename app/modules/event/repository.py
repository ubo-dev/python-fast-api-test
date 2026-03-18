from asyncio import Event
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

import uuid

class EventRepository:
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_by_id(self, id: uuid) -> Event | None:
        result = await self.db.execute(
            select(Event).where(Event.id == id)
        )
        return result.scalar_one_or_none()
    
    async def create(self, event: Event) -> Event:
        self.db.add(event)
        await self.db.commit()
        await self.db.refresh()
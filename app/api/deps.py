
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator
from app.db.session import SessionLocal
from app.modules.auth.service import AuthService
from app.modules.event.service import EventService
from app.modules.user.service import UserService

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as db:
        yield db  # ✅ auto closes, no need for try/finally

def get_user_service(
    db: AsyncSession = Depends(get_db)
) -> UserService:
    return UserService(db)

def get_auth_service(
    db: AsyncSession = Depends(get_db)
) -> AuthService:
    return AuthService(db)

def get_user_service(
    db: AsyncSession = Depends(get_db)
) -> UserService:
    return UserService(db)

def get_event_service(
    db: AsyncSession = Depends(get_db)
) -> EventService:
    return EventService(db)
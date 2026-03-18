
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator
from app.db.session import SessionLocal
from app.modules.auth.service import AuthService
from app.modules.event.service import EventService
from app.modules.photo.service import PhotoService
from app.modules.qr.service import QRService
from app.modules.user.service import UserService

async def get_async_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as db:
        yield db  # auto closes, no need for try/finally

def get_user_service(
    db: AsyncSession = Depends(get_async_db_session)
) -> UserService:
    return UserService(db)

def get_auth_service(
    db: AsyncSession = Depends(get_async_db_session)
) -> AuthService:
    return AuthService(db)

def get_qr_service(
    db: AsyncSession = Depends(get_async_db_session)
) -> QRService:
    return QRService(db)

def get_photo_service(
    db: AsyncSession = Depends(get_async_db_session)
) -> PhotoService:
    return PhotoService(db)

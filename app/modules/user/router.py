from io import BytesIO
from typing import Annotated
import uuid
import qrcode
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db, get_user_service
from app.modules.user.service import UserService
from app.modules.user.shemas import UserCreate, UserRead

router = APIRouter()

UserServiceDep = Annotated[UserService, Depends(get_user_service())]

@router.post("/")
async def create_user(
        user_in: UserCreate, 
        service: UserServiceDep
    ) -> UserRead:
    return await service.create_user(user_in)


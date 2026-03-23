from typing import Annotated
import uuid
from fastapi import APIRouter, Depends
from app.api.deps import get_user_service
from app.modules.user.service import UserService
from app.modules.user.shemas import UserCreate, UserRead, UserDailyRequestResponse

router = APIRouter()

UserServiceDep = Annotated[UserService, Depends(get_user_service)]

@router.post("/")
async def create_user(
        user_in: UserCreate, 
        service: UserServiceDep
    ) -> UserRead:
    return await service.create_user(user_in)


@router.get("/daily_request_count/{user_id}")
async def daily_request_count(
        user_id: uuid.UUID,
        service: UserServiceDep
) -> UserDailyRequestResponse:
    return await service.get_user_daily_request_count(user_id)


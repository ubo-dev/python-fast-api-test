from typing import Annotated
from fastapi import APIRouter, Depends

from app.api.deps import get_user_service
from app.modules.event.shemas import CreateEventRequest
from app.modules.user.service import UserService


router = APIRouter()

UserServiceDep = Annotated[UserService, Depends(get_user_service)]

router.post(
    path="/create"
)
async def create_event(
        request: CreateEventRequest,
        user_service: UserServiceDep
    ):
    existing_user = user_service.get_by_id(request.owner_user_id)
    pass

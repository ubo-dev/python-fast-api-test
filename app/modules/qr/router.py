
from io import BytesIO
import uuid
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
import qrcode
from app.api.deps import get_event_service, get_user_service
from app.modules.event.service import EventService
from app.modules.user.service import UserService
from typing import Annotated

router = APIRouter()

UserServiceDep = Annotated[UserService, Depends(get_user_service)]
EventServiceDep = Annotated[EventService, Depends(get_event_service)]

@router.post("/create_qr_code")
def create_qr_code(
    user_id: uuid.UUID, 
    user_service: UserServiceDep
) -> StreamingResponse:
    
    user = user_service.get_by_id(user_id)
    
    qr = qrcode.make(str(user.id))
    
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)
    
    return StreamingResponse(buffer, media_type="image/png")
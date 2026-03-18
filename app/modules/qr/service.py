from io import BytesIO
import uuid
from fastapi import Depends
from fastapi.responses import StreamingResponse
import qrcode
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.modules.event.service import EventService

class QRService:
    
    def __init__(self):
        pass
    
    async def create_qr_code(
        event_id: uuid.UUID,
        event_service: EventService 
    ) -> StreamingResponse:
    
        event = event_service.get_by_id(event_id)
        
        qr = qrcode.make(event.id)
        buffer = BytesIO(qr, format="PNG")
        buffer.seek(0)
        
        return StreamingResponse(buffer, media_type="image/png")
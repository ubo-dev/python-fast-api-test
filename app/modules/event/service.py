from asyncio import Event
import uuid
from fastapi import HTTPException

from app.modules.event.repository import EventRepository
from app.modules.event.shemas import CreateEventRequest, EventJoinRequest
from app.modules.participant.service import ParticipantService
from app.modules.user.service import UserService

class EventService:
    
    def __init__(self, repository: EventRepository, user_service: UserService, participant_service: ParticipantService):
        self.repository = repository
        self.user_service = user_service
        self.participant_service = participant_service
    
    async def get_by_id(self, id: uuid.UUID) -> Event:
        existing_event = await self.repository.get_by_id(id)
        if existing_event is None:
            raise HTTPException(status_code=404, detail="No event found with given id!")
        
        return existing_event
    
    async def join(self, join_request: EventJoinRequest) -> None:
        existing_event = await self.get_by_id(join_request.event_id)
        invited_user = await self.user_service.get_by_id(join_request.user_id)
        await self.participant_service.create(invited_user, existing_event)
        
    async def create(self, create_request: CreateEventRequest) -> Event:
        invited_user = await self.user_service.get_by_id(create_request.user_id)
        pass
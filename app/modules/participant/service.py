from asyncio import Event
from datetime import time
from app.modules.participant.models import Participant, ParticipantRole
from app.modules.participant.repository import ParticipantRepository
from app.modules.user.models import User


class ParticipantService:
    
    def __init__(self, repository: ParticipantRepository):
        self.repository = repository

    def create(self, invited_user: User, existing_event: Event) -> Participant:
        
        participant = Participant(
            user_id = invited_user.id,
            event_id = existing_event.id,
            role = ParticipantRole.MEMBER,
            joined_at = time.now()
        )
        
        return self.repository.create(participant);
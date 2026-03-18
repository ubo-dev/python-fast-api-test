from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.participant.models import Participant

class ParticipantRepository():
    
    def __init__(self, db: AsyncSession):
        self.db = db
        
    async def create(self, participant: Participant) -> Participant:
        self.db.add(participant)
        await self.db.commit()
        await self.db.refresh()
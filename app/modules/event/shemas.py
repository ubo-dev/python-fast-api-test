import uuid

from pydantic import BaseModel


class EventJoinRequest(BaseModel):
    event_id: uuid.UUID
    user_id: uuid.UUID
    invide_code: str  
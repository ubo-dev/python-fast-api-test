import uuid
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserDailyRequestResponse:
    def __init__(self, user_id: uuid.UUID, remaining_request_count: int) -> None:
        self.user_id = user_id
        self.remaining_request_count = remaining_request_count

    user_id: uuid.UUID
    remaining_request_count: int

class UserRead(UserBase):
    id: uuid.UUID

    model_config = {
        "from_attributes": True
    }
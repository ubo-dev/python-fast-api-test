import uuid
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr
    has_advertisement_perm: bool
    gender: int

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: uuid.UUID

    model_config = {
        "from_attributes": True
    }
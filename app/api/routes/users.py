from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.user import UserCreate, UserRead
from app.service.user_service import UserService

router = APIRouter()

@router.post("/", response_model=UserRead)
async def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return await service.create_user(user_in)
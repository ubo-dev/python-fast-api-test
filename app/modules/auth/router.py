from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_auth_service, get_db
from app.modules.auth.service import AuthService
from app.modules.auth.shemas import LoginRequest, LoginResponse


router = APIRouter()

AuthServiceDep = Annotated[AuthService, Depends(get_auth_service)]

@router.post("/login")
def login(
        request: LoginRequest, 
        service: AuthServiceDep
    ) -> LoginResponse:
    token = service.login(request)
    return {"access_token": token} 
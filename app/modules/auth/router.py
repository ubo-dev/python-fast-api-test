from typing import Annotated
from fastapi import APIRouter, Depends
from app.api.deps import get_auth_service
from app.modules.auth.service import AuthService
from app.modules.auth.shemas import LoginRequest, AuthResponse, RegisterRequest


router = APIRouter()

AuthServiceDep = Annotated[AuthService, Depends(get_auth_service)]

@router.post("/login")
def login(
        request: LoginRequest, 
        service: AuthServiceDep
    ) -> AuthResponse:
    return service.login(request) 

@router.post("/register")
def register(
        request: RegisterRequest,
        service: AuthServiceDep
) -> AuthResponse:
    return service.register(request)

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from app.modules.user.service import UserService


class AuthJwtMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        token = request.headers.get("Authorization")
        if not token:
            return await call_next(request)


        user = await UserService().get_by_token(token)
        if not user:
            return await call_next(request)

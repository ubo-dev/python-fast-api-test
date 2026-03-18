from fastapi import FastAPI

from app.modules.auth.router import router as auth_router
from app.modules.user.router import router as user_router

app = FastAPI(title="Task Manager API")

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(user_router, prefix="/user", tags=["user"])
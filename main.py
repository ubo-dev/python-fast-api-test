from fastapi import FastAPI
from app.api.routes import users, auth

app = FastAPI(title="Task Manager API")

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
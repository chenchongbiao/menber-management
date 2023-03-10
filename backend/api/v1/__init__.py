from fastapi import APIRouter
from .endpoints import admin, login, user, menu

v1 = APIRouter(prefix="/v1")

v1.include_router(admin)
v1.include_router(login)
v1.include_router(user)
v1.include_router(menu)
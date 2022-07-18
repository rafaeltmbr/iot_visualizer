from fastapi import APIRouter

from .device_routes import device_router
from .attribute_routes import attribute_router

user_router = APIRouter(prefix='/user')

user_router.include_router(device_router)
user_router.include_router(attribute_router)
from fastapi import APIRouter

from .reading_routes import reading_router

device_router = APIRouter(prefix='/device')

device_router.include_router(reading_router)
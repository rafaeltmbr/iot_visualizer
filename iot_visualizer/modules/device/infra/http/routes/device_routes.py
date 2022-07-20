from fastapi import APIRouter, Depends

from .reading_routes import reading_router
from ....infra.http.dependecies.device_auth import device_auth


device_router = APIRouter(prefix='/device', dependencies=[Depends(device_auth)])

device_router.include_router(reading_router)
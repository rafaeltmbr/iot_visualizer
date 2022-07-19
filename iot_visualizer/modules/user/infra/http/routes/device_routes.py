from uuid import UUID
from fastapi import APIRouter, Request, Response

from ..controllers.DeviceController import DeviceController

device_router = APIRouter(prefix='/device')

@device_router.get('/{id}')
async def show_device(req: Request, res: Response, id: UUID):
    return await DeviceController.show(req, res, id)
from uuid import UUID
from fastapi import APIRouter, Request, Response

from ..controllers.DeviceController import DeviceController
from ..schemas.device.CreateDeviceSchema import CreateDeviceSchema
from ..schemas.device.UpdateDeviceSchema import UpdateDeviceSchema


device_router = APIRouter(prefix='/device')

@device_router.get('')
async def list_devices(req: Request, res: Response):
    return await DeviceController.list(req, res)

@device_router.get('/{id}')
async def show_device(req: Request, res: Response, id: UUID):
    return await DeviceController.show(req, res, id)

@device_router.post('')
async def create_device(req: Request, res: Response, data: CreateDeviceSchema):
    return await DeviceController.create(req, res, data)

@device_router.patch('/{id}')
async def update_device(req: Request, res: Response, id: UUID, data: UpdateDeviceSchema):
    return await DeviceController.update(req, res, id, data)

@device_router.delete('/{id}')
async def delete_device(req: Request, res: Response, id: UUID):
    return await DeviceController.delete(req, res, id)
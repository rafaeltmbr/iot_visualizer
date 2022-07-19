from fastapi import Request, Response

from .....user.services.device.ShowDeviceService import ShowDeviceService
from .....device.infra.sqlalchemy.repositories.DeviceRepository import DeviceRepository

class DeviceController:
    async def show(req: Request, res: Response, id: str):
        showDeviceService = ShowDeviceService(DeviceRepository())
        device = await showDeviceService.execute(id)

        return device

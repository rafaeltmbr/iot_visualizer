from fastapi import Request, Response
from iot_visualizer.modules.user.services.device.ShowDeviceService import ShowDeviceService


class DeviceController:
    async def show(req: Request, res: Response, id: str):
        showDeviceService = ShowDeviceService()
        device = await showDeviceService.execute(id)

        return device

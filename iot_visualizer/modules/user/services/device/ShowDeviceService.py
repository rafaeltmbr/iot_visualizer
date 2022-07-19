from http.client import HTTPException
from iot_visualizer.modules.device.infra.sqlalchemy.repositories.DeviceRepository import DeviceRepository


class ShowDeviceService:
    def __init__(self, device_repository: DeviceRepository):
        self.device_repository = device_repository

    async def execute(self, id):
        user = self.device_repository.show(id)

        if not user:
            raise Exception('Device not found')

        return user
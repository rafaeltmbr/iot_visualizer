from ....device.repositories.IDeviceRepository import IDeviceRepository

class ListDevicesService():
    def __init__(self, device_repository: IDeviceRepository):
        self.device_repository = device_repository

    async def execute(self):
        return self.device_repository.list()
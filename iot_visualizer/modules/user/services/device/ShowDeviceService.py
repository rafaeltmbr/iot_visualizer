from ....shared.utils.AppError import AppError, ErrorType
from .....modules.device.infra.sqlalchemy.repositories.DeviceRepository import DeviceRepository


class ShowDeviceService:
    def __init__(self, device_repository: DeviceRepository):
        self.device_repository = device_repository

    async def execute(self, id):
        user = self.device_repository.show(id)

        if not user:
            raise AppError(ErrorType.DEVICE_NOT_FOUND)

        return user
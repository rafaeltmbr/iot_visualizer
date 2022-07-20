from uuid import UUID

from ....device.repositories.IDeviceRepository import IDeviceRepository
from ....shared.utils.AppError import AppError, ErrorType

class DeleteDeviceService():
    def __init__(self, device_repository: IDeviceRepository):
        self.device_repository = device_repository

    async def execute(self, id: UUID):
        device = self.device_repository.find_by_id(id)

        if not device:
            raise AppError(ErrorType.DEVICE_NOT_FOUND)

        self.device_repository.delete(device)
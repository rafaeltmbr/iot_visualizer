from ....shared.utils.AppError import AppError, AppErrors
from ....device.repositories.IDeviceRepository import IDeviceRepository

class ShowDeviceService:
    def __init__(self, device_repository: IDeviceRepository):
        self.device_repository = device_repository

    async def execute(self, id):
        device = self.device_repository.find_by_id_with_relations(id)

        if not device:
            raise AppError(AppErrors.DEVICE_NOT_FOUND)

        return device
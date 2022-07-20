from uuid import UUID
from ....device.repositories.IDeviceRepository import IDeviceRepository
from ....device.dto.UpdateDeviceDTO import UpdateDeviceDTO
from ....shared.utils.AppError import AppError, ErrorType
from ....shared.utils.update_instance_attributes import update_instance_attributes

class UpdateDeviceService:
    def __init__(self, device_repository: IDeviceRepository):
        self.device_repository = device_repository

    async def execute(self, id: UUID, data: UpdateDeviceDTO):
        device = self.device_repository.find_by_id(id)

        if not device:
            raise AppError(ErrorType.DEVICE_NOT_FOUND)

        if data.name and data.name != device.name and self.device_repository.find_by_name(data.name):
            raise AppError(ErrorType.DUPLICATED_DEVICE_NAME)

        update_instance_attributes(device, data, True)

        return self.device_repository.update(device)

from ....device.repositories.IDeviceRepository import IDeviceRepository
from ....device.dto.UpdateDeviceDTO import UpdateDeviceDTO
from ....shared.utils.AppError import AppError, ErrorType
from ....shared.utils.update_instance_attributes import update_instance_attributes

class UpdateDeviceService:
    def __init__(self, device_repository: IDeviceRepository):
        self.device_repository = device_repository

    async def execute(self, id: str, data: UpdateDeviceDTO):
        device = self.device_repository.find_by_id(id)

        if not device:
            raise AppError(ErrorType.DEVICE_NOT_FOUND)

        update_instance_attributes(device, data, True)

        return self.device_repository.update(device)

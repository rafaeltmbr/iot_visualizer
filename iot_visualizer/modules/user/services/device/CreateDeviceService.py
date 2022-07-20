from ....device.dto.CreateDeviceDTO import CreateDeviceDTO
from ....device.repositories.IDeviceRepository import IDeviceRepository
from ....device.infra.sqlalchemy.models.Device import Device
from ....shared.utils.AppError import AppError, ErrorType


class CreateDeviceService:
    def __init__(self, device_repository: IDeviceRepository):
        self.device_repository = device_repository

    async def execute(self, data: CreateDeviceDTO) -> Device:
        if self.device_repository.find_by_name(data.name):
            raise AppError(ErrorType.DUPLICATED_DEVICE_NAME)

        return self.device_repository.create(data)
        
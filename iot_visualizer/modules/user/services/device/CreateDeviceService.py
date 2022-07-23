from ....device.dto.device.CreateDeviceDTO import CreateDeviceDTO
from ....device.repositories.IDeviceRepository import IDeviceRepository
from ....device.infra.sqlalchemy.models.Device import Device
from ....shared.utils.AppError import AppError, AppErrors
from ....shared.providers.Token.DeviceSecret import DeviceSecret


class CreateDeviceService:
    def __init__(self, device_repository: IDeviceRepository):
        self.device_repository = device_repository

    async def execute(self, data: CreateDeviceDTO) -> Device:
        if self.device_repository.find_by_name(data.name):
            raise AppError(AppErrors.DUPLICATED_DEVICE_NAME)

        return self.device_repository.create(CreateDeviceDTO(
            name = data.name,
            description = data.description,
            secret = DeviceSecret.generate()
        ))
        
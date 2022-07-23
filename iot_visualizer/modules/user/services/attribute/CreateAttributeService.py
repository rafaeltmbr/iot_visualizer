from ....device.repositories.IAttributeRepository import IAttributeRepository
from ....device.repositories.IDeviceRepository import IDeviceRepository
from ....device.dto.attribute.CreateAttributeDTO import CreateAttributeDTO
from ....shared.utils.AppError import AppError, ErrorType


class CreateAttributeService:
    def __init__(self, attribute_repository: IAttributeRepository, device_repository: IDeviceRepository):
        self.attribute_repository = attribute_repository
        self.device_repository = device_repository


    async def execute(self, data: CreateAttributeDTO):
        if not self.device_repository.find_by_id(data.device_id):
            raise AppError(ErrorType.DEVICE_NOT_FOUND)

        if self.attribute_repository.find_by_name(data.name):
            raise AppError(ErrorType.DUPLICATED_ATTRIBUTE_NAME)

        if not getattr(data.config.formatting, data.type):
            raise ValueError(f'field "{data.type}" is required in the config.formatting object')
        
        return self.attribute_repository.create(data)

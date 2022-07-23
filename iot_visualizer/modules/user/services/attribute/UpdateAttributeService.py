from uuid import UUID

from ....device.dto.attribute.UpdateAttributeDTO import UpdateAttributeDTO
from ....device.repositories.IAttributeRepository import IAttributeRepository
from ....shared.utils.AppError import AppError, AppErrors
from ....shared.utils.update_instance_attributes import update_instance_attributes


class UpdateAttributeService:
    def __init__(self, attribute_repository: IAttributeRepository):
        self.attribute_repository = attribute_repository


    async def execute(self, id: UUID, data: UpdateAttributeDTO):
        attribute = self.attribute_repository.find_by_id(id)

        if not attribute:
            raise AppError(AppErrors.ATTRIBUTE_NOT_FOUND)

        if data.name and data.name != attribute.name and self.attribute_repository.find_by_name(data.name):
            raise AppError(AppErrors.DUPLICATED_ATTRIBUTE_NAME)

        update_instance_attributes(attribute, data, True)

        if not getattr(attribute.config.formatting, attribute.type.value):
            raise ValueError(f'field "{attribute.type.value}" is required in the config.formatting object')

        return self.attribute_repository.update(attribute)
        

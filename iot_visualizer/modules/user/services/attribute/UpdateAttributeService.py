from uuid import UUID

from ....device.dto.attribute.UpdateAttributeDTO import UpdateAttributeDTO
from ....device.repositories.IAttributeRepository import IAttributeRepository
from ....shared.utils.AppError import AppError, ErrorType
from ....shared.utils.update_instance_attributes import update_instance_attributes


class UpdateAttributeService:
    def __init__(self, attribute_repository: IAttributeRepository):
        self.attribute_repository = attribute_repository


    async def execute(self, id: UUID, data: UpdateAttributeDTO):
        attribute = self.attribute_repository.find_by_id(id)

        if not attribute:
            raise AppError(ErrorType.ATTRIBUTE_NOT_FOUND)

        if data.name and data.name != attribute.name and self.attribute_repository.find_by_name(data.name):
            raise AppError(ErrorType.DUPLICATED_ATTRIBUTE_NAME)

        update_instance_attributes(attribute, data, True)

        return self.attribute_repository.update(attribute)
        

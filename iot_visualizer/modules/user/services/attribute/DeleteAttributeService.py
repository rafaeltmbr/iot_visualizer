from uuid import UUID

from ....device.repositories.IAttributeRepository import IAttributeRepository
from ....shared.utils.AppError import AppError, ErrorType


class DeleteAttributeService:
    def __init__(self, attribute_repository: IAttributeRepository):
        self.attribute_repository = attribute_repository


    async def execute(self, id: UUID):
        attribute = self.attribute_repository.find_by_id(id)

        if not attribute:
            raise AppError(ErrorType.ATTRIBUTE_NOT_FOUND)

        self.attribute_repository.delete(attribute)

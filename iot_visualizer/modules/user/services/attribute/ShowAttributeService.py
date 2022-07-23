from uuid import UUID

from ....device.repositories.IAttributeRepository import IAttributeRepository
from ....shared.utils.AppError import AppError, AppErrors


class ShowAttributeService:
    def __init__(self, attribute_repository: IAttributeRepository):
        self.attribute_repository = attribute_repository


    async def execute(self, id: UUID):
        attribute = self.attribute_repository.find_by_id_with_relations(id)

        if not attribute:
            raise AppError(AppErrors.ATTRIBUTE_NOT_FOUND)

        return attribute

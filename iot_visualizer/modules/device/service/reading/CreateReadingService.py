
from ...utils.is_reading_value_valid import is_reading_value_valid
from ...repositories.IReadingRepository import IReadingRepository
from ...repositories.IAttributeRepository import IAttributeRepository
from ...dto.reading.CreateReadingDTO import CreateReadingDTO
from ....shared.utils.AppError import AppError, AppErrors


class CreateReadingService():
    def __init__(self, reading_repository: IReadingRepository, attribute_repository: IAttributeRepository):
        self.reading_repository = reading_repository
        self.attribute_repository = attribute_repository

    async def execute(self, data: CreateReadingDTO):
        attribute = self.attribute_repository.find_by_id(data.attribute_id)

        if not attribute:
            raise AppError(AppErrors.ATTRIBUTE_NOT_FOUND)

        if not is_reading_value_valid(data.value, attribute.type.value):
            raise AppError(AppErrors.INVALID_READING_VALUE)
        

        return self.reading_repository.create(data)
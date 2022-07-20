
from ...repositories.IReadingRepository import IReadingRepository
from ...repositories.IAttributeRepository import IAttributeRepository
from ...dto.reading.CreateReadingDTO import CreateReadingDTO
from ....shared.utils.AppError import AppError, ErrorType


class CreateReadingService():
    def __init__(self, reading_repository: IReadingRepository, attribute_repository: IAttributeRepository):
        self.reading_repository = reading_repository
        self.attribute_repository = attribute_repository

    async def execute(self, data: CreateReadingDTO):
        if not self.attribute_repository.find_by_id(data.attribute_id):
            raise AppError(ErrorType.ATTRIBUTE_NOT_FOUND)

        return self.reading_repository.create(data)
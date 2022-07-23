from fastapi import Request, Response

from ..schemas.CreateReadingSchema import CreateReadingSchema
from ...sqlalchemy.repositories.ReadingRepository import ReadingRepository
from ...sqlalchemy.repositories.AttributeRepository import AttributeRepository
from ...sqlalchemy.repositories.DeviceRepository import DeviceRepository
from ....service.reading.CreateReadingService import CreateReadingService
from ....dto.reading.CreateReadingDTO import CreateReadingDTO


class ReadingController:
    @staticmethod
    async def create(req: Request, res: Response, body: CreateReadingSchema):
        createReading = CreateReadingService(ReadingRepository(), AttributeRepository(), DeviceRepository())

        reading = await createReading.execute( CreateReadingDTO(
            attribute_id = body.attribute_id,
            value = body.value,
        ))

        return reading

from fastapi import Request, Response

from ..schemas.CreateReadingSchema import CreateReadingSchema
from ...sqlalchemy.repositories.ReadingRepository import ReadingRepository
from ...sqlalchemy.repositories.AttributeRepository import AttributeRepository
from ....service.reading.CreateReadingService import CreateReadingService
from ....dto.reading.CreateReadingDTO import CreateReadingDTO


class ReadingController:
    async def create(req: Request, res: Response, body: CreateReadingSchema):
        print('ENTERED')
        createReading = CreateReadingService(ReadingRepository(), AttributeRepository())
        print('ENTERED 2')
        reading = await createReading.execute( CreateReadingDTO(
            attribute_id = body.attribute_id,
            value = body.value,
        ))

        return reading

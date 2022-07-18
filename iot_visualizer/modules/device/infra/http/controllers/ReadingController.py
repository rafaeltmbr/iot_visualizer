from fastapi import Request, Response

from ..schemas.CreateReadingSchema import CreateReadingSchema
from ....service.reading.CreateReadingService import CreateReadingService

class ReadingController:
    async def create(req: Request, res: Response, body: CreateReadingSchema):
        createReading = CreateReadingService()
        reading = await createReading.execute(body)

        return reading

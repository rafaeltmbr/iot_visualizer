from fastapi import Request, Response, status

from ..schemas.CreateReadingSchema import CreateReadingsSchema
from ...sqlalchemy.models.Device import Device
from ...sqlalchemy.repositories.ReadingRepository import ReadingRepository
from ...sqlalchemy.repositories.DeviceRepository import DeviceRepository
from ....service.reading.CreateReadingsService import CreateReadingsService
from ....dto.reading.CreateReadingDTO import CreateReadingDTO


class ReadingController:
    @staticmethod
    async def create(req: Request, res: Response, body: CreateReadingsSchema):
        createReading = CreateReadingsService(ReadingRepository(), DeviceRepository())

        readings = [CreateReadingDTO(attribute_id = r.attribute_id, value = r.value) for r in body.readings]

        await createReading.execute(readings, req.device)

        res.status_code = status.HTTP_204_NO_CONTENT

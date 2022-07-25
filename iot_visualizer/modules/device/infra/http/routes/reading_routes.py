from fastapi import APIRouter, Request, Response

from ..schemas.CreateReadingSchema import CreateReadingsSchema
from ..controllers.ReadingController import ReadingController

reading_router = APIRouter(prefix='/reading')

@reading_router.post('', response_class=Response)
async def create_reading(req: Request, res: Response, body: CreateReadingsSchema):
    return await ReadingController.create(req, res, body)
from fastapi import APIRouter, Request, Response

from ..schemas.CreateReadingSchema import CreateReadingSchema
from ..controllers.ReadingController import ReadingController

reading_router = APIRouter(prefix='/reading')

@reading_router.post('')
async def create_reading(req: Request, res: Response, body: CreateReadingSchema):
    return await ReadingController.create(req, res, body)
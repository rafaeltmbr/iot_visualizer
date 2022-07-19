from uuid import UUID
from fastapi import APIRouter, Request, Response

from ..schemas.UpdateAttributeSchema import UpdateAttributeSchema
from ..schemas.CreateAttributeSchema import CreateAttributeSchema
from ..controllers.AttributeController import AttributeController

attribute_router = APIRouter(prefix='/attribute')


@attribute_router.post('')
async def create_attribute(req: Request, res: Response, body: CreateAttributeSchema):
    return await AttributeController.create(req, res, body)


@attribute_router.patch('/{id}')
async def update_attribute(req: Request, res: Response, id: UUID, body: UpdateAttributeSchema):
    return await AttributeController.update(req, res, id, body)


@attribute_router.delete('/{id}', response_class=Response)
async def remove_attribute(req: Request, res: Response, id: UUID):
    return await AttributeController.remove(req, res, id)
from uuid import UUID
from fastapi import APIRouter, Request, Response

from ..schemas.attribute.UpdateAttributeSchema import UpdateAttributeSchema
from ..schemas.attribute.CreateAttributeSchema import CreateAttributeSchema
from ..controllers.AttributeController import AttributeController

attribute_router = APIRouter(prefix='/attribute')


@attribute_router.get('')
async def list_attribute(req: Request, res: Response):
    return await AttributeController.list(req, res)


@attribute_router.get('/{id}')
async def show_attribute(req: Request, res: Response, id: UUID):
    return await AttributeController.show(req, res, id)


@attribute_router.post('')
async def create_attribute(req: Request, res: Response, body: CreateAttributeSchema):
    return await AttributeController.create(req, res, body)


@attribute_router.patch('/{id}')
async def update_attribute(req: Request, res: Response, id: UUID, body: UpdateAttributeSchema):
    return await AttributeController.update(req, res, id, body)


@attribute_router.delete('/{id}', response_class=Response)
async def delete_attribute(req: Request, res: Response, id: UUID):
    return await AttributeController.delete(req, res, id)
from fastapi import Request, Response, status

from iot_visualizer.modules.user.services.attribute.CreateAttributeService import CreateAttributeService
from iot_visualizer.modules.user.services.attribute.RemoveAttributeService import RemoveAttributeService
from iot_visualizer.modules.user.services.attribute.UpdateAttributeService import UpdateAttributeService

from ..schemas.attribute.CreateAttributeSchema import CreateAttributeSchema


class AttributeController:
    async def create(req: Request, res: Response, body: CreateAttributeSchema):
        createAttribute = CreateAttributeService()
        attribute = await createAttribute.execute(body)
        return attribute

    async def update(req: Request, res: Response, id: str, body: UpdateAttributeService) -> dict:
        updateAttribute = UpdateAttributeService()
        attribute = await updateAttribute.execute(id, body)
        return attribute

    async def remove(req: Request, res: Response, id: str) -> dict:
        removeAttribute = RemoveAttributeService()
        await removeAttribute.execute(id)
        res.status_code = status.HTTP_204_NO_CONTENT
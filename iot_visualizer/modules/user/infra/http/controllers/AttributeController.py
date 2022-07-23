from uuid import UUID
from fastapi import Request, Response, status


from ..schemas.attribute.CreateAttributeSchema import CreateAttributeSchema
from ..schemas.attribute.UpdateAttributeSchema import UpdateAttributeSchema
from ....services.attribute.ListAttributeService import ListAttributeService
from ....services.attribute.ShowAttributeService import ShowAttributeService
from ....services.attribute.CreateAttributeService import CreateAttributeService
from ....services.attribute.DeleteAttributeService import DeleteAttributeService
from ....services.attribute.UpdateAttributeService import UpdateAttributeService
from .....device.dto.attribute.CreateAttributeDTO import CreateAttributeDTO
from .....device.dto.attribute.UpdateAttributeDTO import UpdateAttributeDTO
from .....device.infra.sqlalchemy.repositories.AttributeRepository import AttributeRepository
from .....device.infra.sqlalchemy.repositories.DeviceRepository import DeviceRepository


class AttributeController:
    @staticmethod
    async def list(req: Request, res: Response):
        listAttributeService = ListAttributeService(AttributeRepository())
        attributes = await listAttributeService.execute()

        return { "results": attributes }


    @staticmethod
    async def show(req: Request, res: Response, id: UUID):
        showAttributeService = ShowAttributeService(AttributeRepository())
        attribute = await showAttributeService.execute(id)

        return attribute


    @staticmethod
    async def create(req: Request, res: Response, body: CreateAttributeSchema):
        createAttribute = CreateAttributeService(AttributeRepository(), DeviceRepository())
        attribute = await createAttribute.execute(CreateAttributeDTO(
            device_id = body.device_id,
            name = body.name,
            type = body.type,
            config = body.config
        ))

        return attribute


    @staticmethod
    async def update(req: Request, res: Response, id: UUID, body: UpdateAttributeSchema):
        updateAttribute = UpdateAttributeService(AttributeRepository())
        attribute = await updateAttribute.execute(id, UpdateAttributeDTO(
            name=body.name,
            config=body.config
        ))

        return attribute


    @staticmethod
    async def delete(req: Request, res: Response, id: UUID):
        deleteAttribute = DeleteAttributeService(AttributeRepository())
        await deleteAttribute.execute(id)

        return Response(status_code=status.HTTP_204_NO_CONTENT)
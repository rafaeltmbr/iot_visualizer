from uuid import UUID
from fastapi import Request, Response, status

from ....services.device.DeleteDeviceService import DeleteDeviceService
from ..schemas.device.UpdateDeviceSchema import UpdateDeviceSchema
from ..schemas.device.CreateDeviceSchema import CreateDeviceSchema
from ....services.device.UpdateDeviceService import UpdateDeviceService
from ....services.device.ListDevicesService import ListDevicesService
from ....services.device.CreateDeviceService import CreateDeviceService
from ....services.device.ShowDeviceService import ShowDeviceService
from .....device.infra.sqlalchemy.repositories.DeviceRepository import DeviceRepository
from .....device.dto.UpdateDeviceDTO import UpdateDeviceDTO



class DeviceController:
    async def list(req: Request, res: Response):
        listDevicesService = ListDevicesService(DeviceRepository())
        devices = await listDevicesService.execute()

        return { "results": devices }


    async def show(req: Request, res: Response, id: str):
        showDeviceService = ShowDeviceService(DeviceRepository())
        device = await showDeviceService.execute(id)

        return device


    async def create(req: Request, res: Response, data: CreateDeviceSchema):
        createDeviceService = CreateDeviceService(DeviceRepository())
        device = await createDeviceService.execute(data)

        return device


    async def update(req: Request, res: Response, id: UUID, data: UpdateDeviceSchema):
        updateDeviceService = UpdateDeviceService(DeviceRepository())

        device = await updateDeviceService.execute(id, UpdateDeviceDTO(
            name=data.name,
            description=data.description,
            token=data.token
        ))

        return device

    async def delete(req: Request, res: Response, id: UUID):
        removeDeviceService = DeleteDeviceService(DeviceRepository())
        await removeDeviceService.execute(id)

        return Response(status_code=status.HTTP_204_NO_CONTENT)


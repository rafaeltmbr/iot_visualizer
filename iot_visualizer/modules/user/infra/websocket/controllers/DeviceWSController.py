import json
from uuid import UUID
from fastapi import WebSocket
import asyncio

from .....device.infra.sqlalchemy.repositories.DeviceRepository import DeviceRepository
from .....device.infra.sqlalchemy.models.Device import Device
from .....device.service.reading.CreateReadingsService import CreateReadingsService
from .....shared.utils.AppError import AppError, AppErrors


class DeviceWSController:
    @staticmethod
    async def device_listener(websocket: WebSocket, id: UUID):
        client_connected = True
        device_json = ''

        def change_handler(device: Device):
            nonlocal device_json
            device_json = json.dumps(device.to_dict())

        try:
            await websocket.accept()

            device_repository = DeviceRepository()
            if not device_repository.find_by_id(id):
                raise AppError(AppErrors.DEVICE_NOT_FOUND)

            CreateReadingsService.add_listener(id, change_handler)

            while client_connected:
                await websocket.send_text(device_json)
                device_json = ''
                await asyncio.sleep(1)

        except:
            client_connected = False
            await websocket.close()
            CreateReadingsService.remove_listener(id, change_handler)
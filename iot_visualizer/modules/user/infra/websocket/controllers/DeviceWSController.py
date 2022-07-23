import json
from uuid import UUID
from fastapi import WebSocket
import asyncio

from .....device.infra.sqlalchemy.models.Device import Device
from .....device.service.reading.CreateReadingService import CreateReadingService


class DeviceWSController:
    @staticmethod
    async def reading_listener(websocket: WebSocket, id: UUID):
        client_connected = True
        device_json = ''

        def reading_listener(device: Device):
            nonlocal device_json
            device_json = json.dumps(device.to_dict())

        try:
            CreateReadingService.add_listener(reading_listener)

            await websocket.accept()

            while client_connected:
                await asyncio.sleep(1)
                await websocket.send_text(device_json)
                device_json = ''

        except Exception as e:
            client_connected = False
            CreateReadingService.remove_listener(reading_listener)
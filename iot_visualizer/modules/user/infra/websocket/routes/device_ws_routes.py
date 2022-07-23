from uuid import UUID
from fastapi import FastAPI, WebSocket

from ..controllers.DeviceWSController import DeviceWSController


def device_ws_routes(app: FastAPI, preffix: str):
    @app.websocket(f'{preffix}/device/{{id}}')
    async def reading_listener(websocket: WebSocket, id: UUID):
        await DeviceWSController.reading_listener(websocket, id)

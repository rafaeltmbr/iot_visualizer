from fastapi import FastAPI

from .device_ws_routes import device_ws_routes


def user_ws_routes(app: FastAPI, preffix: str):
    device_ws_routes(app, f'{preffix}/user')

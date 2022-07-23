from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

from .middlewares.exception_middleware import excepetion_middleware
from ..sqlalchemy.db_engine import db_engine
from ..sqlalchemy.models.Base import Base
from ....user.infra.http.routes.user_routes import user_router
from ....user.infra.websocket.routes.user_ws_routes import user_ws_routes
from ....device.infra.http.routes.device_routes import device_router


class App:
    def __init__(self):
        self.app = FastAPI()
        self.middlewares()
        self.routes()
        self.ws_routes()
        self.database()


    def middlewares(self):
        self.app.middleware('http')(excepetion_middleware)
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_methods=['*'],
            allow_headers=['*'],
            allow_credentials=True
        )


    def routes(self):
        self.app.include_router(user_router)
        self.app.include_router(device_router)

 
    def ws_routes(self):
        user_ws_routes(self.app, '/ws')


    def database(self):
        Base.metadata.create_all(db_engine)


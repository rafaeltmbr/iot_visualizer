from fastapi import FastAPI

from ....user.infra.http.routes.user_routes import user_router
from ....device.infra.http.routes.device_routes import device_router

from ..sqlalchemy.db_engine import db_engine
from ..sqlalchemy.models.Base import Base
from .middlewares.RouteHandler import execpetion_handler_middleware

class App:
    def __init__(self):
        self.app = FastAPI()
        self.middlewares()
        self.routes()
        self.database()

    def middlewares(self):
        self.app.middleware('http')(execpetion_handler_middleware)

    def routes(self):
        self.app.include_router(user_router)
        self.app.include_router(device_router)

    def database(self):
        Base.metadata.create_all(db_engine)


from fastapi import FastAPI

from .middlewares.exception_middleware import excepetion_middleware
from ..sqlalchemy.db_engine import db_engine
from ..sqlalchemy.models.Base import Base
from ....user.infra.http.routes.user_routes import user_router
from ....device.infra.http.routes.device_routes import device_router


class App:
    def __init__(self):
        self.app = FastAPI()
        self.middlewares()
        self.routes()
        self.database()

    def middlewares(self):
        self.app.middleware('http')(excepetion_middleware)

    def routes(self):
        self.app.include_router(user_router)
        self.app.include_router(device_router)

    def database(self):
        Base.metadata.create_all(db_engine)


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

    def database(self):
        Base.metadata.create_all(db_engine)


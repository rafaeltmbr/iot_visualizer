from fastapi import FastAPI

from ....user.infra.http.routes.user_routes import user_router
from ....device.infra.http.routes.device_routes import device_router


class App:
    def __init__(self):
        self.app = FastAPI()
        self.setup_routes()

    def setup_routes(self):
        self.app.include_router(user_router)
        self.app.include_router(device_router)


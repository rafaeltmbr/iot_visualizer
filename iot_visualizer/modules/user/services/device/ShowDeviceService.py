class ShowDeviceService:
    async def execute(self, id):
        return {
            "id": id,
            "name": "Home Controller",
            "description": "Controller located at my home."
        }
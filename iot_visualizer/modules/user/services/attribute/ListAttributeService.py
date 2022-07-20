from ....device.repositories.IAttributeRepository import IAttributeRepository


class ListAttributeService:
    def __init__(self, attribute_repository: IAttributeRepository):
        self.attribute_repository = attribute_repository

    async def execute(self):
        return self.attribute_repository.list()


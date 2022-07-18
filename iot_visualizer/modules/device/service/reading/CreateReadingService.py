
from ...infra.http.schemas.CreateReadingSchema import CreateReadingSchema

class CreateReadingService:
    async def execute(self, body: CreateReadingSchema):
        return body
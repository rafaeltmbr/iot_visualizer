from ...infra.http.schemas.CreateAttributeSchema import CreateAttributeSchema

class CreateAttributeService:
    async def execute(self, body: CreateAttributeSchema):
        return body

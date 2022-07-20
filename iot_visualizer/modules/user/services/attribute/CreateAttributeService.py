from ...infra.http.schemas.attribute.CreateAttributeSchema import CreateAttributeSchema

class CreateAttributeService:
    async def execute(self, body: CreateAttributeSchema):
        return body

from ...infra.http.schemas.attribute.UpdateAttributeSchema import UpdateAttributeSchema

class UpdateAttributeService:
    async def execute(self, id: str, body: UpdateAttributeSchema):
        return body

from ...infra.http.schemas.UpdateAttributeSchema import UpdateAttributeSchema

class UpdateAttributeService:
    async def execute(self, id: str, body: UpdateAttributeSchema):
        return body

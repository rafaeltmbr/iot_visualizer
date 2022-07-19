from uuid import UUID
from pydantic import BaseModel

class UpdateAttributeSchema(BaseModel):
    device_id: UUID
    name: str
    formatting: str
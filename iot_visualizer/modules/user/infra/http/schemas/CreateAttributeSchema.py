from pydantic import BaseModel, Field
from uuid import UUID, uuid4

from .....device.type.attribute_type import attribute_type

class CreateAttributeSchema(BaseModel):
    device_id: UUID
    name: str
    type: attribute_type
    formatting: str
from pydantic import BaseModel

from .....device.type.attribute_type import attribute_type

class CreateAttributeSchema(BaseModel):
    device_id: str
    name: str
    type: attribute_type
    formatting: str
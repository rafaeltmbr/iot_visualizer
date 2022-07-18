from pydantic import BaseModel

from .....device.type.attribute_type import attribute_type

class UpdateAttributeSchema(BaseModel):
    device_id: str
    name: str
    formatting: str
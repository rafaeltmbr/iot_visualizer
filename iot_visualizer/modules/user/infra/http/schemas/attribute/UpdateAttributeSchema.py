from typing import Optional
from pydantic import BaseModel

from .AttributeConfigSchema import AttributeConfigSchema

class UpdateAttributeSchema(BaseModel):
    name: Optional[str] = None
    config: Optional[AttributeConfigSchema] = None
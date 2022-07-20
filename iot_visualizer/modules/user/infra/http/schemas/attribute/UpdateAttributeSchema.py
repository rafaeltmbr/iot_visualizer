from typing import Optional
from pydantic import BaseModel

class UpdateAttributeSchema(BaseModel):
    name: Optional[str] = None
    formatting: Optional[str] = None
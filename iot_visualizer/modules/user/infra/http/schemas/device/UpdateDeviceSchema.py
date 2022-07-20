from typing import Optional
from pydantic import BaseModel


class UpdateDeviceSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    token: Optional[str] = None
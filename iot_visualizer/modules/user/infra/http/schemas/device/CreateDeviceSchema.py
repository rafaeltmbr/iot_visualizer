from uuid import UUID
from pydantic import BaseModel


class CreateDeviceSchema(BaseModel):
    # project_id: UUID
    name: str
    description: str
    token: str
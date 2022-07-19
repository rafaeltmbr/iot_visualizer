from uuid import UUID
from pydantic import BaseModel

class CreateReadingSchema(BaseModel):
    attribute_id: UUID
    value: str
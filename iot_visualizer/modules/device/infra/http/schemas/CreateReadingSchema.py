from uuid import UUID
from pydantic import BaseModel

class NewReadingSchema(BaseModel):
    attribute_id: UUID
    value: str

class CreateReadingsSchema(BaseModel):
    readings: list[NewReadingSchema]
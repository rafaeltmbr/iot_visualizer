from pydantic import BaseModel

class CreateReadingSchema(BaseModel):
    attribute_id: str
    value: str
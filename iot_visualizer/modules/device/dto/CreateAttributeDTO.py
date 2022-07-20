from typing import NamedTuple
from uuid import UUID

from ..type.attribute_type import attribute_type

class CreateAttributeDTO(NamedTuple):
    device_id: UUID
    name: str
    type: attribute_type
    formatting: str
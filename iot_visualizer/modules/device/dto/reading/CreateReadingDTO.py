from typing import NamedTuple
from uuid import UUID


class CreateReadingDTO(NamedTuple):
    attribute_id: UUID
    value: str
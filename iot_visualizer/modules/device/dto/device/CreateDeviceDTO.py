from uuid import UUID
from typing import NamedTuple


class CreateDeviceDTO(NamedTuple):
    # project_id: UUID
    name: str
    description: str
    secret: str

from typing import NamedTuple, Optional

class UpdateDeviceDTO(NamedTuple):
    name: Optional[str]
    description: Optional[str]
    token: Optional[str]
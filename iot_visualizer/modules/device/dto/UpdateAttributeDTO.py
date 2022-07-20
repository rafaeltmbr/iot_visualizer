from typing import NamedTuple, Optional


class UpdateAttributeDTO(NamedTuple):
    name: Optional[str]
    formatting: Optional[str]
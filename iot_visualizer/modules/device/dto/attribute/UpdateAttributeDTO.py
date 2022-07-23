from typing import NamedTuple, Optional

from ....user.infra.http.schemas.attribute.AttributeConfigSchema import AttributeConfigSchema


class UpdateAttributeDTO(NamedTuple):
    name: Optional[str]
    config: Optional[AttributeConfigSchema]
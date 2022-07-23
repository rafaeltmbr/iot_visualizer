from typing import NamedTuple
from uuid import UUID

from ....user.infra.http.schemas.attribute.AttributeConfigSchema import AttributeConfigSchema
from ...type.attribute_type import attribute_type

class CreateAttributeDTO(NamedTuple):
    device_id: UUID
    name: str
    type: attribute_type
    config: AttributeConfigSchema
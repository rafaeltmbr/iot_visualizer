from typing import Literal
import enum

attribute_type = Literal['number', 'boolean', 'text']

class AttributeType(enum.Enum):
    number = 'number'
    boolean = 'boolean'
    text = 'text'
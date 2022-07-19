from typing import Literal
import enum

attribute_type = Literal['number', 'boolean', 'text']

class AttributeType(enum.Enum):
    number = 1
    boolean = 2
    text = 3
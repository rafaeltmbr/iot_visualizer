from enum import Enum
from typing import Optional
from pydantic import BaseModel, root_validator


class AttributeFormattingNumber(BaseModel):
    preffix: str
    suffix: str
    decimals: int


class AttributeFormattingBoolean(BaseModel):
    true_text: str
    false_text: str


class TextTransformation(Enum):
    none = "none"
    lowercase = "lowercase"
    uppercase = "uppercase"


class AttributeFormattingText(BaseModel):
    transform: TextTransformation


class AttributeFormatting(BaseModel):
    number: Optional[AttributeFormattingNumber]
    boolean: Optional[AttributeFormattingBoolean]
    text: Optional[AttributeFormattingText]

    @root_validator
    def only_one_field(cls, value):
        values = [value for value in value.values() if value]

        if len(values) != 1:
            raise ValueError('attribute formatting must have only one of the fields "number", "boolean" or "text" defined')

        return value


class AttributeLayout(Enum):
    short = "short"
    long = "long"


class AttributeConfigSchema(BaseModel):
    layout: AttributeLayout
    index: int
    formatting: AttributeFormatting

    def toDict(self):
        d = {}

        d['layout'] = self.layout.value
        d['index'] = self.index

        d['formatting'] = {}

        if self.formatting.number:
            d['formatting']['number'] = self.formatting.number.dict()

        if self.formatting.boolean:
            d['formatting']['boolean'] = self.formatting.boolean.dict()

        if self.formatting.text:
            d['formatting']['text'] = {}
            d['formatting']['text']['transform'] = self.formatting.text.transform.value

        return d

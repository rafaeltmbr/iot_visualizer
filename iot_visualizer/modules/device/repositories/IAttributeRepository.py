from abc import ABC, abstractmethod
from typing import Union
from uuid import UUID

from ..dto.attribute.CreateAttributeDTO import CreateAttributeDTO
from ..infra.sqlalchemy.models.Attribute import Attribute


class IAttributeRepository(ABC):
    @abstractmethod
    def list_all(self) -> list[Attribute]: raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: UUID) -> Union[Attribute, None]: raise NotImplementedError

    @abstractmethod
    def find_by_id_with_relations(self, id: UUID) -> Union[Attribute, None]: raise NotImplementedError

    @abstractmethod
    def find_by_name(self, name: str) -> Union[Attribute, None]: raise NotImplementedError

    @abstractmethod
    def create(self, dto: CreateAttributeDTO) -> Attribute: raise NotImplementedError

    @abstractmethod
    def update(self, attribute: Attribute) -> Attribute: raise NotImplementedError

    @abstractmethod
    def delete(self, attribute: Attribute) -> None: raise NotImplementedError
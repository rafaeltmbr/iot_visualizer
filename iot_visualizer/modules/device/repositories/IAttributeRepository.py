from abc import ABC, abstractmethod
from uuid import UUID

from ..dto.CreateAttributeDTO import CreateAttributeDTO
from ..infra.sqlalchemy.models.Attribute import Attribute

class IAttributeRepository(ABC):
    @abstractmethod
    def list(self) -> list[Attribute]: raise NotImplementedError

    @abstractmethod
    def show(self, id: UUID) -> Attribute: raise NotImplementedError

    @abstractmethod
    def create(self, dto: CreateAttributeDTO) -> Attribute: raise NotImplementedError

    @abstractmethod
    def update(self, attribute: Attribute) -> Attribute: raise NotImplementedError

    @abstractmethod
    def delete(self, attribute: Attribute) -> Attribute: raise NotImplementedError
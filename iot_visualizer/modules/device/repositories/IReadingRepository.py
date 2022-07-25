from abc import ABC, abstractmethod
from uuid import UUID
from typing import Union

from ..infra.sqlalchemy.models.Reading import Reading
from ..dto.reading.CreateReadingDTO import CreateReadingDTO


class IReadingRepository(ABC):
    @abstractmethod
    def list_all(self) -> list[Reading]: raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: UUID) -> Union[Reading, None]: raise NotImplementedError

    @abstractmethod
    def create(self, dto: CreateReadingDTO) -> Reading: raise NotImplementedError

    @abstractmethod
    def create_many(self, dtos: list[CreateReadingDTO]) -> None: raise NotImplementedError

    @abstractmethod
    def update(self, reading: Reading) -> Reading: raise NotImplementedError

    @abstractmethod
    def delete(self, reading: Reading) -> None: raise NotImplementedError

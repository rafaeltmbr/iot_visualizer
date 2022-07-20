from abc import ABC, abstractmethod
from typing import Union
from uuid import UUID

from ..dto.device.CreateDeviceDTO import CreateDeviceDTO
from ..infra.sqlalchemy.models.Device import Device


class IDeviceRepository(ABC):
    @abstractmethod
    def list(self) -> list[Device]: raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: UUID) -> Union[Device, None]: raise NotImplementedError

    @abstractmethod
    def find_by_id_with_relations(self, id: UUID) -> Union[Device, None]: raise NotImplementedError

    @abstractmethod
    def find_by_name(self, name: str) -> Union[Device, None]: raise NotImplementedError

    @abstractmethod
    def create(self, dto: CreateDeviceDTO) -> Device: raise NotImplementedError

    @abstractmethod
    def update(self, device: Device) -> Device: raise NotImplementedError

    @abstractmethod
    def delete(self, device: Device) -> None: raise NotImplementedError
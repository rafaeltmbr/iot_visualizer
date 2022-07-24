from typing import Callable

from ...infra.sqlalchemy.models.Device import Device
from ...utils.is_reading_value_valid import is_reading_value_valid
from ...repositories.IReadingRepository import IReadingRepository
from ...repositories.IAttributeRepository import IAttributeRepository
from ...repositories.IDeviceRepository import IDeviceRepository
from ...dto.reading.CreateReadingDTO import CreateReadingDTO
from ....shared.utils.AppError import AppError, AppErrors


class CreateReadingService():
    device_listeners: dict[str, list[Callable]] = {}

    def __init__(self, reading_repository: IReadingRepository, attribute_repository: IAttributeRepository, device_repository: IDeviceRepository):
        self.reading_repository = reading_repository
        self.attribute_repository = attribute_repository
        self.device_repository = device_repository

    async def execute(self, data: CreateReadingDTO):
        attribute = self.attribute_repository.find_by_id(data.attribute_id)
        if not attribute:
            raise AppError(AppErrors.ATTRIBUTE_NOT_FOUND)

        if not is_reading_value_valid(data.value, attribute.type.value):
            raise AppError(AppErrors.INVALID_READING_VALUE)

        reading = self.reading_repository.create(data)

        device = self.device_repository.find_by_id_with_relations(attribute.device_id)
        if not device:
            raise AppError(AppErrors.DEVICE_NOT_FOUND)

        CreateReadingService.call_listeners(device)

        return reading


    @classmethod
    def add_listener(cls, device_id: str, listener: Callable):
        listeners = cls.device_listeners.get(device_id)
        if not listeners:
            listeners = []
            cls.device_listeners[device_id] = listeners

        if listener not in listeners:
            listeners.append(listener)


    @classmethod
    def remove_listener(cls, device_id: str, listener: Callable):
        listeners = cls.device_listeners.get(device_id)
        if not listeners:
            return

        if listener in listeners:
            listeners.remove(listener)


    @classmethod
    def call_listeners(cls, device: Device):
        listeners = cls.device_listeners.get(device.id)
        if not listeners:
            return

        for listener in listeners[:]:
            try:
                listener(device)

            except:
                listeners.remove(listener)

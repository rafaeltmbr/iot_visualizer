from typing import Callable

from ...infra.sqlalchemy.models.Reading import Reading
from ...infra.sqlalchemy.models.Device import Device
from ...utils.is_reading_value_valid import is_reading_value_valid
from ...repositories.IReadingRepository import IReadingRepository
from ...repositories.IDeviceRepository import IDeviceRepository
from ...dto.reading.CreateReadingDTO import CreateReadingDTO
from ....shared.utils.AppError import AppError, AppErrors


class CreateReadingsService():
    device_listeners: dict[str, list[Callable]] = {}

    def __init__(self, reading_repository: IReadingRepository, device_repository: IDeviceRepository):
        self.reading_repository = reading_repository
        self.device_repository = device_repository

    async def execute(self, data: list[CreateReadingDTO], device: Device) -> None:
        readings: list[Reading] = CreateReadingsService.remove_duplicate_readings(data)

        attribute_map = {}
        for attribute in device.attributes:
            attribute_map[attribute.id] = attribute

        for reading in readings:
            attribute = attribute_map.get(reading.attribute_id)

            if not attribute:
                raise AppError(AppErrors.NOT_AUTHORIZED_TO_CREATE_ATTRIBUTE_READING)

            if not is_reading_value_valid(reading.value, attribute.type.value):
                raise AppError(AppErrors.INVALID_READING_VALUE)


        self.reading_repository.create_many(readings)

        device = self.device_repository.find_by_id_with_attributes_and_readings(attribute.device_id)
        if not device:
            raise AppError(AppErrors.DEVICE_NOT_FOUND)

        CreateReadingsService.call_listeners(device)


    @staticmethod
    def remove_duplicate_readings(readings: list[CreateReadingDTO]):
        filtered_readings = {}

        for reading in readings:
            filtered_readings[reading.attribute_id] = reading

        return [reading for id, reading in filtered_readings.items()]


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

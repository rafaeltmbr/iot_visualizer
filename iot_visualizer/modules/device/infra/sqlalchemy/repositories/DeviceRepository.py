from typing import Union
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from ..models.Device import Device
from ....dto.device.CreateDeviceDTO import CreateDeviceDTO
from ....repositories.IDeviceRepository import IDeviceRepository
from .....shared.infra.sqlalchemy.db_engine import db_engine


class DeviceRepository(IDeviceRepository):
    session: Session = None

    def __init__(self):
        if not DeviceRepository.session:
            DeviceRepository.session = Session(db_engine)


    def list(self) -> list[Device]:
        return DeviceRepository.session.query(Device).all()


    def find_by_id(self, id: UUID) -> Union[Device, None]:
        return DeviceRepository.session.scalar(select(Device).where(Device.id == id))

    def find_by_id_with_relations(self, id: UUID) -> Union[Device, None]:
        query = select(Device).options(joinedload('attributes').joinedload('readings')).where(Device.id == id)
        return DeviceRepository.session.scalar(query)


    def find_by_name(self, name: str) -> Union[Device, None]:
        return DeviceRepository.session.scalar(select(Device).where(Device.name == name))


    def create(self, dto: CreateDeviceDTO) -> Device:
        device = Device(
            name=dto.name,
            description=dto.description,
            secret=dto.secret,
        )

        DeviceRepository.session.add(device)
        DeviceRepository.session.commit()

        return DeviceRepository.session.scalar(select(Device).where(Device.id == device.id))


    def update(self, device: Device) -> Device:
        DeviceRepository.session.commit()
        return DeviceRepository.session.scalar(select(Device).where(Device.id == device.id))


    def delete(self, device: Device) -> None:
        DeviceRepository.session.delete(device)
        DeviceRepository.session.commit()

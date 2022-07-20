from typing import Union
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from ..models.Device import Device
from ....dto.device.CreateDeviceDTO import CreateDeviceDTO
from ....repositories.IDeviceRepository import IDeviceRepository
from .....shared.infra.sqlalchemy.db_engine import db_engine


class DeviceRepository(IDeviceRepository):
    def __init__(self):
        self.session = Session(db_engine)


    def list(self) -> list[Device]:
        return self.session.query(Device).all()


    def find_by_id(self, id: UUID) -> Union[Device, None]:
        return self.session.scalar(select(Device).where(Device.id == id))

    def find_by_id_with_relations(self, id: UUID) -> Union[Device, None]:
        query = select(Device).options(joinedload('attributes').joinedload('readings')).where(Device.id == id)
        return self.session.scalar(query)


    def find_by_name(self, name: str) -> Union[Device, None]:
        return self.session.scalar(select(Device).where(Device.name == name))


    def create(self, data: CreateDeviceDTO) -> Device:
        device = Device(
            name=data.name,
            description=data.description,
            token=data.token,
        )

        self.session.add(device)
        self.session.commit()

        return self.session.scalar(select(Device).where(Device.id == device.id))


    def update(self, device: Device) -> Device:
        self.session.commit()
        return self.session.scalar(select(Device).where(Device.id == device.id))


    def delete(self, device: Device) -> None:
        self.session.delete(device)
        self.session.commit()

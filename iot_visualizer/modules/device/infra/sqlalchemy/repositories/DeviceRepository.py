from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session

from ....dto.CreateDeviceDTO import CreateDeviceDTO
from ....repositories.IDeviceRepository import IDeviceRepository
from .....shared.infra.sqlalchemy.db_engine import db_engine
from ..models.Device import Device
from ..models.Attribute import Attribute
from ..models.Reading import Reading

class DeviceRepository(IDeviceRepository):
    def __init__(self):
        self.session = Session(db_engine)

    def list(self) -> list[Device]:
        return self.session.query(Device).all()

    def find_by_id(self, id: UUID) -> Device:
        return self.session.scalar(select(Device).where(Device.id == id))

    def find_by_name(self, name: str) -> Device:
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
        return self.session.scalars(select(Device).where(Device.id == device.id))

    def delete(self, device: Device) -> None:
        self.session.delete(device)
        self.session.commit()
    
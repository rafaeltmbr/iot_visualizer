from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session

from .....shared.infra.sqlalchemy.db_engine import db_engine
from ..models.Device import Device
from ..models.Attribute import Attribute
from ..models.Reading import Reading

class DeviceRepository:
    def __init__(self):
        self.session = Session(db_engine)

    def list(self) -> Device:
        return self.session.scalars(select(Device))

    def show(self, id: UUID) -> Device:
        return self.session.scalar(select(Device).where(Device.id == id))

    def update(self, device: Device) -> Device:
        self.session.commit()
        return self.session.scalars(select(Device).where(Device.id == device.id))

    def delete(self, device: Device) -> None:
        self.session.delete(device)
        self.session.commit()
    
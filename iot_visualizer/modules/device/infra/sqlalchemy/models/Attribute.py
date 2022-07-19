from sqlalchemy import Column, DateTime, Enum, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from .....shared.infra.sqlalchemy.models.Base import Base
from ....type.attribute_type import AttributeType

class Attribute(Base):
    __tablename__ = 'attribute'

    id = Column(UUID(as_uuid=True), primary_key=True, default='uuid_generate_v4()')
    device_id = Column(UUID(as_uuid=True), ForeignKey('device.id'), nullable=False)
    name = Column(String, nullable=False)
    type = Column(Enum(AttributeType), nullable=False)
    created_at = Column(DateTime, default='now()', nullable=False)
    updated_at = Column(DateTime, default='now()', nullable=False)

    device = relationship('Device', back_populates='attributes')
    readings = relationship('Reading', back_populates='attribute', cascade='all, delete-orphan')

    UniqueConstraint('device_id', 'name', name='UQ_device_name')

    def __repr__(self):
        return f'''Attribute (
            id={self.id},
            device_id={self.device_id},
            name={self.name},
            type={self.type},
            created_at={self.created_at},
            updated_at={self.updated_at}
        )'''
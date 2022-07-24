from uuid import uuid4
from sqlalchemy import Column, DateTime, Enum, String, ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID, JSON
from sqlalchemy_serializer import SerializerMixin

from .....shared.infra.sqlalchemy.models.Base import Base
from ....type.attribute_type import AttributeType


class Attribute(Base, SerializerMixin):
    __tablename__ = 'attribute'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    device_id = Column(UUID(as_uuid=True), ForeignKey('device.id'), nullable=False)
    name = Column(String, nullable=False)
    type = Column(Enum(AttributeType), nullable=False)
    config = Column(JSON, nullable=False)
    created_at = Column(DateTime, default='now()', nullable=False)
    updated_at = Column(DateTime, default='now()', nullable=False, onupdate=func.current_timestamp())

    device = relationship('Device', back_populates='attributes')
    readings = relationship(
        'Reading',
        back_populates='attribute',
        cascade='all, delete-orphan',
        order_by='desc(Reading.updated_at)',
    )

    serialize_rules = ('-device',)

    UniqueConstraint('device_id', 'name', name='UQ_device_name')

    def __repr__(self):
        return f'''Attribute (
            id={self.id},
            device_id={self.device_id},
            name={self.name},
            type={self.type},
            config={self.config},
            created_at={self.created_at},
            updated_at={self.updated_at}
        )'''
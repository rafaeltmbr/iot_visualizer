from sqlalchemy import Column, Date, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from .....shared.infra.sqlalchemy.models.Base import Base

class Device(Base):
    __tablename__ = 'device'

    id = Column(UUID(as_uuid=True), primary_key=True, default='uuid_generate_v4()')
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    token = Column(String, nullable=False)
    created_at = Column(DateTime, default='now()', nullable=False)
    updated_at = Column(DateTime, default='now()', nullable=False)

    attributes = relationship('Attribute', back_populates='device', cascade='all, delete-orphan')

    def __repr__(self):
        return f'''Device (
            id={self.id},
            name={self.name},
            description={self.description},
            token={self.token},
            created_at={self.created_at},
            updated_at={self.updated_at}
        )'''
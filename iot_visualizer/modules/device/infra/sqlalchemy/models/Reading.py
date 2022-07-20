from uuid import uuid4
from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from .....shared.infra.sqlalchemy.models.Base import Base

class Reading(Base):
    __tablename__ = 'reading'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    attribute_id = Column(UUID(as_uuid=True), ForeignKey('attribute.id'), nullable=False)
    value = Column(String, nullable=False)
    created_at = Column(DateTime, default='now()', nullable=False)
    updated_at = Column(DateTime, default='now()', nullable=False)

    attribute = relationship('Attribute', back_populates='readings')

    def __repr__(self):
        return f'''Reading (
            id={self.id},
            attribute_id={self.attribute_id},
            value={self.value},
            created_at={self.created_at},
            updated_at={self.updated_at}
        )'''
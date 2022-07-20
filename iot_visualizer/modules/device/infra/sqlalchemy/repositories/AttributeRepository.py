from sqlalchemy import select
from sqlalchemy.orm import Session
from uuid import UUID

from ..models.Attribute import Attribute
from ....repositories.IAttributeRepository import IAttributeRepository
from ....dto.CreateAttributeDTO import CreateAttributeDTO
from .....shared.infra.sqlalchemy.db_engine import db_engine


class AttributeRepository(IAttributeRepository):
    def __init__(self):
        self.session = Session(db_engine)


    def list(self) -> list[Attribute]:
        return self.session.query(Attribute).all()


    def find_by_id(self, id: UUID) -> Attribute:
        return self.session.scalar(select(Attribute).where(Attribute.id == id))


    def find_by_name(self, name: str) -> Attribute:
        return self.session.scalar(select(Attribute).where(Attribute.name == name))


    def create(self, data: CreateAttributeDTO) -> Attribute:
        attribute = Attribute(
            device_id = data.device_id,
            name = data.name,
            type = data.type,
            formatting = data.formatting,
        )

        self.session.add(attribute)
        self.session.commit()

        return self.session.scalar(select(Attribute).where(Attribute.id == attribute.id))


    def update(self, attribute: Attribute) -> Attribute:
        self.session.commit()
        return self.session.scalar(select(Attribute).where(Attribute.id == attribute.id))


    def delete(self, attribute: Attribute) -> None:
        self.session.delete(attribute)
        self.session.commit()

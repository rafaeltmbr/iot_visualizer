from typing import Union
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload
from uuid import UUID

from ..models.Attribute import Attribute
from ....repositories.IAttributeRepository import IAttributeRepository
from ....dto.attribute.CreateAttributeDTO import CreateAttributeDTO
from .....shared.infra.sqlalchemy.db_engine import db_engine


class AttributeRepository(IAttributeRepository):
    def __init__(self):
        self.session = Session(db_engine)


    def list(self) -> list[Attribute]:
        return self.session.query(Attribute).all()


    def find_by_id(self, id: UUID) -> Union[Attribute, None]:
        return self.session.scalar(select(Attribute).where(Attribute.id == id))


    def find_by_id_with_relations(self, id: UUID) -> Union[Attribute, None]:
        query = select(Attribute).options(joinedload('readings')).where(Attribute.id == id)
        return self.session.scalar(query)


    def find_by_name(self, name: str) -> Union[Attribute, None]:
        return self.session.scalar(select(Attribute).where(Attribute.name == name))


    def create(self, dto: CreateAttributeDTO) -> Attribute:
        attribute = Attribute(
            device_id = dto.device_id,
            name = dto.name,
            type = dto.type,
            formatting = dto.formatting,
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

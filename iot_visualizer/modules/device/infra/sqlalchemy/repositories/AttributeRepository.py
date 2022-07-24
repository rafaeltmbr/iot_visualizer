from typing import Union
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload
from uuid import UUID


from ..models.Attribute import Attribute
from ....repositories.IAttributeRepository import IAttributeRepository
from ....dto.attribute.CreateAttributeDTO import CreateAttributeDTO
from .....shared.infra.sqlalchemy.db_engine import db_engine
from .....user.infra.http.schemas.attribute.AttributeConfigSchema import AttributeConfigSchema


class AttributeRepository(IAttributeRepository):
    session: Session = None

    def __init__(self):
        if not AttributeRepository.session:
            AttributeRepository.session = Session(db_engine)


    def list(self) -> list[Attribute]:
        return AttributeRepository.session.query(Attribute).all()


    def find_by_id(self, id: UUID) -> Union[Attribute, None]:
        return AttributeRepository.session.scalar(select(Attribute).where(Attribute.id == id))


    def find_by_id_with_relations(self, id: UUID) -> Union[Attribute, None]:
        query = select(Attribute).options(joinedload('readings')).where(Attribute.id == id)
        return AttributeRepository.session.scalar(query)


    def find_by_name(self, name: str) -> Union[Attribute, None]:
        return AttributeRepository.session.scalar(select(Attribute).where(Attribute.name == name))


    def create(self, dto: CreateAttributeDTO) -> Attribute:
        attribute = Attribute(
            device_id = dto.device_id,
            name = dto.name,
            type = dto.type,
            config = dto.config.toDict(),
        )

        AttributeRepository.session.add(attribute)
        AttributeRepository.session.commit()

        return AttributeRepository.session.scalar(select(Attribute).where(Attribute.id == attribute.id))


    def update(self, attribute: Attribute) -> Attribute:
        if isinstance(attribute.config, AttributeConfigSchema):
            attribute.config = attribute.config.toDict()

        AttributeRepository.session.commit()
        return AttributeRepository.session.scalar(select(Attribute).where(Attribute.id == attribute.id))


    def delete(self, attribute: Attribute) -> None:
        AttributeRepository.session.delete(attribute)
        AttributeRepository.session.commit()

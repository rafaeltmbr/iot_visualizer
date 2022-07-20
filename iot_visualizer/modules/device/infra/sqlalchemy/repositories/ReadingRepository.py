from typing import Union
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..models.Reading import Reading
from ....repositories.IReadingRepository import IReadingRepository
from ....dto.reading.CreateReadingDTO import CreateReadingDTO
from .....shared.infra.sqlalchemy.db_engine import db_engine


class ReadingRepository(IReadingRepository):
    def __init__(self):
        self.session = Session(db_engine)

    def list(self) -> list[Reading]:
        return self.session.query(Reading).all()

    def find_by_id(self, id: UUID) -> Union[Reading, None]:
        return self.session.scalar(select(Reading).where(Reading.id == id))

    def create(self, dto: CreateReadingDTO) -> Reading:
        reading = Reading(
            attribute_id = dto.attribute_id,
            value = dto.value,
        )

        self.session.add(reading)
        self.session.commit()

        return self.session.scalar(select(Reading).where(Reading.id == reading.id))

    def update(self, reading: Reading) -> Reading:
        self.session.commit()
        return self.session.scalar(select(Reading).where(Reading.id == reading.id))

    def delete(self, reading: Reading) -> None:
        self.session.delete(reading)
        self.session.commit()
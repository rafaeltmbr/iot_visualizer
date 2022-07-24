from typing import Union
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..models.Reading import Reading
from ....repositories.IReadingRepository import IReadingRepository
from ....dto.reading.CreateReadingDTO import CreateReadingDTO
from .....shared.infra.sqlalchemy.db_engine import db_engine


class ReadingRepository(IReadingRepository):
    session: Session = None

    def __init__(self):
        if not ReadingRepository.session:
            ReadingRepository.session = Session(db_engine)

    def list(self) -> list[Reading]:
        return ReadingRepository.session.query(Reading).all()

    def find_by_id(self, id: UUID) -> Union[Reading, None]:
        return ReadingRepository.session.scalar(select(Reading).where(Reading.id == id))

    def create(self, dto: CreateReadingDTO) -> Reading:
        reading = Reading(
            attribute_id = dto.attribute_id,
            value = dto.value,
        )

        ReadingRepository.session.add(reading)
        ReadingRepository.session.commit()

        return ReadingRepository.session.scalar(select(Reading).where(Reading.id == reading.id))

    def update(self, reading: Reading) -> Reading:
        ReadingRepository.session.commit()
        return ReadingRepository.session.scalar(select(Reading).where(Reading.id == reading.id))

    def delete(self, reading: Reading) -> None:
        ReadingRepository.session.delete(reading)
        ReadingRepository.session.commit()
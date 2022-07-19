from .db_engine import db_engine
from .models.Base import Base
from ....device.infra.sqlalchemy.models import Device, Attribute, Reading

def create_tables():
    Base.metadata.create_all(db_engine)

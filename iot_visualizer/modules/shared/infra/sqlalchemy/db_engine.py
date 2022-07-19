from os import getenv
from sqlalchemy import create_engine

from ...utils.DBConfig import DBConfig

config = DBConfig(
    protocol = 'postgresql',
    user = getenv('DB_USER'),
    password = getenv('DB_PASS'),
    host = getenv('DB_HOST'),
    port = getenv('DB_PORT'),
    database = getenv('DB_DB')
)

print('Database URL:', config.url())

is_production = getenv('PYTHON_ENV') == 'production'

db_engine = create_engine(config.url(), echo=not is_production, future=True)
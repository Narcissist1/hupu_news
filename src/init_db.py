from sqlalchemy import create_engine, MetaData
from .db import rss, entries
from .config import config


def get_db_url():
    db_info = {
        'user': config.POSTGRESQL_USER,
        'password': config.POSTGRESQL_PASS,
        'host': config.POSTGRESQL_HOST,
        'port': config.POSTGRESQL_PORT,
        'database': config.DATABASE_NAME
    }
    DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"
    return DSN.format(**db_info)


def create_table(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[rss, entries])


if __name__ == '__main__':
    db_url = get_db_url()
    engine = create_engine(db_url)
    create_table(engine)

import aiopg.sa
from uuid import uuid4
from datetime import datetime
from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String, Date, Text
)

__all__ = ['rss', 'entries']

meta = MetaData()

def _id():
    return str(uuid4())

rss = Table(
    'rss', meta,

    Column('id', String(36), primary_key=True, default=_id),
    Column('channel', String(100), nullable=False),  # channel title
    Column('url', String(200), nullable=False),  # channel source url
    Column('create_time', Date, nullable=False, default=datetime.now)
)

entries = Table(
    'entries', meta,

    Column('id', String(36), primary_key=True, default=_id),
    Column('title', String(100), nullable=False),   # article title
    Column('link', String(200), nullable=True),     # article link
    Column('summary', Text, nullable=False),    # article content
    Column('published_time', Date, nullable=False, default=datetime.now),
    Column('create_time', Date, nullable=False, default=datetime.now),
    Column('rss_id', String(36), ForeignKey('rss.id', ondelete='CASCADE'))
)


class RecordNotFound(Exception):
    """Requested record in database was not found"""


async def init_pg(app):
    conf = app['config']
    engine = await aiopg.sa.create_engine(
        database=conf.DATABASE_NAME,
        user=conf.POSTGRESQL_USER,
        password=conf.POSTGRESQL_PASS,
        host=conf.POSTGRESQL_HOST,
        port=conf.POSTGRESQL_PORT,
        minsize=conf.POSTGRESQL_MIN,
        maxsize=conf.POSTGRESQL_MAX,
    )
    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()


async def insert_model(conn, model, **values):
    await conn.execute(model.insert().values(**values))


async def update_model(conn, model, **values):
    pass


async def delete_model(conn, model, _id):
    pass


async def select_model(conn, model, **value):
    result = await conn.execute(model.select())
    rv = await result.fetchall()
    return rv

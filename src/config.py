import os
_dir = os.path.dirname(__file__)

class config:
    SOURCE_FILE = os.path.join(_dir, 'source.txt')
    POSTGRESQL_USER = os.getenv('DB_USERNAME', default='postgres')
    POSTGRESQL_PASS = os.getenv('DB_PASSWORD', default='postgres')
    POSTGRESQL_HOST = os.getenv('DB_HOST', default='127.0.0.1')
    POSTGRESQL_PORT = os.getenv('DB_PORT', default=5432)
    POSTGRESQL_MIN = os.getenv('POSTGRESQL_MIN', default=1)
    POSTGRESQL_MAX = os.getenv('POSTGRESQL_MAX', default=5)
    DATABASE_NAME = "rss"

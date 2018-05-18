import pathlib
from aiohttp import web
from .api import Rss, Entries


def setup_routes(app):
    app.router.add_view('/api/rss', Rss)
    app.router.add_view('/api/entry/{entry_id}', Entries)

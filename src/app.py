from aiohttp import web
from .db import init_pg, close_pg
from .route import setup_routes
from .config import config

async def create_app():

    app = web.Application()

    app['config'] = config

    # create db connection on startup, shutdown on exit
    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)

    setup_routes(app)

    # setup_middlewares(app)

    return app

from aiohttp import web
from aiohttp.web_response import json_response
from . import db


class Rss(web.View):
    async def get(self):
        async with self.request.app['db'].acquire() as conn:
            results = await db.select_model(conn, db.rss)
            data = []
            for rv in results:
                data.append({
                    'channel': rv['channel'],
                    'url': rv['url'],
                    'create_time': str(rv['create_time'])
                })
            return json_response({'result': data})

    async def post(self):
        data = await self.request.post()
        url = data.get('url', None)
        channel = data.get('channel', None)
        if not url or not channel:
            return json_response({'result': 'Bad Request'})
        async with self.request.app['db'].acquire() as conn:
            await db.insert_model(conn, db.rss, channel=channel, url=url)
        return json_response({'result': 'SUCCESS'})


class Entries(web.View):
    async def get(self):
        pass

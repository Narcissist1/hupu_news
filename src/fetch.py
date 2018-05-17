import aiohttp
import asyncio
from .utils import gen_load_rss_source
from .globals import session
import feedparser

async def fetch_data(url):
    async with session.get(url) as resp:
        if resp.status == 200:
            return await resp.text()


async def parser_rss(url):
    content = await fetch_data(url)
    feed = feedparser.parse(content)
    print(feed.keys)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    for url in gen_load_rss_source():
        loop.run_until_complete(parser_rss(url))
    loop.close()

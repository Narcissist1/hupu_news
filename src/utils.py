from .config import config
import aiohttp
import asyncio
import feedparser


def gen_load_rss_source():
    with open(config.SOURCE_FILE, 'r') as f:
        for line in f:
            if line:
                # remove '/n'
                yield line[:-1]


async def fetch_data(url):
    async with aiohttp.ClientSession().get(url) as resp:
        if resp.status == 200:
            return await resp.text()


async def parser_rss(url):
    content = await fetch_data(url)
    feed = feedparser.parse(content)
    return feed


if __name__ == '__main__':
    for i in gen_load_rss_source():
        print(i)

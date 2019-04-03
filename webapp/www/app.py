import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(resquest):
    return web.Response(body=b'<h1>Awesome</h1>',headers={'content-type':'text/html'})


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    app_runner = web.AppRunner(app)
    await app_runner.setup()
    srv = await loop.create_server(app_runner.server,'127.0.0.1',9001)
    logging.info('service started at http://127.0.0.1:9001...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
import logging
import random
import aiohttp
import aiohttp_jinja2
from aiohttp import web
from faker import Faker
from uuid import uuid4
from pydantic import BaseModel

log = logging.getLogger(__name__)
logger = logging.getLogger('faker')
logger.setLevel(logging.INFO) 

def get_random_name():
    fake = Faker()
    return fake.name()

# def get_random_name():
#     return str(uuid4())

def game(enter_number, random_number):
    try:
        enter_number = int(enter_number)
        random_number = random.randint(1, 100)
    except ValueError:
        result = 'You need to enter a number'
        return result
    if enter_number == random_number:
        result = 'Winner!'
    elif random_number > enter_number:
        result = 'Number less than expected'
    elif random_number < enter_number:
        result = 'Number is greater than'
    elif enter_number > 100:
        result = 'Enter a number from 1 to 100'
    return result

async def index(request):
    ws_current = web.WebSocketResponse()
    
    ws_ready = ws_current.can_prepare(request)
    
    
    if not ws_ready.ok:
        return aiohttp_jinja2.render_template('index.html', request, {})
    await ws_current.prepare(request)
    
    name = get_random_name()
    log.info('%s joined.', name)
    
    await ws_current.send_json({'action': 'connect', 'name': name})
    
    for ws in request.app['websockets'].values():
        await ws.send_json({'action': 'join', 'name': name})
    request.app['websockets'][name] = ws_current
    
    while True:
        msg = await ws_current.receive()
        if msg.type == aiohttp.WSMsgType.text:
            enter_number = str(msg.data)
            result = game(enter_number, random_number=random.randint(1,100))
            for ws in request.app['websockets'].values():
                if ws is not ws_current:
                    await ws.send_json(
                        {'action': 'sent', 'name': name, 'number': enter_number, 'text': result})
                if ws is ws_current:
                    await ws.send_json(
                        {'action': 'sent', 'name': name, 'number': enter_number, 'text': result})
        else:
            break
    del request.app['websockets'][name]
    log.info('%s disconnected.', name)
    for ws in request.app['websockets'].values():
        await ws.send_json({'action': 'disconnect', 'name': name})
    return ws_current
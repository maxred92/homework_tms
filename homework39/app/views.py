from aiohttp import web
import datetime
from http import HTTPStatus
from typing import Optional
import json

from aiohttp import web

from sqlalchemy import exc
import aiohttp_jinja2
import jinja2

api_routes = web.RouteTableDef()

@api_routes.get('/')
async def handler(request):
    context = {'title': 'Write your message...'}
    response = aiohttp_jinja2.render_template('index.html',
                                              request,
                                              context)
    response.headers['Content-Language'] = 'ru'
    return response
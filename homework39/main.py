from aiohttp import web
from app.views import api_routes
from app.database import db_init
import aiohttp_jinja2
import jinja2


app = web.Application(debug=True)
app.router.add_routes(api_routes)

aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader('templates'))

app.cleanup_ctx.append(db_init)


if __name__ == '__main__':
    web.run_app(app, host='localhost', port=7777)
import aiohttp_jinja2
import jinja2
from aiohttp import web
from app.store.database.models import database_accessor
from app.setting import config, BASE_DIR
from app.forum.routes import setup_routes as setup_forum_routes

def setup_config(application):
    application["config"] = config


def setup_external_libraries(application):
    aiohttp_jinja2.setup(
        application,
        loader=jinja2.FileSystemLoader(f"{BASE_DIR}/templates"),
    )

# настроим url-пути для доступа к нашему будущему приложению
def setup_routes(application):
    
    setup_forum_routes(application)

def setup_accessors(application):
    database_accessor.setup(application)

def setup_app(application):
    setup_config(application)
    setup_external_libraries(application)
    setup_routes(application)
    setup_accessors(application)

    
app = web.Application()  # инстанцируем наш веб-сервер

if __name__ == "__main__":
    setup_app(app)
    web.run_app(app, port=config["common"]["port"])
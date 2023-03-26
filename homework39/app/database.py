from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app import setting


engine = create_async_engine(setting.SQLALCHEMY_DATABASE_URL, echo=True)

async_session = async_sessionmaker(bind=engine, expire_on_commit=False)

Base = declarative_base()

async def db_init(app):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    app['db_session'] = async_session
    yield
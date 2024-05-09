from functools import lru_cache
from asyncio import current_task

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import async_sessionmaker
from sqlalchemy.ext.asyncio.scoping import async_scoped_session

import config 


@lru_cache
def get_sessionmaker() -> async_sessionmaker:
    engine = create_async_engine(url=config.get_postgres_url())
    sessionmaker = async_sessionmaker(bind=engine)
    return sessionmaker


Session = async_scoped_session(get_sessionmaker(), scopefunc=current_task)


class Base(DeclarativeBase):
    ...

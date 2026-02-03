import os
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

class SqlAlchemyBase(DeclarativeBase):
    pass

def setup_async_engine():
    db_url = os.getenv("DB_URL")

    if not db_url:
        raise ValueError("DB variables not set")
    
    engine = create_async_engine(
        url=db_url,
        pool_size=20,
        max_overflow=10,
        pool_pre_ping=True 
    )

    return engine

async_engine = setup_async_engine()

AsyncSessionFactory = async_sessionmaker(async_engine, expire_on_commit=False)
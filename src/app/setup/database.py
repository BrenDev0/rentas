from src.persistance.infrastructure.sqlalchemy.setup import get_async_engine
import logging

from src.persistance.infrastructure.sqlalchemy.setup import SqlAlchemyBase
from src.features.users.infrastructure.sqlalchemy.users_repository import SqlAlchemyUser
logger = logging.getLogger(__name__)

async def create_tables():
    try:
        engine = get_async_engine()
        async with engine.begin() as conn:
            await conn.run_sync(SqlAlchemyBase.metadata.create_all)
        logger.info("Tables created successfully")
    except Exception as e:
        logger.error(f"Error creating tables: {str(e)}")
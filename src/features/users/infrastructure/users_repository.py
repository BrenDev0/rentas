from sqlalchemy import Column
from uuid import uuid4
from src.persistance.infrastructure.sqlalchemy.setup import SqlAlchemyBase
from sqlalchemy.dialects.postgresql import UUID
from src.persistance.infrastructure.sqlalchemy.async_data_repository import AsyncSqlAlchemyDataRepositoy

class SqlAlchemyUser(SqlAlchemyBase):
    __tablename__ = "Users"

    user_id=Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    
from uuid import uuid4
from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from src.persistance import SqlAlchemyBase, AsyncSqlAlchemyDataRepository
from ...domain import User

class SqlAlchemyUser(SqlAlchemyBase):
    __tablename__ = "Users"

    user_id=Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name=Column(String, nullable=False)
    email=Column(String, nullable=False)
    email_hash=Column(String, nullable=False)
    phone=Column(String, nullable=False)
    profile_type=Column(String, nullable=False)
    password=Column(String, nullable=False)
    created_at=Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    
class SqlAlchemyUserRepository(AsyncSqlAlchemyDataRepository[User, SqlAlchemyUser]):
    def __init__(self):
        super().__init__(SqlAlchemyUser)

    def _to_entity(self, model):
        return User(
            user_id=model.user_id,
            name=model.name,
            phone=model.phone,
            email=model.email,
            email_hash=model.email_hash,
            profile_type=model.profile_type,
            password=model.password,
            created_at=model.created_at
        )
    
    def _to_model(self, entity):
        data = entity.model_dump(exclude={"user_id", "created_at"} if not entity.user_id else set())
        return SqlAlchemyUser(**data)
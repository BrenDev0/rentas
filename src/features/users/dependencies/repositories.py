from src.di.injector import Injector
from src.features.users.infrastructure.sqlalchemy.users_repository import SqlAlchemyUserRepository


def register_repositories():
    Injector.register_factory(
        key="async_user_repository",
        factory=lambda: SqlAlchemyUserRepository()
    )

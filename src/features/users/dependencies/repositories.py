from src.di.injector import Injector
from src.features.users.infrastructure.sqlalchemy.users_repository import SqlAlchemyUserRepository
from src.persistance.domain.async_data_repository import AsyncDataRepository


def register_repositories(injector: Injector):
    injector.register(AsyncDataRepository, SqlAlchemyUserRepository)



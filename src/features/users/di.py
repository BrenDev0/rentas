from src.di.injector import Injector
from src.features.users.domain import repository
from src.features.users.infrastructure.sqlalchemy.users_repository import SqlAlchemyUserRepository
from src.features.users.application.service import UsersService
from src.features.users.application.use_cases import (
    create
)

def register_app_dependencies(injector: Injector):
    injector.register(repository.UserRepository, SqlAlchemyUserRepository)
    injector.register(UsersService)
    injector.register(create.CreateUser)
    
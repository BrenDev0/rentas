from src.di import Injector
from .domain import UserRepository
from .infrastructure import SqlAlchemyUserRepository
from .application import UsersService
from .application import (
    CreateUser
)

def register_app_dependencies(injector: Injector):
    injector.register(UserRepository, SqlAlchemyUserRepository)
    injector.register(UsersService)
    injector.register(CreateUser)
    
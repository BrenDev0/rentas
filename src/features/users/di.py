from src.di import Injector
from .domain import UserRepository
from .infrastructure import SqlAlchemyUserRepository
from .application import UsersService
from .application import (
    CreateUser,
    UpdateUser,
    UserLogin,
    DeleteUser
)

def register_dependencies(injector: Injector):
    injector.register(UserRepository, SqlAlchemyUserRepository)
    injector.register(UsersService)
    injector.register(CreateUser)
    injector.register(UpdateUser)
    injector.register(UserLogin)
    injector.register(DeleteUser)
    
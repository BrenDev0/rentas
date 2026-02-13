from src.di.injector import Injector
from src.features.users.dependencies import repositories

def register_user_dependencies(injector: Injector):
    repositories.register_repositories(injector=injector)
from src.di.injector import Injector
from src.features.users.dependencies.setup import register_user_dependencies

def setup_dependencies(injector: Injector):
    register_user_dependencies(injector=injector)

    


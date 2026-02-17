from src.di.injector import Injector
from src.security.di import register_shared_dependencies as security_dependencies

from src.features.users.di import register_app_dependencies as users_dependencies

def setup_dependencies(injector: Injector):
    ## core ##
    security_dependencies(injector=injector)


    ## feature ##
    users_dependencies(injector=injector)
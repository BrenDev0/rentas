from src.di.injector import Injector
from .domain.services import (
    encryption,
    hashing,
    web_token
)

from .infrastructure import BcryptHashingService
from .infrastructure.fernet.encryption import FernetEncryptionService
from .infrastructure.jwt.web_token import JwtWebTokenService

def register_shared_dependencies(injector: Injector):
    injector.register(encryption.EncryptionService, FernetEncryptionService)
    injector.register(hashing.HashingService, BcryptHashingService)
    injector.register(web_token.WebTokenService, JwtWebTokenService)


    
    
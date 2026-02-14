from src.di.injector import Injector
from src.security.domain.services import (
    encryption,
    hashing,
    web_token
)

from src.security.infrastructure.bcrypt.hashing import BcryptHashingService
from src.security.infrastructure.fernet.encryption import FernetEncryptionService
from src.security.infrastructure.jwt.web_token import JwtWebTokenService

def register_shared_dependencies(injector: Injector):
    injector.register(encryption.EncryptionService, FernetEncryptionService)
    injector.register(hashing.HashingService, BcryptHashingService)
    injector.register(web_token.WebTokenService, JwtWebTokenService)


    
    
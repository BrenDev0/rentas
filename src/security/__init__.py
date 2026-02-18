"""
structure:
- Domain: Abstract interfaces and exceptions
- Infrastructure: Framework implementations 
- Di registry
"""

__version__ = "1.0.0"
__author__ = "BrenDev0"
__description__ = "Security package for app"

from .domain import (
    HMACException, 
    IncorrectPassword, 
    InvalidToken, 
    ExpiredToken, 
    PermissionsException,
    EncryptionService,
    HashingService,
    WebTokenService
)

from .infrastructure import (
    FernetEncryptionService,
    BcryptHashingService,
    JwtWebTokenService
)

from .interface import (
    authenticate_user,
    verify_hmac
)


__all__ = [
    #### Domain ####
    "HMACException",
    "IncorrectPassword",
    "InvalidToken",
    "ExpiredToken",
    "PermissionsException",

    "EncryptionService",
    "HashingService",
    "WebTokenService",


    #### Infrastructure ####
    "FernetEncryptionService",
    "BcryptHashingService",
    "JwtWebTokenService",

    #### Interface ####
    "authenticate_user",
    "verify_hmac"
]
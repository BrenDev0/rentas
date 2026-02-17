"""
Basic security tools for encryption, hashing, and JWT handling.


This package provides a clean architecture approach:
- Domain: Abstract interfaces and exceptions
- Infrastructure: Framework implementations 
- Di registry
"""

__version__ = "1.0.0"
__author__ = "BrenDev0"
__description__ = "Security utilities for app"

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
    "JwtWebTokenService"
]
"""
Structure:
- Domain: Abstract interfaces, schemas, entities and models
- Infrastructure: Framework implementations 
- Application: Domain applications (use cases, rules)
- Di registry
"""

__version__ = "1.0.0"
__author__ = "BrenDev0"
__description__ = "persistance package for app"

from .domain import (
    ResourceNotFoundException,
    AsyncDataRepository,
    CollisionException
)

from .application import (
    ResourceExists
)

from .infrastructure import (
    AsyncSqlAlchemyDataRepository,
    SqlAlchemyBase,
    get_async_session_factory,
    get_async_engine
)

__all__ = [
    #### Domain ####
    "ResourceNotFoundException",
    "AsyncDataRepository",
    "CollisionException",


    #### Application ####
    "ResourceExists",

    #### Infrastructure ####
    "AsyncSqlAlchemyDataRepository",
    "SqlAlchemyBase",
    "get_async_engine",
    "get_async_session_factory",
]
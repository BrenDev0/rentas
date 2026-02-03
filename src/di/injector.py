from typing import Dict, TypeVar
from src.di.domain.exceptions import DependencyNotRegistered

T = TypeVar("T")

class Injector:
    __instances: Dict[str, T] = {}

    @classmethod
    def register(
        cls,
        key: str,
        instance: T
    ) -> None:
        cls.__instances[key] = instance

    @classmethod
    def resolve(
        cls,
        key: str
    ):
        if key not in cls.__instances:
            raise DependencyNotRegistered(f"Dependency {key} not found")

        return cls.__instances[key]

        
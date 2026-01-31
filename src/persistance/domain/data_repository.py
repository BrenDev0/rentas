from abc import ABC, abstractmethod
from typing import Union, TypeVar, Optional, List
from uuid import UUID

T = TypeVar("T")

class DataRepository(ABC):
    @abstractmethod
    def select_one(
        self,
        key: str,
        value: Union[str, int, UUID],
        response_model: Optional[T] = None
    ) -> T | None:
        raise NotImplementedError
    
    @abstractmethod
    def select_many(
        self,
        key: str,
        value: Union[str, int, UUID],
        response_model: Optional[T] = None
    ) -> List[T] | None:
        raise NotImplementedError
    
    @abstractmethod
    def select_all(self):
        raise NotImplementedError
    
    @abstractmethod
    def update_one(
        self,
        key: str,
        value: Union[str, int, UUID],
        response_model: Optional[T] = None
    ) -> T | None:
        raise NotImplementedError
    
    @abstractmethod
    def update_many(
        self,
        key: str,
        value: Union[str, int, UUID],
        response_model: Optional[T] = None
    ) -> List[T] | None:
        raise NotImplementedError
    
    @abstractmethod
    def delete_one(
        self,
        key: str,
        value: Union[str, int, UUID],
        response_model: Optional[T] = None
    ) -> T | None:
        raise NotImplementedError
    
    @abstractmethod
    def delete_many(
        self,
        key: str,
        value: Union[str, int, UUID],
        response_model: Optional[T] = None
    ) -> List[T] | None:
        raise NotImplementedError
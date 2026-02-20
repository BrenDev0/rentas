from abc import ABC, abstractmethod

class HashingService(ABC):
    @abstractmethod
    def hash_for_search(self, data: str) -> str:
       raise NotImplementedError()

    @abstractmethod
    def hash(self, password: str) -> str:
        raise NotImplementedError()

    @abstractmethod
    def compare(
        self,
        unhashed: str, 
        hashed: str,
    ) -> bool:
        raise NotImplementedError()
from abc import ABC, abstractmethod
from uuid import UUID

class UserExists(ABC):
    @abstractmethod
    async def validate(
        self,
        user_id: UUID
    ) -> bool:
        raise NotImplementedError
    
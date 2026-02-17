from uuid import UUID
from ...domain import AsyncDataRepository
from ...domain import ResourceNotFoundException

class ResourceExists:
    def __init__(
        self,
        repository: AsyncDataRepository
    ):
        self._repository = repository


    async def validate(
        self,
        key: str,
        value: UUID
    ):
        resource = await self._repository.select_one(key, value)

        if not resource:
            raise ResourceNotFoundException(f"Resource with {key}: {value} not found")
        
        return resource
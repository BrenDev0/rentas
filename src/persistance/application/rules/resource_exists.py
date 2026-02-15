from uuid import UUID
from src.persistance.domain.async_data_repository import AsyncDataRepository
from src.persistance.domain.exceptions import ResourceNotFoundException

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
from sqlalchemy import select
from typing import TypeVar, List, Type
from src.persistance.domain.async_data_repository import AsyncDataRepository
from src.persistance.infrastructure.sqlalchemy.setup import AsyncSessionFactory

E = TypeVar("E") # Entity/pydantic
M = TypeVar("M") # sqlalchemy model

class AsyncSqlAlchemyDataRepositoy(AsyncDataRepository[E, M]):
    def __init__(self, model: Type[M], entity: Type[E]):
        self.__model = model
        self.__entity = entity
        self.__session_factory = AsyncSessionFactory

    async def select_one(self, key, value) -> E | None:
        stmt = select(self.__model).where(getattr(self.__model, key) == value)

        async with self.__session_factory() as session:
            result = await session.execute(stmt).scalar_one_or_none()

            return self._to_entity(result) if result else None


    async def select_many(self, key, value) -> List[E] | None:
        stmt = select(self.__model).where(getattr(self.__model, key) == value)

        async with self.__session_factory() as session:
            result = await session.execute(stmt).scalars().all()

            result = [
                self._to_entity(row) for row in result 
            ] if result else None

    async def select_all(self):
        pass

    async def update_one(self, key, value) -> E | None:
        pass

    async def update_many(self, key, value) -> List[E] | None:
        pass

    async def delete_one(self, key, value) -> E | None:
        pass

    async def delete_many(self, key, value) -> List[E] | None:
        pass

    def _to_model(self, entity: E) -> M:
        raise NotImplementedError
    
    def _to_entity(self, model: M) -> E:
        raise NotImplementedError
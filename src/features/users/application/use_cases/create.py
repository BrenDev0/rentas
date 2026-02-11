from src.persistance.domain import async_data_repository
from src.features.users.domain import schemas, entities

class CreateUser:
    def __init__(
        self,
        user_repository: async_data_repository.AsyncDataRepository
    ):
        self.__user_repository = user_repository

    
    async def execute(
        self,
        data: schemas.CreateUserSchema
    ):
        pass
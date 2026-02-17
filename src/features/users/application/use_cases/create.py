from ...domain import UserRepository, CreateUserSchema
from ...application import UsersService

class CreateUser:
    def __init__(
        self,
        users_repository: UserRepository,
        users_service: UsersService
        
    ):
        self.__users_repository = users_repository
        self.__users_service = users_service
        

    async def execute(
        self,
        data: CreateUserSchema,
        profile_type: str
    ):
        partial_entity = self.__users_service.prepare_new_user_data(
            data=data,
            profile_type=profile_type
        )

        enitity = await self.__users_repository.create(
            data=partial_entity
        )

        return self.__users_service.get_public_schema(enitity)
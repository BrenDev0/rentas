from uuid import UUID
from ...domain import UserRepository
from ..service import UsersService


class DeleteUser:
    def __init__(
        self,
        users_repository: UserRepository,
        users_service: UsersService
    ):
        self.__users_repository = users_repository
        self.__users_service = users_service

    async def execute(
        self,
        user_id: UUID
    ):
        deleted_user = await self.__users_repository.delete_one(
            key="user_id",
            value=user_id
        )

        return self.__users_service.get_public_schema(entity=deleted_user)
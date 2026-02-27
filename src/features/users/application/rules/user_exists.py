from uuid import UUID
from ...domain import User, UserExists, UserRepository

class UserExistRule(UserExists):
    """
    Check if user exists in db with if provided in request
    """
    def __init__(
        self,
        user_repository: UserRepository
    ) -> bool:
        self._user_repository = user_repository

    async def validate(self, user_id: UUID):
        """
        Execute the rule

        Args: 
            user_id: from request

        Returns:
            True if user is foundin db with uui provided, False if not
        """
        user = await self._user_repository.select_one(
            key="user_id",
            value=user_id
        )

        return user is not None
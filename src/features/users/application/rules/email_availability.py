from src.features.communications import EmailAvailability
from src.security import HashingService
from ...domain import UserRepository

class EmailAvailabilityRule(EmailAvailability):
    def __init__(
        self,
        hashing: HashingService,
        users_repository: UserRepository
    ):
        self._hashing = hashing
        self._users_repository = users_repository

    
    async def validate(self, email: str) -> bool:
        """
        Check if email is available for registration.
        
        Args:
            email: Email address to validate.
        
        Returns:
            True if email is available (not in use), False if already exists.
        """
        hashed_email = self._hashing.hash_for_search(email)

        email_in_use = await self._users_repository.select_one(
            key="email_hash",
            value=hashed_email
        )

        return email_in_use is None
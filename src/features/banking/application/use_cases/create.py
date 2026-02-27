from uuid import UUID
from src.features.users import UserExists
from src.persistance import ResourceNotFoundException
from ...domian import AccountsRepository, CreateAccountRequest, Account
from ..services.accounts import AccountsService

class CreateAccount:
    def __init__(
        self,
        accounts_repository: AccountsRepository,
        accounts_service: AccountsService,
        user_exists_rule: UserExists
    ):
        self._accounts_repository = accounts_repository
        self._accounts_service = accounts_service
        self._user_exists_rule = user_exists_rule

    async def execute(
        self,
        user_id: UUID,
        data: CreateAccountRequest
    ):
        """
        Execute use case

        Args: 
            user_id: from request
            data: schema from request body
        
        Returns:
            Account public schema

        Raises:
            ResourceNotFoundException if user with id provided does not exist in db.
            User id is used as foregn key for accounts.
        """
        user_exists = self._user_exists_rule.validate(user_id=user_id)

        if not user_exists:
            raise ResourceNotFoundException(
                detail="User not found"
            )

        encrypted_data: Account = self._accounts_service.prepare_new_account_data(
            user_id=user_id,
            data=data
        )

        new_account: Account = self._accounts_repository.create(data=encrypted_data)

        return self._accounts_service.get_public_schema(account=new_account)


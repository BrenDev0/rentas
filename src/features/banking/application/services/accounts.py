from uuid import UUID
from src.security import EncryptionService
from ...domian import CreateAccountRequest, Account, AccountPublic

class AccountsService:
    def __init__(
        self,
        encryption: EncryptionService
    ):
        self._encrytption = encryption

    def prepare_new_account_data(
        self,
        user_id: UUID,
        data: CreateAccountRequest
    ):
        """
        Encrypt feilds before database insertion

        Args:
            data: CreateAccountRequest schema from request body

        Returns: 
            Account entity with encrypted data without db generated fields (account_id, created_at)

        """
        partial_entity = Account(
            user_id=user_id,
            clabe=self._encrytption.encrypt(data.clabe),
            tax_regime=self._encrytption.encrypt(data.tax_regime)
        )

        return partial_entity
    

    def get_public_schema(
        self,
        account: Account
    ):
        """
        Get Public entity for front end

        Args:
            account: entity model directly from db query

        Returns:
            public schema with decrypted feilds for front end
        """
        return AccountPublic(
            account_id=account.account_id,
            tax_regime=self._encrytption.decrypt(account.tax_regime),
            created_at=account.created_at
        )
        
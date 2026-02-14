from src.features.users.domain import entities, schemas
from src.security.domain.services import encryption, hashing

class UsersService:
    def __init__(
        self,
        hashing: hashing.HashingService,
        encryption: encryption.EncryptionService
    ):
        self.__hashing = hashing
        self.__encryption = encryption
        
    def get_public_schema(
        self,
        entity: entities.User
    ) -> schemas.UserPublic:
        return schemas.UserPublic(
            user_id=entity.user_id,
            name=self.__encryption.decrypt(entity.name),
            phone=self.__encryption.decrypt(entity.phone),
            profile_type=entity.profile_type,
            created_at=entity.created_at
        )
    
    def prepare_new_user_data(
        self,
        data: schemas.CreateUserSchema,
        profile_type: str
    ) -> entities.User:
        encrypted_email = self.__encryption.encrypt(data.email)
        encrypted_name = self.__encryption.encrypt(data.name)
        encrypted_phone = self.__encryption.encrypt(data.phone)

        hashed_password = self.__hashing.hash(data.password)
        hashed_email = self.__hashing.hash_for_search(data.email)

        partial_entity = entities.User(
            name=encrypted_name,
            phone=encrypted_phone,
            email=encrypted_email,
            email_hash=hashed_email,
            profile_type=profile_type,
            password=hashed_password
        )

        return partial_entity
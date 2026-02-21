from src.security import EncryptionService, HashingService
from typing import cast
from uuid import UUID
from datetime import datetime
from ..domain import User, UserPublic, CreateUserRequest


class UsersService:
    def __init__(
        self,
        hashing: HashingService,
        encryption: EncryptionService
    ):
        self.__hashing = hashing
        self.__encryption = encryption
        
    def get_public_schema(
        self,
        entity: User
    ) -> UserPublic:
        return UserPublic(
            user_id=cast(UUID, entity.user_id),
            email=self.__encryption.decrypt(entity.email),
            name=self.__encryption.decrypt(entity.name),
            phone=self.__encryption.decrypt(entity.phone),
            profile_type=entity.profile_type,
            created_at=cast(datetime, entity.created_at)
        )
    
    def prepare_new_user_data(
        self,
        data: CreateUserRequest,
        profile_type: str
    ) -> User:
        encrypted_email = self.__encryption.encrypt(data.email)
        encrypted_name = self.__encryption.encrypt(data.name)
        encrypted_phone = self.__encryption.encrypt(data.phone)

        hashed_password = self.__hashing.hash(data.password)
        hashed_email = self.__hashing.hash_for_search(data.email)

        partial_entity = User(
            name=encrypted_name,
            phone=encrypted_phone,
            email=encrypted_email,
            email_hash=hashed_email,
            profile_type=profile_type,
            password=hashed_password
        )

        return partial_entity
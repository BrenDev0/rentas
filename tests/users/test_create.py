import pytest
from unittest.mock import Mock, AsyncMock
from datetime import datetime
from uuid import uuid4
from src.features.users.application.use_cases.create import CreateUser
from src.features.users.application.service import UsersService
from src.features.users.domain import entities, schemas


@pytest.fixture
def mock_users_repository():
    return AsyncMock()

@pytest.fixture
def mock_users_service():
    return Mock()

@pytest.fixture
def use_case(
    mock_users_repository,
    mock_users_service
):
    return CreateUser(
        users_repository=mock_users_repository,
        users_service=mock_users_service
    )


@pytest.mark.asyncio
async def test_success(
    mock_users_repository,
    mock_users_service: UsersService,
    use_case: CreateUser
):
    user_id = uuid4()
    fake_user = entities.User(
        user_id=user_id,
        name="encrypted",
        phone="encrypted",
        email="hashed",
        email_hash="hashed",
        profile_type="OWNER",
        password="hashed",
        last_login=datetime.now(),
        created_at=datetime.now()
    )

    fake_request_data = schemas.CreateUserRequest(
        verification_code=123,
        name="name",
        phone="phone",
        email="email",
        password="password"
    )

    fake_public_schema = schemas.UserPublic(
        user_id=user_id,
        name="decrypted",
        phone="decrypted",
        email="decrypted",
        profile_type="OWNER",
        created_at=datetime.now()

    )

    mock_users_service.prepare_new_user_data.return_value = entities.User(
        name="decrypted",
        phone="decrypted",
        email="decrypted",
        email_hash="hashed",
        profile_type="OWNER",
        password="hashed",
    )

    mock_users_service.get_public_schema.return_value = fake_public_schema

    mock_users_repository.create.return_value = fake_user

    result = await use_case.execute(
        data=fake_request_data,
        profile_type="OWNER"
    )

    mock_users_service.get_public_schema.assert_called_once()



    assert result.name == "decrypted"
    assert result.phone == "decrypted"









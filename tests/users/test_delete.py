import pytest
from datetime import datetime
from uuid import uuid4
from unittest.mock import MagicMock, AsyncMock
from src.features.users.application.use_cases.delete import DeleteUser
from src.features.users.domain import User
from src.features.users.domain.schemas import UserPublic


@pytest.fixture
def mock_repository():
    return AsyncMock()

@pytest.fixture
def mock_service(): 
    return MagicMock()

@pytest.fixture
def use_case(
    mock_repository,
    mock_service
):
    return DeleteUser(
        users_repository=mock_repository,
        users_service=mock_service
    )


@pytest.mark.asyncio
async def test_success(
    mock_repository,
    mock_service,
    use_case: DeleteUser
):
    user_id = uuid4()
    fake_user = User(
        user_id=user_id,
        name="name",
        phone="phone",
        email="email",
        email_hash="hashed email",
        profile_type="owner",
        password="password",
        created_at=datetime.now()
    )

    fake_public_schema = UserPublic(
        user_id=user_id,
        name="decrypted",
        phone="decrypted",
        email="decrypted",
        profile_type="OWNER",
        created_at=datetime.now()

    )


    mock_repository.delete.return_value = fake_user
    mock_service.get_public_schema.return_value = fake_public_schema

    result = await use_case.execute(
        user_id=user_id
    )

    assert isinstance(result, UserPublic)
    assert result.user_id == user_id


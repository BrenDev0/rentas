from dotenv import load_dotenv
load_dotenv()
import pytest
from src.features.users.domain import entities
from src.features.users.infrastructure.sqlalchemy.users_repository import SqlAlchemyUserRepository


@pytest.fixture
def users_repository():
   return SqlAlchemyUserRepository()


@pytest.mark.asyncio
async def test_success(
    users_repository: SqlAlchemyUserRepository
):
    mock_users_data =  entities.User(
        name="decrypted",
        phone="decrypted",
        email="decrypted",
        email_hash="hashed",
        profile_type="OWNER",
        password="hashed",
    )


    result = await users_repository.create(mock_users_data)

    assert isinstance(result, entities.User)

    assert hasattr(result, "user_id")



   

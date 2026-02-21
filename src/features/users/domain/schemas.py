from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
from uuid import UUID
from datetime import datetime
from typing import Optional

class UserConfig(BaseModel):
    model_config=ConfigDict(
        populate_by_name=True,
        serialize_by_alias=True,
        alias_generator=to_camel,
        str_min_length=1,
        extra="forbid"
    )

class UserPublic(UserConfig):
    user_id: UUID
    name: str
    phone: str
    email: str
    profile_type: str
    created_at: datetime

class CreateUserRequest(UserConfig):
    verification_code: int
    name: str
    phone: str
    email: str
    password: str


class UserLoginRequest(UserConfig):
    email: str
    password: str

class UpdateUserRequest(UserConfig):
    name: Optional[str] = None
    phone: Optional[str] = None


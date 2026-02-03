from pydantic import BaseModel
from uuid import UUID
from enum import Enum
from datetime import datetime

class ProfileType(Enum):
    RENTER = "RENTER"
    OWNER = "OWNER"


class User(BaseModel):
    user_id: UUID
    name: str
    phone: str
    email: str
    email_hash: str
    profile_type: ProfileType
    password: str
    created_at: datetime
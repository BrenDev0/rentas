from pydantic import BaseModel
from uuid import UUID
from enum import Enum
from datetime import datetime
from typing import Optional

class ProfileType(Enum):
    RENTER = "RENTER"
    OWNER = "OWNER"


class User(BaseModel):
    user_id: Optional[UUID] = None
    name: str
    phone: str
    email: str
    email_hash: str
    profile_type: ProfileType
    password: str
    created_at: Optional[datetime] = None
    last_login: Optional[datetime] = None
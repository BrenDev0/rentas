from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class Account(BaseModel):
    account_id: UUID
    user_id: UUID
    clabe: str
    tax_regime: str
    created_at: datetime
    
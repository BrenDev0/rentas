from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
from uuid import UUID
from datetime import datetime

class AccountConfig(BaseModel):
    model_config=ConfigDict(
        populate_by_name=True,
        serialize_by_alias=True,
        alias_generator=to_camel,
        extra="forbid",
        str_min_length=1
    )

class AccountPublic(AccountConfig):
    account_id: UUID
    tax_regime: str
    created_at: datetime

class CreateAccountRequest(AccountConfig):
    clabe: str
    tax_regime: str
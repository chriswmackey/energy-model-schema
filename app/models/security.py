from datetime import datetime, timezone
from pydantic import BaseConfig, BaseModel
from uuid import UUID


class RWModel(BaseModel):
    class Config(BaseConfig):
        allow_population_by_alias = True
        json_encoders = {
            datetime: lambda dt: dt.replace(tzinfo=timezone.utc)
            .isoformat()
            .replace("+00:00", "Z")
}


class TokenPayload(RWModel):
    user_id: UUID
    user_name: str = ""


class User(TokenPayload):
    pass

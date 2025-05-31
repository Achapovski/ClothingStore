from datetime import datetime, timezone, timedelta
from uuid import UUID

from pydantic import field_serializer, BaseModel

from src.core.security.config import jwt_config


class JWTDataModel(BaseModel):
    user_id: UUID

    exp: datetime = datetime.now(tz=timezone.utc) + timedelta(
        days=jwt_config.TOKEN_EXPIRED_DAYS,
        minutes=jwt_config.TOKEN_EXPIRED_MINUTES
    )

    @field_serializer("user_id")
    def user_id_serializer(self, value: UUID):
        return value.__str__()

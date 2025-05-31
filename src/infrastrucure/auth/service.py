from dataclasses import dataclass

from jose import jwt
from src.core.security.config import JWTConfig, BaseAuthConfig
from src.core.security.models import JWTDataModel
from src.domains.users.services.service import UserDomainService


@dataclass
class AuthService:
    user_service: UserDomainService
    jwt_config: JWTConfig
    auth_config: BaseAuthConfig

    async def login(self, user_login: str, password: str):
        user = await self.user_service.get_user_by_login(login=user_login)
        await self._validate_auth_user(user_password=password, user_hashed_password=user.password.get_secret_value())
        jwt_data = JWTDataModel(user_id=user.id)
        access_token = await self.generate_access_token(payload=jwt_data)
        return access_token

    async def get_jwt_data(self, token: str) -> JWTDataModel:
        data = jwt.decode(token=token, key=self.jwt_config.TOKEN_SECRET_KEY, algorithms=self.jwt_config.TOKEN_ALGORITHM)
        return JWTDataModel(**data)

    async def generate_access_token(self, payload: JWTDataModel) -> str:
        jwt_token = jwt.encode(
            claims=payload.model_dump(),
            key=self.jwt_config.TOKEN_SECRET_KEY,
            algorithm=self.jwt_config.TOKEN_ALGORITHM
        )
        return jwt_token

    async def _validate_auth_user(self, user_password: str, user_hashed_password: str):
        if not self.auth_config.crypt_context.verify(secret=user_password, hash=user_hashed_password):
            raise ValueError("НЕВЕРНЫЙ ПАРОЛЬ, АЛЛО!")

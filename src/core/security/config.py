from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from pydantic_settings import BaseSettings
from pydantic import Field, computed_field


class BaseAuthConfig(BaseSettings):
    TOKEN_URL: str = "users/login"
    SCHEMES: list[str] = Field(default_factory=lambda: ["bcrypt"])
    DEPRECATED: str = Field(default="auto")

    @computed_field()
    def oauth2_password(self) -> OAuth2PasswordBearer:
        return OAuth2PasswordBearer(tokenUrl=f"{self.TOKEN_URL}")

    @computed_field()
    def crypt_context(self) -> CryptContext:
        return CryptContext(schemes=self.SCHEMES, deprecated=self.DEPRECATED)

    model_config = {
        "env_prefix": "AUTH_"
    }


class JWTConfig(BaseSettings):
    TOKEN_SECRET_KEY: str = Field(default="skaf8sjfa08sf")
    TOKEN_ALGORITHM: str = Field(default='HS256')
    TOKEN_EXPIRED_DAYS: int = Field(default=0)
    # TEST ONLY
    TOKEN_EXPIRED_MINUTES: int = Field(default=10)

    model_config = {
        "env_prefix": "JWT_",
    }


class AuthConfig(BaseSettings):
    base_auth_config: BaseAuthConfig = JWTConfig()
    jwt_config: JWTConfig = JWTConfig()


jwt_config = JWTConfig()
base_auth_config = BaseAuthConfig()

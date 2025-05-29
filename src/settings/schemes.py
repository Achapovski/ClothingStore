from pydantic import BaseModel, SecretStr, Field, PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings


# TODO: Автоматизировать через мета-класс model-config


class DataBase(BaseSettings):
    CONNECTION: str
    USER: SecretStr
    PASSWORD: SecretStr
    HOST: str
    PORT: int = Field(ge=1000, le=16394)
    NAME: str
    IS_ECHO: bool

    @property
    def dsn(self) -> PostgresDsn:
        return PostgresDsn(
            f"{self.CONNECTION}://{self.USER.get_secret_value()}:{self.PASSWORD.get_secret_value()}@{self.HOST}/{self.NAME}"
        )

    model_config = {
        "env_prefix": "DATABASE_"
    }


class Redis(BaseSettings):
    CONNECTION: str
    HOST: str
    PORT: int = Field(ge=1000, le=16394)
    DB_DEFAULT_NUMBER: int = Field(ge=0, le=15)
    DB_STORAGE_NUMBER: int = Field(ge=0, le=15)
    DB_STATE_NUMBER: int = Field(ge=0, le=15)

    def dsn(self, db_number: Field(ge=0, le=15) = 0):
        return RedisDsn(
            f"{self.CONNECTION}://{self.HOST}:{self.PORT}/{db_number}"
        )


class Settings(BaseModel):
    db: DataBase
    redis: Redis

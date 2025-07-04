from functools import lru_cache

from yaml import safe_load
from src.settings.schemes import Settings


@lru_cache()
def get_settings(config_file_name: str = "config.yml") -> Settings:
    with open(f"{config_file_name}") as file:
        data = safe_load(stream=file)
    return Settings.model_validate(data)


settings = get_settings()

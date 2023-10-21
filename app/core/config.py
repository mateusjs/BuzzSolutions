import os
from enum import Enum

from pydantic_settings import BaseSettings


class ModeEnum(str, Enum):
    development = "development"
    production = "production"
    testing = "testing"


class Settings(BaseSettings):
    PROJECT_NAME: str = "app"
    BACKEND_CORS_ORIGINS: list = ["*"]
    MODE: ModeEnum = ModeEnum.development

    class Config:
        case_sensitive = True
        env_file = os.path.expanduser("~/.env")


settings = Settings()

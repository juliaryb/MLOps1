# settings.py
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    API_KEY: str

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value):
        allowed_environments = {"dev", "test", "prod"}

        if value not in allowed_environments:
            raise ValueError(
                f"ENVIRONMENT must be one of {list(allowed_environments)}, got {value}"
            )

        return value

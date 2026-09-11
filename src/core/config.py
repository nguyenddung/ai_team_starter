from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Team Starter"
    app_env: str = "development"
    app_debug: bool = False
    api_prefix: str = "/api/v1"
    database_url: str = "sqlite:///./app.db"
    ai_provider: str = "mock"
    ai_model: str = "mock-model"
    openai_api_key: str | None = None
    cors_origins: list[str] = ["http://localhost:3000"]
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

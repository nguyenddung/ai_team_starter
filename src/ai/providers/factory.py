from src.ai.providers.base import AIProvider
from src.ai.providers.mock import MockProvider
from src.core.config import settings


def create_provider() -> AIProvider:
    if settings.ai_provider == "mock":
        return MockProvider()
    raise ValueError(f"Unsupported AI_PROVIDER: {settings.ai_provider}")


import pytest

from src.ai.providers.mock import MockProvider
from src.schemas.chat import ChatRequest
from src.services.chat import ChatService


@pytest.mark.asyncio
async def test_chat_service_uses_provider() -> None:
    result = await ChatService(MockProvider()).reply(ChatRequest(message="hello"))
    assert result.answer == "Mock response: hello"
    assert result.provider == "mock"


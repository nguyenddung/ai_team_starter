from src.ai.providers.factory import create_provider
from src.services.chat import ChatService


def get_chat_service() -> ChatService:
    return ChatService(provider=create_provider())


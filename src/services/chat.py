from src.ai.providers.base import AIProvider
from src.schemas.chat import ChatRequest, ChatResponse


class ChatService:
    def __init__(self, provider: AIProvider) -> None:
        self.provider = provider

    async def reply(self, request: ChatRequest) -> ChatResponse:
        answer = await self.provider.generate(request.message)
        return ChatResponse(answer=answer, provider=self.provider.name)


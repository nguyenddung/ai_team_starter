from fastapi import APIRouter, Depends

from src.api.dependencies import get_chat_service
from src.schemas.chat import ChatRequest, ChatResponse
from src.services.chat import ChatService

router = APIRouter()


@router.post("", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    service: ChatService = Depends(get_chat_service),
) -> ChatResponse:
    return await service.reply(request)

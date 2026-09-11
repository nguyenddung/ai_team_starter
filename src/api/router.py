from fastapi import APIRouter

from src.api.routes.agents import router as agents_router
from src.api.routes.chat import router as chat_router

api_router = APIRouter()
api_router.include_router(chat_router, prefix="/chat", tags=["chat"])
api_router.include_router(agents_router, prefix="/agents", tags=["agents"])


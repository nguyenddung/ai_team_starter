from src.ai.agents.base import Agent
from src.ai.agents.evaluator import create_evaluator_agent
from src.ai.agents.interviewer import create_interviewer_agent
from src.ai.agents.screener import create_screener_agent
from src.ai.providers.factory import create_provider
from src.services.chat import ChatService


def get_chat_service() -> ChatService:
    return ChatService(provider=create_provider())


def get_screener_agent() -> Agent:
    return create_screener_agent(create_provider())


def get_interviewer_agent() -> Agent:
    return create_interviewer_agent(create_provider())


def get_evaluator_agent() -> Agent:
    return create_evaluator_agent(create_provider())


from src.ai.agents.base import Agent
from src.ai.agents.researcher import create_researcher_agent
from src.ai.agents.reviewer import create_reviewer_agent
from src.ai.agents.writer import create_writer_agent
from src.ai.providers.factory import create_provider
from src.services.chat import ChatService


def get_chat_service() -> ChatService:
    return ChatService(provider=create_provider())


def get_researcher_agent() -> Agent:
    return create_researcher_agent(create_provider())


def get_writer_agent() -> Agent:
    return create_writer_agent(create_provider())


def get_reviewer_agent() -> Agent:
    return create_reviewer_agent(create_provider())

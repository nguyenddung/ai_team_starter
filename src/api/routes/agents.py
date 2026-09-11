from fastapi import APIRouter, Depends

from src.ai.agents.base import Agent
from src.api.dependencies import get_researcher_agent, get_reviewer_agent, get_writer_agent
from src.schemas.agents import AgentRequest, AgentResponse

router = APIRouter()


async def _run(agent: Agent, request: AgentRequest) -> AgentResponse:
    output = await agent.run(request.input)
    return AgentResponse(agent=agent.name, output=output)


@router.post("/researcher", response_model=AgentResponse)
async def researcher(
    request: AgentRequest,
    agent: Agent = Depends(get_researcher_agent),
) -> AgentResponse:
    return await _run(agent, request)


@router.post("/writer", response_model=AgentResponse)
async def writer(
    request: AgentRequest,
    agent: Agent = Depends(get_writer_agent),
) -> AgentResponse:
    return await _run(agent, request)


@router.post("/reviewer", response_model=AgentResponse)
async def reviewer(
    request: AgentRequest,
    agent: Agent = Depends(get_reviewer_agent),
) -> AgentResponse:
    return await _run(agent, request)

from fastapi import APIRouter, Depends

from src.ai.agents.base import Agent
from src.api.dependencies import get_evaluator_agent, get_interviewer_agent, get_screener_agent
from src.schemas.agents import AgentRequest, AgentResponse

router = APIRouter()


async def _run(agent: Agent, request: AgentRequest) -> AgentResponse:
    output = await agent.run(request.input)
    return AgentResponse(agent=agent.name, output=output)


@router.post("/screener", response_model=AgentResponse)
async def screener(
    request: AgentRequest,
    agent: Agent = Depends(get_screener_agent),
) -> AgentResponse:
    return await _run(agent, request)


@router.post("/interviewer", response_model=AgentResponse)
async def interviewer(
    request: AgentRequest,
    agent: Agent = Depends(get_interviewer_agent),
) -> AgentResponse:
    return await _run(agent, request)


@router.post("/evaluator", response_model=AgentResponse)
async def evaluator(
    request: AgentRequest,
    agent: Agent = Depends(get_evaluator_agent),
) -> AgentResponse:
    return await _run(agent, request)

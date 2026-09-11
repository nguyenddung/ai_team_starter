import pytest

from src.ai.agents.evaluator import create_evaluator_agent
from src.ai.agents.interviewer import create_interviewer_agent
from src.ai.agents.screener import create_screener_agent
from src.ai.providers.mock import MockProvider


@pytest.mark.asyncio
async def test_screener_agent_runs_with_its_own_system_prompt() -> None:
    agent = create_screener_agent(MockProvider())
    result = await agent.run("CV: Python 3 năm.\nJD: cần Python 2+ năm.")

    assert agent.name == "screener"
    assert "CV: Python 3 năm." in result


@pytest.mark.asyncio
async def test_interviewer_agent_runs_with_its_own_system_prompt() -> None:
    agent = create_interviewer_agent(MockProvider())
    result = await agent.run("CV + JD backend developer")

    assert agent.name == "interviewer"
    assert "CV + JD backend developer" in result


@pytest.mark.asyncio
async def test_evaluator_agent_runs_with_its_own_system_prompt() -> None:
    agent = create_evaluator_agent(MockProvider())
    result = await agent.run("Câu hỏi: ...\nTrả lời: ...")

    assert agent.name == "evaluator"
    assert "Câu hỏi: ...\nTrả lời: ..." in result


@pytest.mark.asyncio
async def test_agents_have_distinct_system_prompts() -> None:
    provider = MockProvider()
    agents = [
        create_screener_agent(provider),
        create_interviewer_agent(provider),
        create_evaluator_agent(provider),
    ]

    prompts = {agent.system_prompt for agent in agents}
    names = {agent.name for agent in agents}

    assert len(prompts) == 3
    assert names == {"screener", "interviewer", "evaluator"}

import pytest

from src.ai.agents.researcher import create_researcher_agent
from src.ai.agents.reviewer import create_reviewer_agent
from src.ai.agents.writer import create_writer_agent
from src.ai.providers.mock import MockProvider


@pytest.mark.asyncio
async def test_researcher_agent_runs_with_its_own_system_prompt() -> None:
    agent = create_researcher_agent(MockProvider())
    result = await agent.run("Ngữ cảnh: dự án X cần tài liệu Y.")

    assert agent.name == "researcher"
    assert "Ngữ cảnh: dự án X cần tài liệu Y." in result


@pytest.mark.asyncio
async def test_writer_agent_runs_with_its_own_system_prompt() -> None:
    agent = create_writer_agent(MockProvider())
    result = await agent.run("Brief: viết đoạn giới thiệu ngắn.")

    assert agent.name == "writer"
    assert "Brief: viết đoạn giới thiệu ngắn." in result


@pytest.mark.asyncio
async def test_reviewer_agent_runs_with_its_own_system_prompt() -> None:
    agent = create_reviewer_agent(MockProvider())
    result = await agent.run("Bản nháp cần review.")

    assert agent.name == "reviewer"
    assert "Bản nháp cần review." in result


@pytest.mark.asyncio
async def test_agents_have_distinct_system_prompts() -> None:
    provider = MockProvider()
    agents = [
        create_researcher_agent(provider),
        create_writer_agent(provider),
        create_reviewer_agent(provider),
    ]

    prompts = {agent.system_prompt for agent in agents}
    names = {agent.name for agent in agents}

    assert len(prompts) == 3
    assert names == {"researcher", "writer", "reviewer"}

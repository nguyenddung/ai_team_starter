from dataclasses import dataclass

from src.ai.providers.base import AIProvider


@dataclass
class Agent:
    """A single-purpose AI agent bound to one fixed system prompt."""

    name: str
    system_prompt: str
    provider: AIProvider

    async def run(self, user_input: str) -> str:
        return await self.provider.generate(user_input, system_prompt=self.system_prompt)

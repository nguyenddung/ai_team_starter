from abc import ABC, abstractmethod


class AIProvider(ABC):
    name: str

    @abstractmethod
    async def generate(self, prompt: str, *, system_prompt: str | None = None) -> str:
        """Generate a response for a prompt, optionally guided by a system prompt."""


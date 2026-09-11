from abc import ABC, abstractmethod


class AIProvider(ABC):
    name: str

    @abstractmethod
    async def generate(self, prompt: str) -> str:
        """Generate a response for a prompt."""


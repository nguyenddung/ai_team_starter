from src.ai.providers.base import AIProvider


class MockProvider(AIProvider):
    name = "mock"

    async def generate(self, prompt: str) -> str:
        return f"Mock response: {prompt}"


from src.ai.providers.base import AIProvider


class MockProvider(AIProvider):
    name = "mock"

    async def generate(self, prompt: str, *, system_prompt: str | None = None) -> str:
        if system_prompt:
            label = system_prompt.strip().splitlines()[0][:40]
            return f"Mock response [{label}]: {prompt}"
        return f"Mock response: {prompt}"


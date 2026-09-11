from pydantic import BaseModel, Field


class AgentRequest(BaseModel):
    input: str = Field(min_length=1, max_length=20_000)


class AgentResponse(BaseModel):
    agent: str
    output: str

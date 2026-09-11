from dataclasses import dataclass


@dataclass(frozen=True)
class Document:
    text: str
    source: str


class Retriever:
    async def search(self, query: str, limit: int = 5) -> list[Document]:
        """Connect a vector store here when RAG is required."""
        return []


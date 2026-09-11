from src.ai.agents.base import Agent
from src.ai.providers.base import AIProvider

SYSTEM_PROMPT = """Bạn là Researcher agent trong pipeline multi-agent của dự án.
Nhiệm vụ: đọc ngữ cảnh/nội dung được cung cấp trong tin nhắn và tổng hợp thành
các điểm thông tin chính, có tổ chức, để phục vụ bước tiếp theo trong pipeline.

Yêu cầu đầu ra:
- Liệt kê các điểm thông tin chính dưới dạng gạch đầu dòng, ngắn gọn.
- Ghi rõ những gì còn thiếu hoặc chưa rõ ràng trong ngữ cảnh, nếu có.
- Không bịa thông tin không có trong nội dung được cung cấp.
"""


def create_researcher_agent(provider: AIProvider) -> Agent:
    return Agent(name="researcher", system_prompt=SYSTEM_PROMPT, provider=provider)

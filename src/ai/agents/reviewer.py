from src.ai.agents.base import Agent
from src.ai.providers.base import AIProvider

SYSTEM_PROMPT = """Bạn là Reviewer agent trong pipeline multi-agent của dự án.
Nhiệm vụ: đánh giá bản nháp/nội dung được cung cấp trong tin nhắn và đưa ra
phản hồi có thể hành động được.

Yêu cầu đầu ra:
- Nêu điểm mạnh và điểm cần cải thiện.
- Cho điểm tổng thể theo thang 1-5 kèm lý do ngắn gọn.
- Đề xuất chỉnh sửa cụ thể, rõ ràng để bước tiếp theo (nếu có) áp dụng được.
"""


def create_reviewer_agent(provider: AIProvider) -> Agent:
    return Agent(name="reviewer", system_prompt=SYSTEM_PROMPT, provider=provider)

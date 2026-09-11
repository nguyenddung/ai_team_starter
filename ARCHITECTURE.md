# Architecture

Luồng phụ thuộc chính: `API route -> service -> AI provider / RAG / database`. Route chỉ xử lý HTTP; business logic nằm trong service; code nhà cung cấp model được cô lập sau interface `AIProvider`.

## Modules

- `src/app`: khởi tạo và vòng đời ứng dụng.
- `src/api`: endpoint và dependency injection.
- `src/core`: settings, logging ứng dụng thông thường và shared concerns.
- `src/services`: use cases và orchestration.
- `src/ai/providers`: adapter model; không chứa telemetry.
- `src/ai/agents`: các agent chuyên biệt (mỗi agent gắn một system prompt cố định),
  dùng chung `AIProvider` qua `Agent.run(user_input)`.
- `src/ai/rag`: ingest, retrieval và chunking.
- `src/db`, `src/models`, `src/schemas`: persistence và data contracts.
- `eval`: quality gates cho AI; `training`: job/offline experiments.

Provider, vector store và database phải thay thế được qua cấu hình. Không import framework HTTP vào AI/domain layer.

## Multi-agent (TalentScreen)

`src/ai/agents/base.py` định nghĩa `Agent`: một dataclass gồm `name`,
`system_prompt` và một `AIProvider`. Mỗi agent nghiệp vụ là một file riêng,
khai báo hằng số `SYSTEM_PROMPT` và một factory `create_*_agent(provider)`:

- `src/ai/agents/screener.py` — đối chiếu CV với JD, kết luận phù hợp/không phù hợp.
- `src/ai/agents/interviewer.py` — soạn câu hỏi phỏng vấn theo CV/JD.
- `src/ai/agents/evaluator.py` — chấm điểm câu trả lời phỏng vấn.

`AIProvider.generate` nhận thêm tham số `system_prompt` (optional, keyword-only)
để mỗi agent truyền persona của mình xuống provider mà không phá vỡ các lời gọi
cũ (ví dụ `ChatService` vẫn gọi `generate(prompt)` không kèm system prompt).

Mỗi agent được expose qua route riêng dưới `/api/v1/agents/{screener,interviewer,evaluator}`
(xem `src/api/routes/agents.py`), dùng chung schema `AgentRequest`/`AgentResponse`.
Thêm agent mới bằng cách tạo file mới trong `src/ai/agents/`, một dependency
trong `src/api/dependencies.py` và một route trong `src/api/routes/agents.py`.

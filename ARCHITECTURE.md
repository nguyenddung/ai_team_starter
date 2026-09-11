# Architecture

Luồng phụ thuộc chính: `API route -> service -> AI provider / RAG / database`. Route chỉ xử lý HTTP; business logic nằm trong service; code nhà cung cấp model được cô lập sau interface `AIProvider`.

## Modules

- `src/app`: khởi tạo và vòng đời ứng dụng.
- `src/api`: endpoint và dependency injection.
- `src/core`: settings, logging ứng dụng thông thường và shared concerns.
- `src/services`: use cases và orchestration.
- `src/ai/providers`: adapter model; không chứa telemetry.
- `src/ai/rag`: ingest, retrieval và chunking.
- `src/db`, `src/models`, `src/schemas`: persistence và data contracts.
- `eval`: quality gates cho AI; `training`: job/offline experiments.

Provider, vector store và database phải thay thế được qua cấu hình. Không import framework HTTP vào AI/domain layer.


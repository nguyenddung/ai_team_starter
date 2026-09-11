# AI Team Starter

Skeleton thực tế cho team xây dựng ứng dụng AI bằng Python. Project có API, abstraction cho model provider, điểm mở rộng RAG/data pipeline, database, migration, eval, training, test, frontend và CI/CD. Không tích hợp AI logging hoặc telemetry.

## Bắt đầu nhanh

Yêu cầu: Python 3.11+, Git; Docker là tùy chọn.

```bash
cp .env.example .env
python -m venv .venv
# Windows: .venv\Scripts\activate
python -m pip install -e ".[dev]"
uvicorn src.app.main:app --reload
```

Mở `http://localhost:8000/docs`, hoặc kiểm tra `GET /health` và gửi `POST /api/v1/chat` với JSON `{"message":"Xin chào"}`. Mặc định dùng mock provider nên onboarding không cần API key.

## Lệnh thường dùng

```bash
make test
make lint
make migrate
docker compose up --build
```

## Phân chia ownership gợi ý

- Backend: `src/api`, `src/services`, `src/db`, `src/models`, `src/schemas`
- AI/ML: `src/ai`, `eval`, `training`
- Data/RAG: `src/ai/rag`, `scripts`, `config`
- Frontend: `frontend`
- Platform: `.github`, Docker, migrations, CI/CD

Xem [ARCHITECTURE.md](ARCHITECTURE.md), [GIT_WORKFLOW.md](GIT_WORKFLOW.md) và [docs/ONBOARDING.md](docs/ONBOARDING.md).


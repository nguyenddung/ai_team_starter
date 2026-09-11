# AI Team Starter

Skeleton thực tế cho team xây dựng ứng dụng AI bằng Python. Project có API
(FastAPI), abstraction cho model provider, điểm mở rộng RAG/data pipeline,
database (SQLAlchemy + Alembic), eval, training, test, frontend (React +
Vite) và CI/CD. Không tích hợp AI logging hoặc telemetry.

## Yêu cầu hệ thống

- Python 3.11 trở lên
- Git
- Node.js 18+ và npm (chỉ cần nếu làm frontend)
- Docker + Docker Compose (tùy chọn, dùng khi muốn chạy kèm PostgreSQL)

## 1. Cài đặt backend

```bash
# 1. Sao chép file biến môi trường mẫu
cp .env.example .env

# 2. Tạo virtual environment
python -m venv .venv

# 3. Kích hoạt virtual environment
# Windows (cmd/PowerShell):
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 4. Cài dependency (bao gồm dev: pytest, ruff, mypy)
python -m pip install -e ".[dev]"
```

Nguồn khai báo dependency chính là `pyproject.toml`. Nếu công cụ/deploy
platform của bạn cần `requirements.txt` (thay vì cài qua `pyproject.toml`),
repo đã kèm sẵn:

```bash
pip install -r requirements.txt        # chỉ dependency chạy production
pip install -r requirements-dev.txt    # thêm pytest, ruff, mypy cho dev
```

`requirements-dev.txt` tự include `requirements.txt`. Khi thêm/đổi version
dependency, cập nhật cả `pyproject.toml` lẫn hai file này để không bị lệch.

## 2. Chạy backend

```bash
uvicorn src.app.main:app --reload
```

- API chạy tại `http://localhost:8000`.
- Swagger UI: `http://localhost:8000/docs`.
- Kiểm tra nhanh service còn sống: `GET http://localhost:8000/health`.
- Gọi thử endpoint chat:

```bash
curl -X POST http://localhost:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Xin chào"}'
```

Mặc định `AI_PROVIDER=mock` trong `.env`, dùng `MockProvider` (không gọi ra
ngoài) nên onboarding không cần API key. Để dùng provider thật, cập nhật
`AI_PROVIDER` và key tương ứng trong `.env`, sau đó thêm provider mới vào
`src/ai/providers/factory.py`.

### Multi-agent (TalentScreen)

Mỗi agent là một file riêng trong `src/ai/agents/` với `SYSTEM_PROMPT` cố định
và có route API riêng, dùng chung `AI_PROVIDER` đang cấu hình:

```bash
# Đối chiếu CV với JD
curl -X POST http://localhost:8000/api/v1/agents/screener \
  -H "Content-Type: application/json" \
  -d '{"input":"CV: 3 năm Python.\nJD: yêu cầu 2+ năm Python."}'

# Soạn câu hỏi phỏng vấn
curl -X POST http://localhost:8000/api/v1/agents/interviewer \
  -H "Content-Type: application/json" \
  -d '{"input":"CV + JD vị trí Backend Developer"}'

# Chấm điểm câu trả lời phỏng vấn
curl -X POST http://localhost:8000/api/v1/agents/evaluator \
  -H "Content-Type: application/json" \
  -d '{"input":"Câu hỏi: ...\nTrả lời: ..."}'
```

Muốn thêm agent mới: tạo file trong `src/ai/agents/` (khai báo `SYSTEM_PROMPT`
và `create_*_agent(provider)`), thêm dependency trong
`src/api/dependencies.py` và route trong `src/api/routes/agents.py`. Chi tiết
kiến trúc xem [ARCHITECTURE.md](ARCHITECTURE.md).

## 3. Database và migration

Mặc định dùng SQLite tại chỗ (`sqlite:///./app.db`), không cần cài thêm gì.

```bash
# Áp dụng toàn bộ migration hiện có
alembic upgrade head

# Sau khi sửa model trong src/models, tạo migration mới
alembic revision --autogenerate -m "mô tả thay đổi"
alembic upgrade head
```

Muốn dùng PostgreSQL, đổi `DATABASE_URL` trong `.env` (ví dụ giá trị Docker
Compose cấp bên dưới) rồi chạy lại `alembic upgrade head`.

## 4. Lệnh thường dùng (Makefile)

Trên macOS/Linux có `make`, dùng trực tiếp các lệnh sau. Trên Windows không
có `make` mặc định thì chạy lệnh gốc bên phải (hoặc cài Make qua
`choco install make` / dùng Git Bash / WSL).

| Lệnh make | Lệnh gốc | Tác dụng |
| --- | --- | --- |
| `make install` | `python -m pip install -e ".[dev]"` | Cài dependency + dev tools |
| `make dev` | `uvicorn src.app.main:app --reload` | Chạy API với hot-reload |
| `make test` | `pytest` | Chạy toàn bộ test |
| `make lint` | `ruff check . && mypy src` | Lint + type-check |
| `make format` | `ruff format . && ruff check --fix .` | Tự format và fix lỗi lint |
| `make migrate` | `alembic upgrade head` | Áp dụng migration |
| `make docker-up` | `docker compose up --build` | Chạy API + PostgreSQL bằng Docker |
| `make docker-down` | `docker compose down` | Tắt container |

## 5. Chạy bằng Docker

```bash
docker compose up --build
```

Lệnh này build image từ `Dockerfile`, chạy container `api` (đọc biến môi
trường từ `.env`, expose cổng `8000`) và container `db` (PostgreSQL 16, dữ
liệu lưu trong volume `postgres_data`, expose cổng `5432`, user/password/db
đều là `app`). Khi dùng Docker, đặt trong `.env`:

```env
DATABASE_URL=postgresql+psycopg://app:app@db:5432/app
```

Tắt: `docker compose down` (thêm `-v` nếu muốn xóa luôn volume database).

## 6. Test và lint

```bash
pytest              # chạy tests/unit và tests/integration
ruff check .         # lint
ruff format .        # format code
mypy src             # type-check (strict mode, xem pyproject.toml)
```

## 7. Frontend

```bash
cd frontend
npm install
npm run dev       # chạy dev server Vite, mặc định http://localhost:5173
npm run build      # build production vào frontend/dist
npm run preview    # xem thử bản build
```

Frontend gọi API qua CORS; đảm bảo `CORS_ORIGINS` trong `.env` backend có
chứa origin của frontend (mặc định đã cấu hình `http://localhost:3000`, đổi
lại nếu Vite chạy ở cổng khác).

## 8. Eval và training

- `eval/`: đặt dataset versioned, script evaluator (`eval/run_eval.py`) và
  báo cáo chất lượng model. Chạy: `python eval/run_eval.py`. Không lưu
  prompt/response người dùng thật nếu chưa ẩn danh và được phê duyệt.
- `training/`: config và entrypoint cho fine-tuning/offline training
  (`training/train.py`). Dataset lớn, checkpoint, weights phải để ở object
  storage hoặc model registry, không commit vào Git.

## 9. Biến môi trường (`.env`)

| Biến | Ý nghĩa | Giá trị mặc định |
| --- | --- | --- |
| `APP_NAME` | Tên ứng dụng hiển thị | `AI Team Starter` |
| `APP_ENV` | Môi trường chạy (`development`/`staging`/`production`) | `development` |
| `APP_DEBUG` | Bật debug mode | `true` |
| `API_PREFIX` | Tiền tố route API | `/api/v1` |
| `DATABASE_URL` | Connection string SQLAlchemy | `sqlite:///./app.db` |
| `AI_PROVIDER` | Provider AI đang dùng (`mock`, tự thêm provider khác) | `mock` |
| `AI_MODEL` | Tên model gửi cho provider | `mock-model` |
| `OPENAI_API_KEY` | API key nếu dùng provider OpenAI | (trống) |
| `CORS_ORIGINS` | Danh sách origin frontend được phép gọi API (JSON array) | `["http://localhost:3000"]` |

## 10. Cấu trúc thư mục và phân chia ownership gợi ý

| Khu vực | Thư mục | Đội phụ trách gợi ý |
| --- | --- | --- |
| API, business logic, persistence | `src/api`, `src/services`, `src/db`, `src/models`, `src/schemas` | Backend |
| Model provider, RAG, eval, training | `src/ai`, `eval`, `training` | AI/ML |
| Data ingestion, script, cấu hình | `src/ai/rag`, `scripts`, `config` | Data/RAG |
| Giao diện | `frontend` | Frontend |
| CI/CD, Docker, migration | `.github`, `Dockerfile`, `docker-compose.yml`, `alembic` | Platform |

## 11. Tài liệu liên quan

- [ARCHITECTURE.md](ARCHITECTURE.md) — luồng phụ thuộc và vai trò từng module.
- [GIT_WORKFLOW.md](GIT_WORKFLOW.md) — quy ước nhánh, commit, pull request.
- [docs/ONBOARDING.md](docs/ONBOARDING.md) — checklist onboarding thành viên mới.

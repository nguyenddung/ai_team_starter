# Onboarding

1. Copy `.env.example` thành `.env`.
2. Tạo Python virtual environment và chạy `make install` (Windows không có Make: `python -m pip install -e ".[dev]"`).
3. Chạy `pytest`, sau đó `uvicorn src.app.main:app --reload`.
4. Đọc `ARCHITECTURE.md`; chọn module theo ownership trong README.
5. Tạo nhánh theo `GIT_WORKFLOW.md` và mở pull request nhỏ đầu tiên.

Mock provider là mặc định. Chỉ thêm secret vào `.env` cục bộ hoặc secret manager của môi trường deploy.


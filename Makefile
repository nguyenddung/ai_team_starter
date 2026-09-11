.PHONY: install dev test lint format migrate docker-up docker-down
install:
	python -m pip install -e ".[dev]"
dev:
	uvicorn src.app.main:app --reload
test:
	pytest
lint:
	ruff check . && mypy src
format:
	ruff format . && ruff check --fix .
migrate:
	alembic upgrade head
docker-up:
	docker compose up --build
docker-down:
	docker compose down


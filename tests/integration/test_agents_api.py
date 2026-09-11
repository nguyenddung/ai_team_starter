from fastapi.testclient import TestClient

from src.app.main import app

client = TestClient(app)


def test_researcher_endpoint_returns_mock_output() -> None:
    response = client.post("/api/v1/agents/researcher", json={"input": "chủ đề cần nghiên cứu"})

    assert response.status_code == 200
    body = response.json()
    assert body["agent"] == "researcher"
    assert "chủ đề cần nghiên cứu" in body["output"]


def test_writer_endpoint_returns_mock_output() -> None:
    response = client.post("/api/v1/agents/writer", json={"input": "brief nội dung"})

    assert response.status_code == 200
    assert response.json()["agent"] == "writer"


def test_reviewer_endpoint_returns_mock_output() -> None:
    response = client.post("/api/v1/agents/reviewer", json={"input": "bản nháp"})

    assert response.status_code == 200
    assert response.json()["agent"] == "reviewer"


def test_agent_endpoint_rejects_empty_input() -> None:
    response = client.post("/api/v1/agents/researcher", json={"input": ""})

    assert response.status_code == 422

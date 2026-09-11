from fastapi.testclient import TestClient

from src.app.main import app

client = TestClient(app)


def test_screener_endpoint_returns_mock_output() -> None:
    response = client.post("/api/v1/agents/screener", json={"input": "CV vs JD"})

    assert response.status_code == 200
    body = response.json()
    assert body["agent"] == "screener"
    assert "CV vs JD" in body["output"]


def test_interviewer_endpoint_returns_mock_output() -> None:
    response = client.post("/api/v1/agents/interviewer", json={"input": "CV + JD"})

    assert response.status_code == 200
    assert response.json()["agent"] == "interviewer"


def test_evaluator_endpoint_returns_mock_output() -> None:
    response = client.post("/api/v1/agents/evaluator", json={"input": "Q&A"})

    assert response.status_code == 200
    assert response.json()["agent"] == "evaluator"


def test_agent_endpoint_rejects_empty_input() -> None:
    response = client.post("/api/v1/agents/screener", json={"input": ""})

    assert response.status_code == 422

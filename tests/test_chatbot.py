import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_chat_endpoint():
    response = client.post("/chat", json={"message": "Cześć, jak się masz?"})
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert isinstance(data["response"], str)
    assert len(data["response"]) > 0
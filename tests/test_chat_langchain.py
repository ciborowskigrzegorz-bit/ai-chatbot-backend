import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_chat_langchain_endpoint():
    response = client.post("/chat-langchain", json={"message": "Jak działa LangChain?"})
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert isinstance(data["response"], str)
    assert len(data["response"]) > 0
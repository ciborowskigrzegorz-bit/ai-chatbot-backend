import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_chat_with_empty_input():
    response = client.post("/chat", json={})
    assert response.status_code == 422  # brak wymaganych danych

def test_chat_with_wrong_type():
    response = client.post("/chat", json={"message": 123})
    assert response.status_code == 422  # niewłaściwy typ danych
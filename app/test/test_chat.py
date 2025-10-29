from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_chat_endpoint():
  response = client.post("/chat/", json={"query":"What are the HR policies?"})
  assert response.status_code == 200
  assert "reply" in response.json()
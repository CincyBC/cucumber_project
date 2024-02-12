from fastapi.testclient import TestClient

from .app import api

client = TestClient(api)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 404
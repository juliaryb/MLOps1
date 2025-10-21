from fastapi.testclient import TestClient
from app import app


client = TestClient(app)  # this is a "virtual browser"


def test_welcome_root():
    response = client.get("/")  # send a GET request to the root endpoint

    assert response.status_code == 200  # code for request success
    assert response.json() == {"message": "Welcome to the ML API"}


def test_health_check():
    response = client.get("/health")  # request to the health endpoint

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

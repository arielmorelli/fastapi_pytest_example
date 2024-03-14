from fastapi import FastAPI
from fastapi.testclient import TestClient

from src.routes import create_routes


def test_hello_world_route():
    app = FastAPI()
    create_routes(app)

    client = TestClient(app)

    response = client.get("/hello-world")
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}


def test_inexistent_route():
    app = FastAPI()
    create_routes(app)

    client = TestClient(app)

    response = client.get("/inexistent-route")
    assert response.status_code == 404

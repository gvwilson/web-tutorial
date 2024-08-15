"""Test the JSON server."""

from fastapi.testclient import TestClient
import pytest

from server import HEARTBEAT, app


@pytest.fixture
def client():
    return TestClient(app)


def test_can_get_heartbeat(client):
    response = client.get("/heartbeat")
    assert response.status_code == 200
    assert response.json() == HEARTBEAT

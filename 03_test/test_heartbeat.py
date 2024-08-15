"""Test the JSON server."""

from fastapi.testclient import TestClient

from server import HEARTBEAT, app


def test_can_get_heartbeat():
    client = TestClient(app)
    response = client.get("/heartbeat")
    assert response.status_code == 200
    assert response.json() == HEARTBEAT

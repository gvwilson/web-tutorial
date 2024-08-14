"""Test the JSON server."""

from fixtures import client, data

from server import HEARTBEAT


def test_can_get_root(client):
    response = client.get("/heartbeat")
    assert response.status_code == 200
    assert response.json() == HEARTBEAT

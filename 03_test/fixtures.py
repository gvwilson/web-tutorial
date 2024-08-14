"""Test fixtures."""

from fastapi.testclient import TestClient
import pytest

import server
import util


@pytest.fixture
def client():
    return TestClient(server.app)


@pytest.fixture
def data():
    return util.load_data()

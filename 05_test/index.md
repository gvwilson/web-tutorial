# Testing the Server

-   Add a heartbeat to [`server.py`](./server.py)
-   Wrap the [Flask][flask] application with a test client that provides an interface like [httpx][httpx]
-   Run `pytest test_heartbeat.py` to run tests in [`test_heartbeat.py`](./test_heartbeat.py)
-   Rewrite using [pytest][pytest] fixtures in [`test_fixtures.py`](./test_fixtures.py)
    -   Don't duplicate the expected value, since it might change
-   Patch database connection function in [`test_db.py`](./test_db.py) instead of creating a fixture
-   Use the two approaches together in [`test_combined.py`](./test_combined.py)

[flask]: https://flask.palletsprojects.com/
[httpx]: https://www.python-httpx.org/
[pytest]: https://docs.pytest.org/

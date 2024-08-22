# A Server

-   [`server_hello.py`](./server_hello.py): return HTML
    -   Go to http://127.0.0.1:5000 to view (5000 being [Flask][flask]'s default port)
    -   Or use [`fetch.py`](./fetch.py) to fetch and display data
-   [`server_func.py`](./server_func.py) creates the application and configures routes in a function
    -   Get path to staff CSV from `DATA` environment variable
    -   Read and convert to HTML with [PrettyTable][prettytable]
-   [`server_routes.py`](./server_routes.py) configures several routes
    -   Use query parameters in routes to select individual row or column
    -   Use [Polars][polars] to get a dataframe and [Flask][flask] to convert to JSON
-   Some endpoints return HTML, some return JSON
    -   No endpoint should return both
-   [`server_err.py`](./server_err.py) handles errors
    -   Check row and column and raise exception if not there
    -   Rely on [Flask][flask] to handle nonexistent routes

[flask]: https://flask.palletsprojects.com/
[polars]: https://pola.rs/
[prettytable]: https://pypi.org/project/prettytable/

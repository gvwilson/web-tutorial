# Serving JSON

-   <./server_hello.py>: return JSON
    -   Go to <http://127.0.0.1:8000> to view
    -   Or use <./fetch.py> to fetch and display data
-   <./server_func.py> creates the application and configures routes in a function
    -   Get path to staff CSV from `DATA` environment variable
    -   Attach data to `app` object
-   <./server_routes.py> configures several routes
    -   Use query parameters in routes to select individual row or column
    -   Use Python type hints to do type conversion
-   <./server_err.py> handles errors
    -   Check row and column and raise `HTTPException` if not there
    -   Rely on FastAPI to handle nonexistent routes

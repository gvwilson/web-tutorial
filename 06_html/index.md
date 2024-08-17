# Serving HTML

-   Introduce the view part of MVC and use [Jinja][jinja] templates
    -   Alternative [htpy][htpy] is more amenable to debugging but harder to read
-   Add exceptions to [`util.py`](./util.py)
    -   Common parent for all application exceptions to make catching easier
-   Introduction `fmt=whatever` query parameter
    -   Considered a bad practice by some: API endpoint should return a single data format
    -   Doing it this way prevents us using [FastAPI][fastapi]'s built-in support for template rendering
-   Load templates from filesystem in [`views.py`](./views.py)
-   Pass in data as named argument
-   Use the sample template for single-row and multi-row views
-   No changes to [`models.py`](./models.py)

[fastapi]: https://fastapi.tiangolo.com/
[htpy]: https://htpy.dev/
[jinja]: https://jinja.palletsprojects.com/

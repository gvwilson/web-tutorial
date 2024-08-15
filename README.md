# Web Programming for Data Scientists

This tutorial is a short introduction to web programming using modern tools and practices
for data scientists who are comfortable using Python
but have never built interactive websites before.
All of the material is available under [open licenses](./LICENSE.md),
and contributions through our [GitHub repository][repo] are welcome.
All contributors are required to respect our [Code of Conduct](./CODE_OF_CONDUCT.md).

## Learner Persona

-   Sabina, 28, has a master's degree in animal physiology
    and now works for a mid-sized veterinary pharmaceutical company.
-   She learned a bit of R in an undergraduate biostatistics course,
    then picked up Python in grad school.
    She spends several hours a week analyzing data with [Pandas][pandas]
    and visualizing it with [Plotly Express][plotly-express],
    and is comfortable with basic Git commands.
-   Sabina recently became responsible for maintaining a dashboard application built with [Dash][dash].
    She believes a better understanding of how web applications work in general
    will help her debug and extend it.
-   Sabina has tried doing asynchronous online courses a couple of times,
    but strongly prefers learning in real time with other people.

## Syllabus

-   [Introduction](./00_intro/index.md)
-   [Serving JSON](./01_json/index.md)
-   [Using a Database](./02_db/index.md)
-   [Testing the Server](./03_test/index.md)
-   [Serving HTML](./04_html/index.md)
-   [Using Forms](./05_forms/index.md)
-   [An Hour of JavaScript](./06_js/index.md)
-   [JavaScript in the Browser](./07_browser/index.md)
-   [Using HTMX](./08_htmx/index.md)

## Technologies

| Package              | Purpose         |
| -------------------- | --------------- |
| [deno][deno]         | JavaScript      |
| [FastAPI][fastapi]   | web server      |
| [htmx][htmx]         | interaction     |
| [httpx][httpx]       | http            |
| [Jinja2][jinja]      | html templating |
| [Picnic CSS][picnic] | styling         |
| [Polars][polars]     | tabular data    |
| [PyPika][pypika]     | query builder   |
| [pytest][pytest]     | testing         |
| [SQLite][sqlite]     | database        |

[dash]: https://dash.plotly.com/
[deno]: https://deno.com/
[fastapi]: https://fastapi.tiangolo.com/
[htmx]: https://htmx.org/
[httpx]: https://www.python-httpx.org/
[jinja]: https://jinja.palletsprojects.com/
[pandas]: https://pandas.pydata.org/
[picnic]: https://picnicss.com/
[plotly-express]: https://plotly.com/python/plotly-express/
[polars]: https://pola.rs/
[pypika]: https://pypika.readthedocs.io/
[pytest]: https://docs.pytest.org/
[repo]: https://github.com/gvwilson/wp4ds
[sqlite]: https://www.sqlite.org/

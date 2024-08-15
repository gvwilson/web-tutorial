# Using a Database

## Direct SQL

-   Use [SQLite][sqlite] database in `./data/lab.db` instead of CSV file
-   Install `_dict_factory` to get results as list of dictionaries instead of list of tuples
-   And use a flag to convert types like dates and times (used later)
-   [`models.py`](./models.py) implements model part of model-view-controller (MVC)
    -   One function for each question we might ask of our data
-   Use SQL directly instead of an object-relational mapper like [SQLAlchemy], [SQLModel][sqlmodel], or [Pony][pony]
    -   ORMs are hard to debug and don't actually provide that much insulation from schema changes
-   Re-create connection each time model is accessed
    -   Creating it once and attaching to the [FastAPI][fastapi] app fails because of threading
-   Catch SQLite exceptions and raise our own so that our server only has to catch one thing
-   Add some more error handling
-   Security problem: we're inserting a user-defined name into a query
    -   Can't parameterize query on column name
    -   Opens us up to SQL injection attack

## Query Builder

-   FIXME: rewrite with [PyPika][pypika]

[fastapi]: https://fastapi.tiangolo.com/
[pony]: https://ponyorm.org/
[pypika]: https://pypika.readthedocs.io/
[sqlite]: https://www.sqlite.org/
[sqlmodel]: https://sqlmodel.tiangolo.com/

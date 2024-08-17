# Using Forms

-   Remove everything except display of a table of all staff
-   Make HTML the default display format
-   Add a form for adding new people
    -   Copy the database before running
-   [`inserting.py`](./inserting.py): experiment with insertion
    -   Select largest staff ID, add one, insert: race condition
    -   Better to build a subquery
-   Add `add_staff` function to [`models.py`](./models.py)
    -   Must have `commit` in `models.add_staff`
    -   Redirect to "/" instead of using `return root()`
    -   Really should check values…

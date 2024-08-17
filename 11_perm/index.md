# Permissions

-   Everyone can read everything
-   If we're going to add create, update, and delete, we should add *permissions*
    -   The ability to perform an operation on a thing
-   Standard approach:
    -   An *actor* (person or similar) has zero or more *roles*
    -   Each *role* is a collection of pairs of *subject* and *permission*
    -   E.g., *Reader* role has *read* permission for all tables
-   Represent permissions with two tables in the database (obviously)
    -   Worry about authentication (proof of identity) later
-   But how to know which queries are going to do what to which tables?
    -   Store metadata in the on-disk query files (e.g., as embedded comments)
    -   Move our queries into our Python code (object with query and metadata)
    -   First approach requires us to write a parser, so it's probably a bad idea
    -   We can always export the SQL queries from our Python code for testing
    -   So some quick refactoring…
-   Add two new tables
    -   `role` is a many-to-many join table
    -   `permission` defines what roles mean (with wildcard for "all tables")
    -   Load into memory at start of program and turn into lookup table
    -   Expect roles and permissions to change infrequently, so can reload in our server once we have one
-   Implement as checking function that throws an exception
    -   Saves us from writing `if not… raise` over and over
-   `db_fixture.py`: adds the tables
    -   Gives the three users mnemonic names because we're going to use these in tests
    -   Could write tests using numeric staff IDs but magic numbers like that have bitten us before
-   `permission.py`: defines `require`
    -   Also define `get_role` and `get_staff` to support testing
    -   Because a false positive is worse than no signal
-   `test_permission.py`: three kinds of tests
    1.  Do things that shouldn't work at all actually not work? (E.g., no such user)
    1.  Is the error message correctly formatted?
    1.  Do people have the right capabilities?
-   Parameterize (or "parametrize") tests to avoid repetition
    -   Split into two groups (have and have not)
    -   Or doubly-parameterize
-   Notice that there isn't a widely-known Python library for handling permissions
-   And that what we have built will only work if we add the check to our code
    -   Databases like [PostgreSQL][postgresql] implement fine-grained permissions on tables and even rows
    -   But someone still has to set it up
    -   And if someone has access to the underlying `.db` file, the permissions in our Python are moot

[postgresql]: https://www.postgresql.org/

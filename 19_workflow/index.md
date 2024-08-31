# Designing a Workflow

-   A [workflow](g:workflow) is a series of steps something has to go through
-   First is designing plates for an experiment
    -   Sample must not already be claimed by an existing experiment
    -   Plates must parse correctly
    -   Plates cannot be duplicates
    -   One or more people must be associated with experiment
    -   Does the uploader have to be one of those people?
-   Second is invalidating a plate
    -   Person must have privileges
    -   A second person with privileges must OK the invalidation
    -   An example of work in progress
-   To implement experiment creation
    -   Add a `create_experiment` page with a form
    -   Must handle multiple file upload
    -   And check multiple people (no duplicates)
    -   Use [Alpine][alpine] to make page interactive
    -   No schema changes required
-   To implement plate invalidation
    -   Add a `confirmed_by` column to `invalidated`?
    -   But what if we decide two confirmations are needed? Or three?
    -   Would need a join table like `performed`
    -   Save that complexity until the day…
    -   For now just used `confirmed_by`
        -   Display confirmations with NULL as "awaiting"

[alpine]: https://alpinejs.dev/

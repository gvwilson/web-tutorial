# Introduction

-   Sooner or later you're going to want to share your findings
-   And learning how the web works is fun
-   Use modern Python and JavaScript tools
    -   Yes, you're going to have to learn some JavaScript…
    -   …but it's not as bad as you've been told
-   All of these materials can be freely re-used under
    the [CC-BY-NC][cc_by_nc] License (prose)
    and [MIT License][mit] (software)

## Setup

-   Install [uv][uv] for managing Python packages and virtual environments and then run:
    -   `uv venv` in the root directory of this project to create a virtual environment in `./.venv`
    -   `source .venv/bin/activate` to activate that virtual environment
    -   `uv pip install -r requirements.txt` to install requirements
-   To regenerate the sample data, run `make datasets` to:
    -   install the default parameters for `snailz` in `./params`
    -   regenerate the sample data in `./data`
-   Run `make lint` at any time to check the state of the project

This project uses [Make][make] to run tasks because every other option proved to be more complicated.

## The Data

[snailz][snailz] creates synthetic data for a study of mutant snails in the Pacific Northwest.

-   One or more *surveys* are conducted at one or more *sites*.
-   Each survey collects *genomes* and *sizes* of snails.
-   A *grid* at each site is marked out to show the presence or absence of pollution.
-   *Staff* perform *assays* of the snails' genetic material.
-   Each assay plate has a *design* showing the material applied and *readings* showing the measured response.
-   Plates may be *invalidated* after the fact if a staff member believes it is contaminated.

[cc_by_nc]: https://creativecommons.org/licenses/by-nc/4.0/
[make]: https://www.gnu.org/software/make/
[mit]: https://opensource.org/license/MIT
[snailz]: https://gvwilson.github.io/snailz/
[uv]: https://github.com/astral-sh/uv

# Contributing

Contributions are very welcome;
please contact us [by email][email] or by filing an issue in [our repository][repo].
All contributors must abide by our [Code of Conduct](./CODE_OF_CONDUCT.md).

## Structure

-   Use [mccole][mccole] to turn Markdown into HTML
    -   Markdown files are in root directory and sub-directories
    -   Generated HTML is put in `./docs`
-   `BIBLIOGRAPHY.md` has bibliography as definition list
    -   Citation keys have IDs for linking
    -   Use `[key](b:key)` in files to create links (note the `b:` prefix)
-   `GLOSSARY.md` has glossary as definition list
    -   Reference keys have IDs for linking
    -   Use `[key](g:key)` in files to create links (note the `g:` prefix)
-   Lessons are in `nn_slug` directories
    -   `nn` is two-digit sequence number
    -   `slug` is short mnemonic
-   Each lesson must have:
    -   `index.md`: lesson content
    -   `slides.md`: same content as slides
    -   `Makefile`: re-run tasks
        -   Should `include ../common.mk` to get common tasks
    -   Symbolic links `data` and `static` to the `./data` and `./static` directories in the project root

| make task | effect                                   |
| --------- | ---------------------------------------- |
| clean     | clean up                                 |
| commands  | show available commands (default)        |
| datasets  | re-create snailz parameters and datasets |
| lint      | check code and project                   |
| render    | convert to HTML                          |
| serve     | serve generated HTML                     |

## FAQ

Do you need any help?
:   Yes—please see the issues in [our repository][repo].

What sort of feedback would be useful?
:   Everything is welcome,
    from pointing out mistakes in the code to suggestions for better explanations.

Can I add a new section?
:   Absolutely, but please [reach out][email] before doing so.

Why is this material free to read?
:   Because if we all give a little, we all get a lot.

## <a id="contributors">Contributors</a>

-   [*Juanan Pereira*][pereira-juanan] is a lecturer in Computer Science
    at the University of the Basque Country (UPV/EHU), where he researches and tries 
    to integrate open source software, software engineering, and LLMs in education.

-   [*Greg Wilson*][wilson-greg] is a programmer, author, and educator based in Toronto.
    He was the co-founder and first Executive Director of Software Carpentry
    and received ACM SIGSOFT's Influential Educator Award in 2020.

[email]: mailto:gvwilson@third-bit.com
[mccole]: https://github.com/gvwilson/mccole
[repo]: https://github.com/gvwilson/wp4ds
[pereira-juanan]: https://ikasten.io/
[wilson-greg]: https://third-bit.com/

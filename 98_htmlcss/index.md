# HTML and CSS

-   [HyperText Markup Language](g:html) (HTML) is the standard way to represent documents on the web
-   [Cascading Style Sheets](g:css) (CSS) is the standard way to style them
-   Both are more complicated than they should have been but we need to understand a bit of both

## HTML

-   HTML document contains [elements](g:element) and text
-   Elements are shown using [tags](g:tag)
    -   Opening tag `<tagname>` shows where the element begins
    -   Closing tag `</tagname>` shows where it ends
-   Elements must form a tree, i.e., must be strictly nested
    -   `<X>{\ldots}<Y>{\ldots}</Y></X>` is legal
    -   `<X>{\ldots}<Y>{\ldots}</X></Y>` is not
-   And every document should have a single [root element](g:root-element)\index{element!root} that encloses everything else
-   Since `<` and `>` are used to show where tags start and end,
    must use [escape sequences](g:escape-sequence) to represent them
    -   Written `&name;`

| Name         | Escape Sequence | Character |
|------------|-----------------|-----------|
| Less than    | `&lt;`          | < |
| Greater than | `&gt;`          | > |
| Ampersand    | `&amp;`         | & |
| Copyright    | `&copy;`        | © |
| Plus/minus   | `&plusmn;`      | ± |
| Micro        | `&micro;`       | µ |


-   Well-formed HTML page has:
    -   `<!DOCTYPE html>` as the first line
    -   An `html` element enclosing everything else
    -   A single `head` element with metadata
    -   A single `body` element with content
-   Indentation doesn't matter to the browser (but make source more readable to people)
-   Use `<!--` and `-->` to start and end comments (which cannot be nested)

| HTML Tag | Used For                |
| -------- | ----------------------- |
| `div`    | section in a document   |
| `h1`     | level-1 heading         |
| `h2`     | level-2 heading, etc.   |
| `p`      | paragraph               |
| `span`   | inline text             |
| `a`      | hyperlink               |
| `img`    | reference to image      |
| `ul`     | unordered list          |
| `ol`     | ordered (numbered) list |
| `li`     | list element            |
| `table`  | table                   |
| `tr`     | table row               |
| `th`     | table heading           |
| `td`     | table data cell         |

-   Customize elements with `name="value" [attributes](g:attribute)

```
<h1 align="center">A Centered Heading</h1>
```

-   Use `href` attribute of `a` element to link to:
    -   Another page with a full URL such as `https://example.com/page.html`
    -   A page relative to the current one such as `./examples/page.html`
    -   Another element in this page by ID such as `#main-title`

## CSS

-   `<h1 align="center" color="red">…</h1>` is frowned on these days
    -   Hard to keep styling consistent
-   Give elements [classes](g:css-class) and defines styles for classes
-   [`styled_page.html`](./styled_page.html) uses an [external style sheet](g:external-style-sheet)
    [`styled_page.css`](./styled_page.css)
    -   Which can be shared by many pages
-   Can define [CSS variables](g:css-variable) or style things directly

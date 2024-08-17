"""Convert Markdown to HTML."""


import argparse
from bs4 import BeautifulSoup
from markdown import markdown
from pathlib import Path
import util


MARKDOWN_EXTENSIONS = ["attr_list", "def_list", "fenced_code", "md_in_html", "tables"]

RENAMES = {
    "CODE_OF_CONDUCT.md": "code_of_conduct.md",
    "LICENSE.md": "license.md",
    "README.md": "index.md",
}

CSS_LINK = '<link rel="stylesheet" href="@root/static/{css_file}" type="text/css">'

TEMPLATE = """\
<html>
  <head>
    {css_link}
    <link rel="stylesheet" href="@root/static/site.css" type="text/css">
  </head>
  <body>
  {content}
  </body>
  <footer>
    Copyright © 2024 the authors
  </footer>
<html>
"""


def main():
    """Main driver."""
    opt = parse_args()
    files = util.find_files(opt, set([opt.out]))
    for filepath, content in files.items():
        if filepath.suffix == ".md":
            render_markdown(opt.out, filepath, content)
        else:
            copy_file(opt.out, filepath, content)


def copy_file(output_dir, source_path, content):
    """Copy a file verbatim."""
    output_path = make_output_path(output_dir, source_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if output_path.suffix in util.SUFFIXES:
        output_path.write_text(content)
    else:
        output_path.write_bytes(content)


def do_markdown_links(doc, source_path):
    """Fix .md links in HTML."""
    for node in doc.find_all("a"):
        if ("href" in node.attrs) and node["href"].endswith(".md"):
            node["href"] = node["href"].replace(".md", ".html").lower()
    return doc


def do_root_path_prefix(doc, source_path):
    """Fix @root links in HTML."""
    depth = len(source_path.parents) - 1
    prefix = "./" if (depth == 0) else "../" * depth
    for kind in ("a", "link"):
        for node in doc.find_all(kind):
            if ("href" in node.attrs) and ("@root/" in node["href"]):
                node["href"] = node["href"].replace("@root/", prefix)
    return doc


def make_output_path(output_dir, source_path):
    """Build output path."""
    if source_path.name in RENAMES:
        source_path = Path(source_path.parent, RENAMES[source_path.name])
    source_path = Path(str(source_path).replace(".md", ".html"))
    return Path(output_dir, source_path)


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--css", type=str, help="CSS file")
    parser.add_argument("--out", type=str, default="docs", help="output directory")
    parser.add_argument("--root", type=str, default=".", help="root directory")
    return parser.parse_args()


def render_markdown(output_dir, source_path, content):
    """Convert Markdown to HTML."""
    html = markdown(content, extensions=MARKDOWN_EXTENSIONS)
    css_link = CSS_LINK.format(css_file=css_file) if css_file else ""
    html = TEMPLATE.format(content=html, css_link=css_link)

    doc = BeautifulSoup(html, "html.parser")
    for func in (do_markdown_links, do_root_path_prefix):
        doc = func(doc, source_path)

    output_path = make_output_path(output_dir, source_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(str(doc))


if __name__ == "__main__":
    main()

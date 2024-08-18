"""Convert Markdown to HTML."""

import argparse
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader
from markdown import markdown
from pathlib import Path

import util


MARKDOWN_EXTENSIONS = ["attr_list", "def_list", "fenced_code", "md_in_html", "tables"]

RENAMES = {
    "CODE_OF_CONDUCT.md": "code_of_conduct.md",
    "CONTRIBUTING.md": "contributing.md",
    "GLOSSARY.md": "glossary.md",
    "LICENSE.md": "license.md",
    "README.md": "index.md",
}

ROOT_SKIPS = {"bin", "templates"}


def main():
    """Main driver."""
    opt = parse_args()
    root_skips = ROOT_SKIPS | {opt.out}
    files = util.find_files(opt, root_skips)
    env = Environment(loader=FileSystemLoader(opt.templates))
    for filepath, content in files.items():
        if filepath.suffix == ".md":
            render_markdown(env, opt.out, opt.css, filepath, content)
        else:
            copy_file(opt.out, filepath, content)
    for filepath in util.find_symlinks(opt, root_skips):
        copy_symlink(opt.out, filepath)


def choose_template(env, source_path):
    """Select a template."""
    if source_path.name == "slides.md":
        return env.get_template("slides.html")
    return env.get_template("page.html")


def copy_file(output_dir, source_path, content):
    """Copy a file verbatim."""
    output_path = make_output_path(output_dir, source_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    util.write_file(output_path, content)


def copy_symlink(output_dir, source_path):
    """Copy a symbolic link."""
    output_path = make_output_path(output_dir, source_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if not output_path.exists():
        output_path.symlink_to(source_path.readlink())


def do_glossary_links(doc, source_path):
    """Turn 'g:key' links into glossary references."""
    for node in doc.select("a[href]"):
        if node["href"].startswith("g:"):
            node["href"] = f"@root/glossary.html#{node['href'][2:]}"


def do_markdown_links(doc, source_path):
    """Fix .md links in HTML."""
    for node in doc.select("a[href]"):
        if node["href"].endswith(".md"):
            node["href"] = node["href"].replace(".md", ".html").lower()


def do_title(doc, source_path):
    """Make sure title element is filled in."""
    doc.title.string = doc.h1.get_text()


def do_root_path_prefix(doc, source_path):
    """Fix @root links in HTML."""
    depth = len(source_path.parents) - 1
    prefix = "./" if (depth == 0) else "../" * depth
    targets = (
        ("a[href]", "href"),
        ("link[href]", "href"),
        ("script[src]", "src"),
    )
    for selector, attr in targets:
        for node in doc.select(selector):
            if "@root/" in node[attr]:
                node[attr] = node[attr].replace("@root/", prefix)


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
    parser.add_argument("--templates", type=str, default="templates", help="templates directory")
    return parser.parse_args()


def render_markdown(env, output_dir, css_file, source_path, content):
    """Convert Markdown to HTML."""
    template = choose_template(env, source_path)
    html = markdown(content, extensions=MARKDOWN_EXTENSIONS)
    html = template.render(content=html, css_file=css_file)

    transformers = (do_glossary_links, do_markdown_links, do_title, do_root_path_prefix)
    doc = BeautifulSoup(html, "html.parser")
    for func in transformers:
        func(doc, source_path)

    output_path = make_output_path(output_dir, source_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(str(doc))


if __name__ == "__main__":
    main()

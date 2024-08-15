"""Check site consistency."""

import argparse
from pathlib import Path
import re

import util


MD_LINK_DEF = re.compile(r"^\[(.+?)\]:\s+(.+?)\s*$", re.MULTILINE)
MD_LINK_REF = re.compile(r"\[(.+?)\]\[(.+?)\]", re.MULTILINE)
MD_FILE_LINK = re.compile(r"\[(.+?)\]\((.+?)\)", re.MULTILINE)


def main():
    """Main driver."""
    opt = parse_args()
    files = util.find_files(opt)
    linters = [
        lint_file_references,
        lint_link_definitions,
        lint_markdown_links,
    ]
    success = all(f(opt, files) for f in linters)
    if success:
        print("All self-checks passed.")


def lint_file_references(opt, files):
    """Check inter-file references."""
    result = True
    for filepath, content in files.items():
        if filepath.suffix != ".md":
            continue
        for link in MD_FILE_LINK.finditer(content):
            target = resolve_path(filepath.parent, link.group(2))
            if _is_missing(target, files):
                print(f"Missing file: {filepath} => {target}")
                result = False
    return result


def lint_link_definitions(opt, files):
    """Check that Markdown files define the links they use."""
    problems = False
    for filepath, content in files.items():
        if filepath.suffix != ".md":
            continue
        link_refs = {m[1] for m in MD_LINK_REF.findall(content)}
        link_defs = {m[0] for m in MD_LINK_DEF.findall(content)}
        problems = problems or report_diff(f"{filepath} links", link_refs, link_defs)
    return not problems


def lint_markdown_links(opt, files):
    """Check consistency of Markdown links."""
    found = {}
    for filepath, content in files.items():
        if filepath.suffix != ".md":
            continue
        for link in MD_LINK_DEF.finditer(content):
            label, url = link.group(1), link.group(2)
            if label not in found:
                found[label] = {}
            if url not in found[label]:
                found[label][url] = set()
            found[label][url].add(filepath)

    result = True
    for label, data in found.items():
        if len(data) > 1:
            print(f"Inconsistent link: {label} => {data}")
            result = False
    return result


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=str, default=".", help="root directory")
    return parser.parse_args()


def report_diff(msg, refs, defs):
    """Report differences if any."""
    problems = False
    for (kind, vals) in (("missing", refs - defs), ("unused", defs - refs)):
        if vals:
            print(f"{msg} {kind}: {', '.join(vals)}")
            problems = True
    return problems


def resolve_path(source, dest):
    """Account for '..' in paths."""
    while dest[:3] == "../":
        source = source.parent
        dest = dest[3:]
    result = Path(source, dest)
    return result


def _is_missing(actual, available):
    return (not actual.exists()) or ((actual.suffix in util.SUFFIXES) and (actual not in available))


if __name__ == "__main__":
    main()

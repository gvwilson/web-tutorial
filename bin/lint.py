"""Check site consistency."""

import argparse
from pathlib import Path
import re

import util


GLOSS_KEY_DEF = re.compile(r"^.+\s+\{\s*\#(.+?)\s*\}", re.MULTILINE)
GLOSS_KEY_REF = re.compile(r"\[.+?\]\(g:(.+?)\)", re.MULTILINE)
MD_CODEBLOCK_FILE = re.compile(r"^```\s*\{\s*\.(.+?)\s+\#(.+?)\s*\}\s*$(.+?)^```\s*$", re.DOTALL + re.MULTILINE)
MD_FILE_LINK = re.compile(r"\[(.+?)\]\((.+?)\)", re.MULTILINE)
MD_LINK_DEF = re.compile(r"^\[(.+?)\]:\s+(.+?)\s*$", re.MULTILINE)
MD_LINK_REF = re.compile(r"\[(.+?)\]\[(.+?)\]", re.MULTILINE)


def main():
    """Main driver."""
    opt = parse_args()
    root_skips = set(["bin", opt.out])
    files = util.find_files(opt, root_skips)
    linters = [
        lint_codeblock_files,
        lint_file_references,
        lint_glossary_references,
        lint_link_definitions,
        lint_markdown_links,
    ]
    if all(f(opt, files) for f in linters):
        print("All self-checks passed.")


def lint_codeblock_files(opt, files):
    """Check file inclusions."""
    ok = True
    for filepath, content in files.items():
        if filepath.suffix == ".md":
            for block in MD_CODEBLOCK_FILE.finditer(content):
                codepath, expected = block.group(2), block.group(3).strip()
                actual = Path(filepath.parent, codepath).read_text().strip()
                if actual != expected:
                    print(f"Content mismatch: {filepath} => {codepath}")
                    ok = False
    return ok


def lint_file_references(opt, files):
    """Check inter-file references."""
    ok = True
    for filepath, content in files.items():
        if filepath.suffix == ".md":
            for link in MD_FILE_LINK.finditer(content):
                if _is_special_link(link.group(2)):
                    continue
                target = resolve_path(filepath.parent, link.group(2))
                if _is_missing(target, files):
                    print(f"Missing file: {filepath} => {target}")
                    ok = False
    return ok


def lint_glossary_references(opt, files):
    """Check glossary references."""

    # Find keys in glossary file.
    candidates = [k for k in files if "glossary" in str(k).lower()]
    if len(candidates) != 1:
        print("No glossary found (or multiple matches)")
        return False
    gloss_file_key = candidates[0]
    available = set(GLOSS_KEY_DEF.findall(files[gloss_file_key]))

    # Check all files.
    ok = True
    for filepath, content in files.items():
        if filepath.suffix == ".md":
            missing = {
                k.group(1)
                for k in GLOSS_KEY_REF.finditer(content)
                if k.group(1) not in available
            }
            if missing:
                print(f"Missing glossary keys in {filepath}: {', '.join(sorted(missing))}")
                ok = False
    return ok


def lint_link_definitions(opt, files):
    """Check that Markdown files define the links they use."""
    ok = True
    for filepath, content in files.items():
        if filepath.suffix == ".md":
            link_refs = {m[1] for m in MD_LINK_REF.findall(content)}
            link_defs = {m[0] for m in MD_LINK_DEF.findall(content)}
            ok = ok and report_diff(f"{filepath} links", link_refs, link_defs)
    return ok


def lint_markdown_links(opt, files):
    """Check consistency of Markdown links."""
    found = {}
    for filepath, content in files.items():
        if filepath.suffix == ".md":
            for link in MD_LINK_DEF.finditer(content):
                label, url = link.group(1), link.group(2)
                if label not in found:
                    found[label] = {}
                if url not in found[label]:
                    found[label][url] = set()
                found[label][url].add(filepath)

    ok = True
    for label, data in found.items():
        if len(data) > 1:
            print(f"Inconsistent link: {label} => {data}")
            ok = False
    return ok


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=str, default="docs", help="output directory")
    parser.add_argument("--root", type=str, default=".", help="root directory")
    return parser.parse_args()


def report_diff(msg, refs, defs):
    """Report differences if any."""
    ok = True
    for (kind, vals) in (("missing", refs - defs), ("unused", defs - refs)):
        if vals:
            print(f"{msg} {kind}: {', '.join(vals)}")
            ok = False
    return ok


def resolve_path(source, dest):
    """Account for '..' in paths."""
    while dest[:3] == "../":
        source = source.parent
        dest = dest[3:]
    result = Path(source, dest)
    return result


def _is_missing(actual, available):
    """Is a file missing?"""
    return (not actual.exists()) or ((actual.suffix in util.SUFFIXES) and (actual not in available))


def _is_special_link(link):
    """Is this link handled specially?"""
    return link.startswith("g:")


if __name__ == "__main__":
    main()

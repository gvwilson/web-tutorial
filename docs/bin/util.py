"""Utilities."""

from pathlib import Path


SUFFIXES = {".css", ".html", ".js", ".md", ".py"}


def find_files(opt, root_skips=[]):
    """Collect all interesting files."""
    return {
        filepath: _read_file(filepath)
        for filepath in Path(opt.root).glob("**/*.*")
        if _is_interesting(filepath, root_skips)
    }


def _is_interesting(filepath, root_skips):
    """Is this file worth checking?"""
    result = (
        (not str(filepath).startswith(".")) and
        filepath.is_file() and
        (filepath.suffix in SUFFIXES) and
        (not str(filepath.parent.name).startswith(".")) and
        (not any(str(filepath).startswith(s) for s in root_skips))
    )
    return result


def _read_file(filepath):
    """Read file as bytes or text."""
    if filepath.suffix in SUFFIXES:
        return filepath.read_text()
    else:
        return filepath.read_bytes()

"""Slice sections from source files."""

import argparse
import ast
import esprima
from pathlib import Path


class MatchVisitor(esprima.NodeVisitor):
    """Visit Esprima nodes to find identifiers."""

    def __init__(self, expr):
        """Store expression to match."""
        super().__init__()
        self._expr = expr
        self._found = None

    def visit_VariableDeclarator(self, obj):
        """Variable declaration."""
        if obj.id.name == self._expr:
            self._found = obj

    def visit_FunctionDeclaration(self, obj):
        """Function declaration."""
        if obj.id.name == self._expr:
            self._found = obj


def main():
    """Main driver for testing."""
    options = parse_args()
    text = slice_file(options.src, options.expr)
    assert text is not None, f"cannot match {options.expr} in {options.src}"
    print(text)


def js_slice(src, expr):
    """Find and slice in JavaScript file."""
    text = Path(src).read_text()
    doc = esprima.parseScript(text, options={"loc": True})
    matcher = MatchVisitor(expr)
    matcher.visit(doc)
    node = matcher._found
    if node is None:
        return None
    return slice_lines(text, node.loc.start.line, node.loc.end.line)


def py_slice(src, expr):
    """Find and slice in Python file."""
    text = Path(src).read_text()
    doc = ast.parse(text)
    node = py_match(doc, expr)
    if node is None:
        return None
    return slice_lines(text, node.lineno, node.end_lineno)


def py_match(node, expr):
    """Find an entity by name."""
    if hasattr(node, "name") and (node.name == expr):
        return node
    if not hasattr(node, "body"):
        return None
    for child in node.body:
        found = py_match(child, expr)
        if found:
            return found
    return None


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--expr", type=str, required=True, help="pattern expression")
    parser.add_argument("--src", type=str, required=True, help="source file")
    return parser.parse_args()


def slice_file(filepath, expr):
    """Extract slide from file."""
    language = Path(filepath).suffix.lstrip(".")
    handler = {
        "js": js_slice,
        "py": py_slice
    }.get(language, None)
    assert handler is not None, f"unknown file type {filepath}"
    return handler(filepath, expr)


def slice_lines(text, start, end):
    """Slice text from 1-based start to 1-based end line."""
    lines = text.split("\n")
    return "\n".join(lines[start - 1:end])


if __name__ == "__main__":
    main()

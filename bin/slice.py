"""Slice sections from source files."""

import argparse
import ast
import esprima
from pathlib import Path


class MatchVisitor(esprima.NodeVisitor):
    def __init__(self, expr):
        super().__init__()
        self._expr = expr
        self._found = None

    def visit_VariableDeclarator(self, obj):
        if obj.id.name == self._expr:
            self._found = obj

    def visit_FunctionDeclaration(self, obj):
        if obj.id.name == self._expr:
            self._found = obj


def main():
    """Main driver for testing."""
    options = parse_args()
    language = Path(options.src).suffix.lstrip(".")
    handler = {
        "js": js_slice,
        "py": py_slice
    }.get(language, None)
    assert handler is not None, f"unknown file type {options.src}"
    text = handler(options.src, options.expr)
    assert text is not None, f"cannot match {options.expr} in {options.src}"
    print(text)


def js_slice(src, expr):
    """Find and slice in JavaScript file."""
    text = Path(src).read_text()
    doc = esprima.parseScript(text, options={"loc": True})
    matcher = MatchVisitor(expr)
    matcher.visit(doc)
    found = matcher._found
    return None if found is None else slice_lines(text, found.loc.start.line, found.loc.end.line)


def py_slice(src, expr):
    """Find and slice in Python file."""
    text = Path(src).read_text()
    doc = ast.parse(text)
    node = py_match(doc, expr)
    return None if node is None else slice_lines(text, node.lineno, node.end_lineno)


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


def slice_lines(text, start, end):
    lines = text.split("\n")
    return "\n".join(lines[start - 1:end])


if __name__ == "__main__":
    main()

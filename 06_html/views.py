"""Manage HTML views."""

from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateError

from util import ViewException


Env = Environment(
    loader=FileSystemLoader("./templates"),
)


def all_staff(data):
    return _use_template(data, "rows.html")


def heartbeat(data):
    return HTMLResponse(f"<p>{data['message']}</p>")


def column(data):
    return _use_template(data, "col.html")


def row(data):
    return _use_template([data], "rows.html")


def _use_template(data, template_name):
    try:
        template = Env.get_template(template_name)
        return HTMLResponse(template.render(data=data))
    except TemplateError as exc:
        raise ViewException(f"template error: {exc}")

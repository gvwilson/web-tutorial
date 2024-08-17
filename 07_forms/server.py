"""Serve data from data model layer."""

from fastapi import FastAPI, Form, HTTPException

import models
import views

from util import AppException


FMT_HTML = "html"
FMT_JSON = "json"


def handle_format(data, fmt, view):
    """Handle format conversion."""
    if fmt == FMT_JSON:
        return data
    elif fmt == FMT_HTML:
        return view(data)
    raise HTTPException(status_code=415, detail=f"Unsupported format {fmt}")


def make_server():
    """Build application and configure routes."""
    app = FastAPI()

    @app.get("/")
    def root(fmt: str = FMT_HTML):
        try:
            return handle_format(models.all_staff(), fmt, views.all_staff)
        except AppException as exc:
            raise HTTPException(status_code=404, detail=f"Error serving all staff: {exc}")

    @app.post("/add")
    def add(personal: str = Form(), family: str = Form()):
        print(f"personal {personal} family {family}")
        return root()

    return app


app = make_server()

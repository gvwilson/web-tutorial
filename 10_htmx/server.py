"""Serve data from data model layer."""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

import models
import views
from util import AppException


HEARTBEAT = {"message": "alive"}
FMT_HTML = "html"
FMT_JSON = "json"


def handle_format(data, fmt, view, *args):
    """Handle format conversion."""
    if fmt == FMT_JSON:
        return data
    elif fmt == FMT_HTML:
        return view(data, *args)
    raise HTTPException(status_code=415, detail=f"Unsupported format {fmt}")


def make_server():
    """Build application and configure routes."""
    app = FastAPI()
    app.mount("/static", StaticFiles(directory="static"), name="static")

    @app.get("/")
    def root(fmt: str = FMT_HTML):
        try:
            return handle_format(models.all_staff(), fmt, views.all_staff)
        except AppException as exc:
            raise HTTPException(status_code=404, detail=f"Error serving all staff: {exc}")

    @app.get("/exp/{staff_id}")
    def exp(staff_id: int, fmt: str = FMT_HTML):
        try:
            return handle_format(models.experiments(staff_id), fmt, views.experiments, staff_id)
        except AppException as exc:
            raise HTTPException(status_code=404, detail=f"Error serving experiments for {staff_id}: {exc}")

    @app.get("/heartbeat")
    def heartbeat(fmt: str = FMT_HTML):
        try:
            return handle_format(HEARTBEAT, fmt, views.heartbeat)
        except AppException as exc:
            raise HTTPException(status_code=404, detail=f"Error serving heartbeat: {exc}")

    return app


app = make_server()

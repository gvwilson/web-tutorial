"""Serve data from data model layer."""

from fastapi import FastAPI, HTTPException

import models
import views

from exceptions import AppException


HEARTBEAT = {"message": "alive"}
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
    def root(fmt: str = FMT_JSON):
        try:
            return handle_format(models.all_staff(), fmt, views.all_staff)
        except AppException as exc:
            raise HTTPException(status_code=404, detail=f"Error serving all staff: {exc}")

    @app.get("/heartbeat")
    def heartbeat(fmt: str = FMT_JSON):
        try:
            return handle_format(HEARTBEAT, fmt, views.heartbeat)
        except AppException as exc:
            raise HTTPException(status_code=404, detail=f"Error serving heartbeat: {exc}")

    @app.get("/col/{name}")
    def column(name: str, fmt: str = FMT_JSON):
        try:
            return handle_format(models.column(name), fmt, views.column)
        except AppException as exc:
            raise HTTPException(status_code=404, detail=f"Error serving column {name}: {exc}")

    @app.get("/row/{staff_id}")
    def row(staff_id: int, fmt: str = FMT_JSON):
        try:
            return handle_format(models.row(staff_id), fmt, views.row)
        except AppException as exc:
            raise HTTPException(status_code=404, detail=f"Error serving row {staff_id}: {exc}")

    return app


app = make_server()

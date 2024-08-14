"""Serve data from data model layer."""

from fastapi import FastAPI, HTTPException

import model


def make_server():
    """Build application and configure routes."""
    app = FastAPI()

    @app.get("/")
    def root():
        return model.all_staff()

    @app.get("/col/{name}")
    def column(name: str):
        try:
            return model.column(name)
        except model.ModelException as exc:
            raise HTTPException(status_code=404, detail=f"Error serving column {name}: {exc}")

    @app.get("/row/{staff_id}")
    def row(staff_id: int):
        try:
            return model.row(staff_id)
        except model.ModelException as exc:
            raise HTTPException(status_code=404, detail=f"Error serving row {staff_id}: {exc}")


app = make_server()

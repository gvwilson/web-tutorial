"""Configure multiple routes."""

from fastapi import FastAPI, HTTPException
import polars as pl

import util

def make_server(data):
    """Build application and configure routes."""
    app = FastAPI()
    app.data = data

    @app.get("/")
    def root():
        return app.data.write_json()

    @app.get("/col/{name}")
    def column(name: str):
        if name not in app.data.columns:
            raise HTTPException(status_code=404, detail=f"Column {name} not found")
        return list(app.data[name])

    @app.get("/row/{staff_id}")
    def row(staff_id: int):
        if staff_id not in app.data["staff_id"]:
            raise HTTPException(status_code=404, detail=f"Row {staff_id} not found")
        return app.data.filter(pl.col("staff_id") == staff_id).row(0, named=True)

    return app


data = util.load_data()
app = make_server(data)

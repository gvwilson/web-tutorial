"""Configure multiple routes."""

from fastapi import FastAPI
import polars as pl

import util

def make_server(data):
    """Build application and configure routes."""
    app = FastAPI()
    app.data = data

    @app.get("/")
    def root():
        return app.data.to_dicts()

    @app.get("/col/{name}")
    def column(name: str):
        return list(app.data[name])

    @app.get("/row/{staff_id}")
    def row(staff_id: int):
        return app.data.filter(pl.col("staff_id") == staff_id).row(0, named=True)

    return app


data = util.load_data()
app = make_server(data)

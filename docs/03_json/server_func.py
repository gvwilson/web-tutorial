"""Define application in function."""

from fastapi import FastAPI

import util


def make_server(data):
    """Build application and configure routes."""
    app = FastAPI()
    app.data = data

    @app.get("/")
    def root():
        # Convert the Polars DataFrame to a list of dictionaries
        return app.data.to_dicts()

    return app


data = util.load_data()
app = make_server(data)
